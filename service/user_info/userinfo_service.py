from marshmallow import EXCLUDE

from model.user_info.user_info_model import Userinfo
from schemas.user_info.user_info_schema import UserinfoSchema

class UserinfoService:
    @staticmethod
    def create_userinfo(data) -> Userinfo:
        userinfo_model = UserinfoSchema().load(data, unknown=EXCLUDE)
    
        if type(userinfo_model) is dict:
            userinfo = Userinfo(**userinfo_model)
        else:
           userinfo = userinfo_model

        userinfo.insert()
        return userinfo

    @staticmethod
    def update_userinfo(data, userinfo) -> Userinfo:
        userinfo_data = UserinfoSchema().dump(data)
        if userinfo_data:
            for key, value in userinfo_data.items():
                setattr(userinfo, key, value)
            userinfo.update()
            return userinfo
        else:
            return None