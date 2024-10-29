from flask import Flask 
from dotenv import load_dotenv
from .routes.routes_user import users_bp

load_dotenv() 

def create_app(): 
    app = Flask(__name__)
    app.register_blueprint(users_bp, url_prefix='/api') 
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
