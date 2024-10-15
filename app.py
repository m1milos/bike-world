from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/bike-selector', methods=['GET', 'POST'])
def bike_selector():
    recommended_bike = None
    if request.method == 'POST':
        bike_type = request.form.get('bike_type')
        suspension_type = request.form.get('suspension_type')
        riding_surface = request.form.get('riding_surface')
        primary_use = request.form.get('primary_use')
        wheel_size = request.form.get('wheel_size')
        budget = request.form.get('budget')
        electric_assist = 'electric_assist' in request.form

        if bike_type == 'mountain':
            if wheel_size == '24':
                if suspension_type == 'dual':
                    recommended_bike = {
                        'name': 'Polygon Siskiu D24 Dual Suspension Mountain Bike',
                        'image': 'polygon-siskiu-d24.webp',
                        'description': 'The Polygon Siskiu D24 is a high-quality dual suspension mountain bike designed for young riders or adults who prefer a more compact frame. With its 24-inch wheels and full suspension, it offers excellent control and comfort for various trail conditions.'
                    }
                elif suspension_type == 'hardtail':
                    recommended_bike = {
                        'name': 'Polygon Premier 24 Hardtail Mountain Bike',
                        'image': 'polygon-siskiu-d24.webp',  # Updated image for 24-inch hardtail
                        'description': 'The Polygon Premier 24 is a high-quality hardtail mountain bike designed for young riders or adults who prefer a more compact frame. With its 24-inch wheels and front suspension, it offers a perfect balance of efficiency and comfort for various trail conditions.'
                    }
            else:
                recommended_bike = {
                    'name': f"{suspension_type.capitalize() if suspension_type else 'Mountain'} Bike",
                    'image': 'mountain_bike.jpg',
                    'description': f"A {'mountain' if not suspension_type else suspension_type} bike designed for off-road adventures. "
                }
        elif bike_type == 'road':
            recommended_bike = {
                'name': 'Road Bike',
                'image': 'road_bike.jpg',
                'description': "A lightweight bike designed for speed and efficiency on paved roads. Ideal for long distances, racing, or fast-paced rides on smooth surfaces."
            }
        elif bike_type == 'hybrid':
            recommended_bike = {
                'name': 'Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': "A versatile bike that combines features of road and mountain bikes, suitable for various terrains and uses. Offers a comfortable upright position and is great for commuting, fitness riding, and light trail use."
            }
        elif bike_type == 'cruiser':
            recommended_bike = {
                'name': 'Cruiser Bike',
                'image': 'cruiser_bike.jpg',
                'description': 'A comfortable bike for casual rides and leisurely cycling in flat areas. Features a relaxed upright position and wide tires, perfect for easy rides around town or along the beach.'
            }
        elif bike_type == 'electric':
            recommended_bike = {
                'name': 'Electric Bike',
                'image': 'electric_bike.jpg',
                'description': "An electric-assist bike, providing extra power for easier riding and longer distances. Ideal for commuters, those tackling hilly terrain, or riders wanting to extend their range."
            }
        else:
            # Fallback option if no specific bike type is selected
            recommended_bike = {
                'name': 'Versatile Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': "A versatile hybrid bike that combines features of various bike types, suitable for multiple terrains and uses. This bike is recommended based on your preferences for a well-rounded riding experience."
            }

        # Add suspension information to the description for all bike types
        if suspension_type and bike_type != 'mountain':
            if suspension_type == 'dual':
                recommended_bike['description'] += " Features front and rear suspension for maximum control on technical trails and rough terrain."
            elif suspension_type == 'hardtail':
                recommended_bike['description'] += " Equipped with front suspension, offering a balance of efficiency and comfort for various terrains."
            elif suspension_type == 'no_suspension':
                recommended_bike['description'] += " A rigid frame provides direct feedback from the terrain, ideal for riders who prefer simplicity and efficiency."

        # Additional customization based on other factors
        if riding_surface == 'gravel' and bike_type != 'mountain':
            recommended_bike['name'] = f"Gravel-ready {recommended_bike['name']}"
            recommended_bike['description'] += " This bike has been adapted for gravel riding with slightly wider tires and a more stable frame geometry."

        if primary_use == 'commuting' and bike_type not in ['cruiser', 'electric']:
            recommended_bike['description'] += " For commuting, this bike can be equipped with racks and fenders to make your daily rides more convenient."

        if electric_assist and bike_type != 'electric':
            recommended_bike['name'] = f"Electric {recommended_bike['name']}"
            recommended_bike['description'] += " As per your preference, this bike comes with electric assist, providing extra power when you need it."

        if wheel_size and wheel_size != '24':
            recommended_bike['description'] += f" Recommended with {wheel_size} inch wheels, which are well-suited for this type of bike and your riding preferences."

    return render_template('bike_selector.html', recommended_bike=recommended_bike)

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

@app.route('/videos')
def videos():
    return render_template('videos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
