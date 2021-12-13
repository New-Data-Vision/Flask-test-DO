from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy, SQLAlchemy

app = Flask(__name__)
#db_name = 'vision.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doadmin:eFVn8uvcNrbMIqTY@db-postgresql-nyc3-94812-do-user-10431606-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Blogpost(db.Model):
    __tablename__ = 'blogpost'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date_post = db.Column(db.DateTime)
    content = db.Column(db.Text)
    reading_time = db.Column(db.Float)


# Route for Home
@app.route('/')
def index():
    return render_template('index.html')

# Route for About
@app.route('/about')
def about():
    return render_template("about.html")

# Route for Contact
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Route for Customer Contact
@app.route('/customer_c')
def customer_c():
    return render_template("customer_c.html")
