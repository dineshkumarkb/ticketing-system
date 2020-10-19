from flask import Blueprint, jsonify, Flask, request
from constants import MOVIE_LIST, MOVIE_INFO


movie_list = Blueprint(name="user", import_name=__name__, url_prefix="/movies" )


@movie_list.route("/getall", methods=["GET"])
def get_movies():
    return jsonify(MOVIE_LIST), 200


@movie_list.route("/getinfo", methods=["GET"])
def get_movie_info():
    movie_name = request.args.get("name").title()
    if movie_name not in MOVIE_LIST.values():
        return jsonify(f" No movie information found ")
    cine_info = MOVIE_INFO.get(movie_name)
    print(f" The cineinfo is {cine_info} ")
    return jsonify(cine_info), 200


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(movie_list)
    app.run(host="0.0.0.0", debug=True, port=5000)



