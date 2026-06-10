import random   
from flask import Blueprint, render_template

home_Routes = Blueprint('home', __name__, template_folder="templates", root_path=f"C:\\Users\\eduar\\Documents\\GitHub\\megaloja-project")
@home_Routes.route('/')
def home():
    return render_template('index.html')