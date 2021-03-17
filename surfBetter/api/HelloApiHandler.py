from flask_restful import Api, Resource, reqparse

# Class with get and post
class HelloApiHandler(Resource):
    # get at ('/flask/hello')
    def get(self):
        ret = {
            'resultStatus': 'SUCCESS',
            'message': 'Hello Api Handler'
        }
        return ret
    
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type="str")

        args = parser.parse_args()

        print(args)
        # note: post req needs to match the same args (type and message)

        request_type = args['type'] # get type
        request_json = args['message'] # get message
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


