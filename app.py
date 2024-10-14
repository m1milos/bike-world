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
        budget = request.form.get('budget')

        # Simple logic to recommend a bike based on user preferences
        if riding_surface == 'road' and primary_use in ['commuting', 'exercise', 'racing']:
            recommended_bike = {
                'name': 'Road Bike',
                'image': 'road_bike.jpg',
                'description': 'A lightweight and fast bike perfect for paved roads and speed.'
            }
        elif riding_surface == 'off_road':
            recommended_bike = {
                'name': 'Mountain Bike',
                'image': 'mountain_bike.jpg',
                'description': 'A sturdy bike built for rough terrains and off-road adventures.'
            }
        elif riding_surface == 'mixed' or primary_use in ['commuting', 'leisure']:
            recommended_bike = {
                'name': 'Hybrid Bike',
                'image': 'hybrid_bike.jpg',
                'description': 'A versatile bike suitable for various terrains and casual riding.'
            }
        elif primary_use == 'leisure' and budget == 'low':
            recommended_bike = {
                'name': 'Cruiser Bike',
                'image': 'cruiser_bike.jpg',
                'description': 'A comfortable bike for casual rides and leisurely cycling.'
            }
        else:
            recommended_bike = {
                'name': 'Electric Bike',
                'image': 'electric_bike.jpg',
                'description': 'A bike with electric assistance, suitable for various uses and terrains.'
            }

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
