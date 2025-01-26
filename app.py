from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import random

app = Flask(__name__)

# MySQL Database connection details
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='flask_user',
        password='9090',
        database='career_counselor'
    )

# Routes for the app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    success_message = None  # Variable to hold success message
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        education_level = request.form['education_level']
        field_of_study = request.form['field_of_study']
        current_institution = request.form['current_institution']
        career_interests = request.form['career_interests']
        short_term_goals = request.form['short_term_goals']
        long_term_goals = request.form['long_term_goals']
        learning_style = request.form['learning_style']
        challenges = request.form['challenges']

        try:
            # Database connection and insert code here
            connection = get_db_connection()
            cursor = connection.cursor()

            insert_query = '''
                INSERT INTO form_submissions (name, email, phone, education_level, field_of_study, 
                                              current_institution, career_interests, short_term_goals, 
                                              long_term_goals, learning_style, challenges)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (name, email, phone, education_level, field_of_study,
                                          current_institution, career_interests, short_term_goals,
                                          long_term_goals, learning_style, challenges))
            connection.commit()

            success_message = 'Form submitted successfully!'  # Success message to be displayed
        except Error as e:
            print(f"Error: {e}")
            success_message = 'There was an error while submitting your form.'
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    return render_template('form.html', success_message=success_message)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    # List of Font Awesome icons to assign randomly
    icons = [
        'fas fa-user-tie',  # Businessman
        'fas fa-laptop-code',  # Developer
        'fas fa-palette',  # Designer
        'fas fa-chart-line',  # Data Scientist
        'fas fa-cogs',  # Engineer
    ]

    # Fixed team member details
    team_members = [
        {'name': 'Karthik Nallapu', 'role': 'Founder & CEO', 'photo': 'static/images/karthik.jpg'},  # Fixed image
        {'name': 'Suri BhAAi', 'role': 'Chief Technical Officer', 'icon': random.choice(icons)},  # Random icon for Suri BhAAi
        {'name': 'Alex Johnson', 'role': 'UI/UX Designer', 'photo': 'static/images/alex.jpg'},  # Fixed image
        {'name': 'Emily Davis', 'role': 'Lead Data Scientist', 'photo': 'static/images/emily.jpg'},  # Fixed image
    ]

    return render_template('about.html', team_members=team_members)

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

if __name__ == '__main__':
    app.run(debug=True)
