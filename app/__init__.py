from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initializing the Flask app
app = Flask(__name__)

# Configuring the SQLite database URI and disabling track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing the SQLAlchemy instance for database operations
db = SQLAlchemy(app)

# Setting up Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Importing the Blueprint for the routes
from app.routes import main as main_blueprint
# Registering the Blueprint with the Flask app
app.register_blueprint(main_blueprint)

# Running the Flask app with debugging enabled
if __name__ == "__main__":
    app.run(debug=True)
