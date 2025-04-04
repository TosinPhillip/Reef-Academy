from flask import Flask, render_template, jsonify
import os
from mongo_db import *
from login import *


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

db = client["Users"]
users_collection = db["User_Details"]



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
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')

@app.route('/select_test')
def select_test():
    return render_template('select_exam.html',title='Select Test')

@app.route('/sign_in_page')
def sign_in_page():
    return render_template("sign_in_page.html")

@app.route('/layout')
def layout():
    return render_template('layout.html')

    
@app.route("/login_with_google")
def login_with_google():
    return google.authorize_redirect(url_for("callback", _external=True))

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

    return render_template('profile.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})

@app.route("/profile")
@login_required
def profile():
    return jsonify({
        "name": current_user.name,
        "email": current_user.id,
        "picture": current_user.picture
    })


if __name__ == '__main__':
    app.run(debug=True)