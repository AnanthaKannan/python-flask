from flask import Flask, request, Response
from database.db import initialize_db
# from database.models import Movie
# route
from route.admin import admin_route
from route.errors import errors

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/admin_check'
}

db = initialize_db(app)
app.register_blueprint(admin_route, url_prefix='/admin')
app.register_blueprint(errors)
# @app.route('/admin/getAllAdmin')
# def get_movies():
#     movies = Movie.objects().to_json()
#     return Response(movies, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(port=5000, debug=True)