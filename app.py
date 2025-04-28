from flask import Flask, render_template, jsonify, redirect, url_for, session, flash
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Imports to manage flask login details
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Database imports
from db.mongo_db import users_db

# Login imports
from sign_in.google_login import google_func




# Load environment variables
load_dotenv()


#Instantiate the appp
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


# The database imports here
users_collection = users_db["User_Details"]


# Google log in function
google = google_func(app)




# Flask-Login setup
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)



# User set up 
class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data["email"]
        self.name = user_data["name"]
        self.picture = user_data["picture"]
        
        

@login_manager.user_loader
def load_user(user_id):
    user_data = users_collection.find_one({"email": user_id})
    return User(user_data) if user_data else None




# Routes

# Home page
@app.route('/')
def index():
    return render_template('index.html')

#  Admin page
@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')

# Test selection page
@app.route('/select_test')
def select_test():
    return render_template('select_exam.html',title='Select Test')

# Sigb in page
@app.route('/sign_in_page')
def sign_in_page():
    
    return render_template("sign_in_page.html", default_message="Test is the true proof of ability.")

# Lay out page
@app.route('/layout')
def layout():
    return render_template('layout.html')

# Option to log in with google account  
@app.route("/login_with_google")
def login_with_google():
    return google.authorize_redirect(url_for("callback", _external=True))

# After google login
# After google login
@app.route("/login/callback")
def callback():
    token = google.authorize_access_token()
    user_info = google.get("https://www.googleapis.com/oauth2/v2/userinfo").json()

    # Check if user exists
    existing_user = users_collection.find_one({"email": user_info["email"]})
    if not existing_user:
        users_collection.insert_one(user_info)  # Store new user

    user = User(user_info)
    login_user(user)

    return redirect(url_for("profile"))  # Redirect to profile route

# log out page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.")
    return redirect(url_for("sign_in_page"))  
    
   

# Profile page
@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', user_info={
        "name": current_user.name,
        "email": current_user.id,
        "picture": current_user.picture
    })


if __name__ == '__main__':
    app.run(debug=True)