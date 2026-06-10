import random
from flask import Flask, url_for,render_template
from routes.home import home_Routes

app = Flask(__name__,template_folder="templates",root_path=f"C:\\Users\\eduar\\Documents\\GitHub\\megaloja-project\\megaloja-project-main",instance_relative_config=True)

app.register_blueprint(home_Routes,url_prefix='/')
# rotas
@app.route('/')
def home():
    return render_template('index.html')
#execução
app.run(debug=True)
