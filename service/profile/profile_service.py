from model.user.user_model import User
from service.identification.identification_service import IdentificationService
from service.user.user_service import UserService
from service.user_info.userinfo_service import UserinfoService
from utils.custom_errors.custom_errors import CustomError

class ProfileService:
    @staticmethod
    def create_profile(data) -> User:
        user = User.query.get(data['id_user'])

        if user is None:
            raise CustomError.NotFoundError("User id not found")
        if user.id_userinfo is not None:
            raise CustomError.AlreadyExistsError("Profile already created for the user")

        identification = IdentificationService.create_identification(data)
        data['id_identification'] = identification.id_identification

        userinfo = UserinfoService.create_userinfo(data)
        user_info_data = {
            'id_userinfo': userinfo.id_userinfo
        }
        UserService.update_user(user_info_data, user)

        return user

    @staticmethod
    def update_profile(id, data) -> User:
        user = User.query.get(id)
       
        if user is None:
            raise CustomError.NotFoundError("User id not found")
        
        IdentificationService.update_identification(data, user.userinfo.identification)
        UserinfoService.update_userinfo(data, user.userinfo)
        UserService.update_user(data, user)

        return user
