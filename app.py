from flask import Flask, render_template, send_file, request, flash, redirect, url_for
import requests
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bike-types')
def bike_types():
    bikes = [
        {
            'name': 'Road Bike',
            'image': 'road_bike.jpg',
            'description': 'Designed for speed and efficiency on paved roads.'
        },
        {
            'name': 'Mountain Bike',
            'image': 'mountain_bike.jpg',
            'description': 'Built for off-road cycling on rough terrain.'
        },
        {
            'name': 'Hybrid Bike',
            'image': 'hybrid_bike.jpg',
            'description': 'A versatile bike that combines features of road and mountain bikes.'
        },
        {
            'name': 'Cruiser Bike',
            'image': 'cruiser_bike.jpg',
            'description': 'Comfortable bikes for casual riding on flat surfaces.'
        },
        {
            'name': 'Electric Bike',
            'image': 'electric_bike.jpg',
            'description': 'Equipped with an electric motor for assisted pedaling.'
        }
    ]
    return render_template('bike_types.html', bikes=bikes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically send an email or save the message to a database
        # For now, we'll just flash a success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/bike-selector', methods=['GET', 'POST'])
def bike_selector():
    recommended_bike = None
    if request.method == 'POST':
        bike_type = request.form.get('bike_type')
        riding_surface = request.form.get('riding_surface')
        primary_use = request.form.get('primary_use')
        experience_level = request.form.get('experience_level')
        wheel_size = request.form.get('wheel_size')
        budget = request.form.get('budget')
        electric_assist = request.form.get('electric_assist') == 'on'

        # Enhanced logic to recommend a bike based on user preferences
        if bike_type == 'road':
            if experience_level == 'advanced' and budget == 'high' and wheel_size == '700c':
                recommended_bike = {
                    'name': 'Carbon Fiber Road Bike',
                    'image': 'carbon_road_bike.jpg',
                    'description': 'A high-performance road bike with a lightweight carbon fiber frame, perfect for racing and long rides. Its aerodynamic design and responsive handling make it ideal for experienced riders looking to maximize speed and efficiency on paved roads.'
                }
            else:
                recommended_bike = {
                    'name': 'Aluminum Road Bike',
                    'image': 'road_bike.jpg',
                    'description': 'A versatile road bike with an aluminum frame, suitable for commuting and fitness riding. It offers a good balance of speed and comfort, making it an excellent choice for riders of all levels who want to enjoy road cycling without breaking the bank.'
                }
        elif bike_type == 'mountain':
            if experience_level == 'advanced' and budget == 'high' and wheel_size in ['27.5', '29']:
                recommended_bike = {
                    'name': 'Full Suspension Mountain Bike',
                    'image': 'full_suspension_mtb.jpg',
                    'description': 'A high-end mountain bike with front and rear suspension, ideal for technical trails and downhill riding. The full suspension system provides maximum control and comfort on rough terrain, allowing you to tackle the most challenging off-road adventures with confidence.'
                }
            else:
                recommended_bike = {
                    'name': 'Hardtail Mountain Bike',
                    'image': 'mountain_bike.jpg',
                    'description': 'A durable mountain bike with front suspension, great for off-road trails and beginners. The hardtail design offers a good balance of efficiency and comfort, making it suitable for a wide range of trail conditions and skill levels.'
                }
        elif bike_type == 'hybrid':
            recommended_bike = {
                'name': 'Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': "A versatile bike that combines features of road and mountain bikes, suitable for various terrains and uses. Hybrid bikes offer a comfortable upright position, medium-width tires for diverse surfaces, and a wide range of gears. They're an excellent all-around choice for riders who want one bike for commuting, fitness riding, and light trail use."
            }
        elif bike_type == 'cruiser':
            recommended_bike = {
                'name': 'Cruiser Bike',
                'image': 'cruiser_bike.jpg',
                'description': 'A comfortable bike for casual rides and leisurely cycling in flat areas. With a relaxed upright position, wide tires, and often a single-speed drivetrain, cruiser bikes are perfect for easy rides around town or along the beach. They prioritize comfort and style over speed, making them ideal for casual cyclists.'
            }
        elif bike_type == 'electric':
            recommended_bike = {
                'name': 'Electric Bike',
                'image': 'electric_bike.jpg',
                'description': "An electric-assist bike, providing extra power for easier riding and longer distances. E-bikes are perfect for riders who want to extend their range, tackle hilly terrain with ease, or simply arrive at their destination without breaking a sweat. They're particularly useful for commuters and those with physical limitations."
            }
        else:
            # Fallback option if no specific bike type is selected
            recommended_bike = {
                'name': 'Versatile Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': "A versatile hybrid bike that combines features of various bike types, suitable for multiple terrains and uses. This bike is recommended based on your preferences for a well-rounded riding experience."
            }

        # Additional customization based on other factors
        if riding_surface == 'gravel' and bike_type != 'mountain':
            recommended_bike['name'] = f"Gravel-ready {recommended_bike['name']}"
            recommended_bike['description'] += " This bike has been adapted for gravel riding with slightly wider tires and a more stable frame geometry."

        if primary_use == 'commuting' and bike_type not in ['cruiser', 'electric']:
            recommended_bike['description'] += " For commuting, this bike can be equipped with racks and fenders to make your daily rides more convenient."

        if electric_assist and bike_type != 'electric':
            recommended_bike['name'] = f"Electric {recommended_bike['name']}"
            recommended_bike['description'] += " As per your preference, this bike comes with electric assist, providing extra power when you need it."

        recommended_bike['description'] += f" Recommended with {wheel_size} inch wheels, which are well-suited for this type of bike and your riding preferences."

    return render_template('bike_selector.html', recommended_bike=recommended_bike)

@app.route('/static/images/dual_suspension_mountain_bike.jpg')
def serve_dual_suspension_bike_image():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Dual_suspension_mountain_bike.jpg/640px-Dual_suspension_mountain_bike.jpg"
    response = requests.get(image_url)
    return send_file(
        io.BytesIO(response.content),
        mimetype='image/jpeg',
        download_name='dual_suspension_mountain_bike.jpg'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
