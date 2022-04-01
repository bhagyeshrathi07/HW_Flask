#discussed with : Pranav Arora, Pranav Pandey
from flask import Flask

myobj = Flask(__name__)

myobj.config.from_mapping(SECRET_KEY = 'secret_key')

from app import routes