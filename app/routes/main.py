from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/about")
def about():
    return "<h1>About our Donation Platform</h1>"


@main_bp.route("/signup")
def signup():
    return render_template("signup.html")


@main_bp.route("/signup-hospital")
def signup_hospital():
    return render_template("signup-hospital.html")
    
    
@main_bp.route("/login-hospital")
def login_hospital():
    return render_template("login-hospital.html")


@main_bp.route("/requests")
def requests():
    return render_template("requests.html")


@main_bp.route("/d-donor")
def donor_dashboard():
    return render_template("dashboards/donor.html")
    
    
@main_bp.route("/d-hospital")
def hospital_dashboard():
    return render_template("dashboards/hospital.html")
    
    
@main_bp.route("/d-admin")
def admin_dashboard():
    return render_template("dashboards/admin.html")
