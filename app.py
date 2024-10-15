from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

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
