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
        riding_surface = request.form.get('riding_surface')
        primary_use = request.form.get('primary_use')
        experience_level = request.form.get('experience_level')
        frame_size = request.form.get('frame_size')
        budget = request.form.get('budget')
        electric_assist = request.form.get('electric_assist') == 'on'

        # Enhanced logic to recommend a bike based on user preferences
        if riding_surface == 'road' and primary_use in ['commuting', 'exercise', 'racing']:
            if experience_level == 'advanced' and budget == 'high':
                recommended_bike = {
                    'name': 'Carbon Fiber Road Bike',
                    'image': 'carbon_road_bike.jpg',
                    'description': 'A high-performance road bike with a lightweight carbon fiber frame, perfect for racing and long rides.'
                }
            else:
                recommended_bike = {
                    'name': 'Aluminum Road Bike',
                    'image': 'road_bike.jpg',
                    'description': 'A versatile road bike with an aluminum frame, suitable for commuting and fitness riding.'
                }
        elif riding_surface == 'off_road' or primary_use == 'mountain_biking':
            if experience_level == 'advanced' and budget == 'high':
                recommended_bike = {
                    'name': 'Full Suspension Mountain Bike',
                    'image': 'full_suspension_mtb.jpg',
                    'description': 'A high-end mountain bike with front and rear suspension, ideal for technical trails and downhill riding.'
                }
            else:
                recommended_bike = {
                    'name': 'Hardtail Mountain Bike',
                    'image': 'mountain_bike.jpg',
                    'description': 'A durable mountain bike with front suspension, great for off-road trails and beginners.'
                }
        elif riding_surface == 'gravel' or primary_use == 'touring':
            recommended_bike = {
                'name': 'Gravel Bike',
                'image': 'gravel_bike.jpg',
                'description': 'A versatile bike designed for mixed terrain, perfect for long rides on unpaved roads and light trails.'
            }
        elif riding_surface == 'urban' and primary_use == 'commuting':
            recommended_bike = {
                'name': 'City Bike',
                'image': 'city_bike.jpg',
                'description': 'A comfortable and practical bike for urban commuting, equipped with fenders and a rack.'
            }
        elif primary_use == 'leisure' and budget == 'low':
            recommended_bike = {
                'name': 'Cruiser Bike',
                'image': 'cruiser_bike.jpg',
                'description': 'A comfortable bike for casual rides and leisurely cycling in flat areas.'
            }
        elif primary_use == 'trick_riding':
            recommended_bike = {
                'name': 'BMX Bike',
                'image': 'bmx_bike.jpg',
                'description': 'A small, sturdy bike designed for tricks and stunts in bike parks or urban environments.'
            }
        else:
            recommended_bike = {
                'name': 'Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': 'A versatile bike that combines features of road and mountain bikes, suitable for various terrains and uses.'
            }

        if electric_assist:
            recommended_bike = {
                'name': f"Electric {recommended_bike['name']}",
                'image': 'electric_bike.jpg',
                'description': f"An electric-assist version of the {recommended_bike['name'].lower()}, providing extra power for easier riding and longer distances."
            }

        recommended_bike['description'] += f" Available in size {frame_size}."

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
