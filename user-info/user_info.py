from flask import Flask, jsonify, request
from flask.views import View
from constants import USER_CURRENT_BOOKINGS, USER_BOOKING_HISTORY
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "new-secret"
jwt = JWTManager(app)


class UserInfo(View):

    methods = ["GET"]

    @jwt_required
    def dispatch_request(self, userid):
        return jsonify({"Upcoming": USER_CURRENT_BOOKINGS,
                        "Past Orders": USER_BOOKING_HISTORY}), 200


class CreateOrder(View):

    methods = ["POST"]

    @jwt_required
    def dispatch_request(self):
        print(f" THe query params: {request.args}")
        return jsonify({"Movie": "The Dark Knight",
                        "userid": 1,
                        "username": "dineshkumarkb",
                        "Show time": "23-04-2020 7:40 P.M",
                        "TransactionId": "1234452A",
                        "Booking Status": "Successful",
                        "Booking Date and Time": "Nov 8 12:40 P.M"})


class GetCart(View):

    methods = ["GET"]

    @jwt_required
    def dispatch_request(self):
        snacks_info = "Get this information from snacks_info"
        return jsonify({"Items": {"Movie": "The Dark Knight",
                                  "Time": "10:30 A.M",
                                  "Seats": 2,
                                  "Snacks": {"Popcorn": 2,
                                             "Coffee": 2}
        }})


if __name__ == "__main__":
    app.add_url_rule("/userinfo/<userid>", view_func=UserInfo.as_view("userinfo"))
    app.add_url_rule("/booktickets/neworder", view_func=CreateOrder.as_view("createorder"))
    app.add_url_rule("/booktickets/getcart/", view_func=GetCart.as_view("getcart"))
    app.run(host="0.0.0.0", debug=True, port=5002)
