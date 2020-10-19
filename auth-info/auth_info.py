from flask import jsonify, Flask, request
from flask_jwt_extended import JWTManager, create_access_token
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
jwt = JWTManager(app)


@app.route("/auth/getauthtoken")
def get_auth_token():

    user_name = request.args.get("username")
    access_token = create_access_token(user_name)
    return jsonify(access_token), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5003)



