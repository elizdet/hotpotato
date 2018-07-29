from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from potato.config import DB_CONNECTION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION
db = SQLAlchemy(app)

# Register models.
import potato.models

# Register controllers.
import potato.controllers