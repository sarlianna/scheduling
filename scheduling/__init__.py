from flask import Flask
app = Flask(__name__)

import scheduling.views
import scheduling.api.routes
