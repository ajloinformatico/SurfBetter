from flask_restful import Api, Resource, reqparse
from flask import request
from models import User


# Class with get and post
class ExampleModel(Resource):
    # get at ('/flask/hello')

    def post(self):
        """
        Add new user
        Returns: Json success

        """
        ret = {
            "status" : "success",
            "name" : "Juancho"
        }
        return ret


    class ExampleRoute(Resource):

        def get(self):
            ret = {
                'resultStatus': 'SUCCESS',
                'message': 'Hello im a response'
            }
            if True:
                return ret

            ret = {"resultStatus": "ERROR"}
            return ret

        def post(self):
            print(self)
            parser = reqparse.RequestParser()
            parser.add_argument('type', type=str)
            parser.add_argument('message', type="str")

            args = parser.parse_args()

            print(args)
            # note: post req needs to match the same args (type and message)

            request_type = args['type']  # get type
            request_json = args['message']  # get message
            # ret_status, ret_msg = ReturnData(request_type, request_json)
            # return directly the same request
            ret_status = request_type
            ret_msg = request_json

            # Build return if there is message or not
            # if message return message
            if ret_msg:
                message = f"Your Message Request: {ret_msg}"
            else:
                message = "There isnt nothing message"

            final_ret = {"status": "Success", "message": message}

            return final_ret


class UserController(Resource):
    """
    Controller for user
    """
    def get(self):
        ret = {
            "name" : "name example",
            "zxczxc": "sxdsdsdsd"
        }
        return ret



