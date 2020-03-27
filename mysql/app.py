from flask import Flask, abort
import curd.curd

# route
from route.admin import admin_route
from route.errors import errors

app = Flask(__name__)
app.register_blueprint(admin_route, url_prefix='/admin')
app.register_blueprint(errors)

if __name__ == "__main__":
    app.run(port=5000, debug=True)