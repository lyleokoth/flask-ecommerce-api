from flask import Flask

app = Flask(__name__)

from ecom import models, routes
