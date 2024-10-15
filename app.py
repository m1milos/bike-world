from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bike-selector', methods=['GET', 'POST'])
def bike_selector():
    if request.method == 'POST':
        bike_type = request.form.get('bike_type')
        suspension_type = request.form.get('suspension_type')
        riding_surface = request.form.get('riding_surface')
        primary_use = request.form.get('primary_use')
        wheel_size = request.form.get('wheel_size')
        budget = request.form.get('budget')
        electric_assist = request.form.get('electric_assist')

        # Simple logic to recommend a bike
        recommended_bike = {
            'name': 'Generic Bike',
            'image': 'road_bike.jpg',
            'description': 'A versatile bike suitable for various riding conditions.'
        }

        if bike_type == 'mountain':
            if suspension_type == 'dual':
                recommended_bike['name'] = 'Full Suspension Mountain Bike'
                recommended_bike['image'] = 'polygon-siskiu-d24.webp'
                recommended_bike['description'] = 'A high-performance mountain bike with front and rear suspension, perfect for rough terrains and technical trails.'
            elif suspension_type == 'hardtail':
                recommended_bike['name'] = 'Hardtail Mountain Bike'
                recommended_bike['image'] = 'polygon.webp'
                recommended_bike['description'] = 'A versatile mountain bike with front suspension, ideal for a mix of trail riding and cross-country adventures.'
            else:
                recommended_bike['name'] = 'Rigid Mountain Bike'
                recommended_bike['image'] = 'mountain_bike.jpg'
                recommended_bike['description'] = 'A lightweight and efficient mountain bike without suspension, best for smooth trails and cross-country riding.'

        elif bike_type == 'road':
            recommended_bike['name'] = 'Road Bike'
            recommended_bike['image'] = 'Roadbike.jpg'
            recommended_bike['description'] = 'A lightweight and aerodynamic bike designed for speed on paved roads.'

        elif bike_type == 'hybrid':
            recommended_bike['name'] = 'Hybrid Bike'
            recommended_bike['image'] = 'hybrid_bike.jpg'
            recommended_bike['description'] = 'A versatile bike that combines features of both road and mountain bikes, suitable for various terrains.'

        elif bike_type == 'cruiser':
            recommended_bike['name'] = 'Cruiser Bike'
            recommended_bike['image'] = 'cruiser_bike.jpg'
            recommended_bike['description'] = 'A comfortable, laid-back bike perfect for casual rides on flat terrain.'

        elif bike_type == 'electric' or electric_assist:
            recommended_bike['name'] = 'Electric Bike'
            recommended_bike['image'] = 'electric_bike.jpg'
            recommended_bike['description'] = 'A bike with an electric motor to assist pedaling, great for commuting or longer rides.'

        return render_template('bike_selector.html', recommended_bike=recommended_bike)

    return render_template('bike_selector.html')

@app.route('/bike-types')
def bike_types():
    bikes = [
        {
            'name': 'Road Bike',
            'image': 'Roadbike.jpg',
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
