from flask import Blueprint, jsonify, Flask, request
from constants import SNACKS_LIST

food_list = Blueprint(name="food", import_name=__name__, url_prefix="/food" )


@food_list.route("/getall", methods=["GET"])
def get_all_food():
    return jsonify(SNACKS_LIST), 200


@food_list.route("/getsnacks/<orderid>", methods=["GET"])
def get_movie_info(orderid):
    order_id = orderid
    print(f" The order_id is {order_id} ")
    user_id = request.args.get("user_id", 1)
    print(f" The user id is {user_id}")
    date = request.args.get("date", "10-03-2019")
    return jsonify({"Item1": {"Popcorn": SNACKS_LIST.get("Popcorn")},
                    "Item2": {"Colddrink": SNACKS_LIST.get("Colddrink")}}), 200


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(food_list)
    app.run(host="0.0.0.0", debug=True, port=5001)



