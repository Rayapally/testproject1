from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///internships.db'

db = SQLAlchemy(app)

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    application_deadline = db.Column(db.Date, nullable=False)

class InternshipForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    application_deadline = DateField('Application Deadline', validators=[DataRequired()])

@app.route('/')
def index():
    internships = Internship.query.all()
    return render_template('index.html', internships=internships)

@app.route('/apply/<int:internship_id>', methods=['POST'])
def apply(internship_id):
    # Handle the application logic here
    flash('Application submitted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
