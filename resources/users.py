from flask import Blueprint, url_for

from flask_restful import (Resource, Api, reqparse,
                           inputs, marshal_with, fields, marshal)

import models

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'password': fields.String(default=''),
    'created_at': fields.DateTime
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(user_fields)
    def post(self):
        args = self.reqparse.parse_args()
        user = models.User.create(**args)
        return (url_for('resources.users.user'), 201,
                {'Location': url_for('resources.users.user', id=user.id)})


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='reviews'
)
# api.add_resource(
#     User,
#     '/users/<int:id>',
#     endpoint='review'
# )
