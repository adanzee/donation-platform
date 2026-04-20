from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/about")
def about():
    return "<h1>About our Donation Platform</h1>"


@main_bp.route("/register")
def register():
    return render_template("register.html")


@main_bp.route("/d-donor")
def donor_dashboard():
    return render_template("dashboards/donor.html")
    
    
@main_bp.route("/d-hospital")
def hospital_dashboard():
    return render_template("dashboards/hospital.html")
    
    
@main_bp.route("/d-admin")
def admin_dashboard():
    return render_template("dashboards/admin.html")
