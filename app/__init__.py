from flask import Flask

app = Flask(__name__)

from app.module.controller import *
from app.module.const import *

def trades():
    return None