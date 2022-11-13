from flask import request
from flask_restplus import Resource

from flask_jwt_extended import jwt_required, get_jwt_identity
from middleware.auth import token_required

from schemas.dto import UserDto
from services.user_service import UserServices
from utils import status


api = UserDto.api

@api.route('/me')
class CurrentUserRoute(Resource):
    @api.doc('get_current_user')
    @api.marshal_list_with(UserDto.IUser, envelope='data')
    @jwt_required()
    def get(self):
        """Get Current User"""
        identity = get_jwt_identity()
        return UserServices().get_by_publicId(identity["publicId"])

    @api.doc('update_current_user')
    @api.marshal_list_with(UserDto.IUserUpdtae, envelope='data')
    @jwt_required()
    def patch(self):
        """Update Current User"""
        identity = get_jwt_identity()
        return UserServices().update_user_by_publicId(publicId=identity["publicId"], data=request.json)


@api.route('')
class CurrentUserRoute(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(UserDto.IUser, envelope='data')
    @jwt_required()
    def get(self):
        """List all registered users"""
        identity = get_jwt_identity()
        return UserServices().get_all_users()


# @api.route('/<publicId>')
# @api.param('publicId', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(UserDto.users)
#     @jwt_required()
#     def get(self, publicId):
#         """get a user given its identifier"""
#         user = get_a_user(publicId)
#         if not user:
#             api.abort(404)
#         else:
#             return user
