from model.user.user_model import User
from schemas.user.user_schema import UserSchema

class UserService:
    @staticmethod
    def update_user(data, user) -> User:
        user_data = UserSchema().dump(data)
        if user_data:
            for key, value in user_data.items():
                setattr(user, key, value)
            user.update()
            
            return user
        else:
            return None