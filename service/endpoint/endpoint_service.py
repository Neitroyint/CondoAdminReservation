from controller.status.status_controller import StatusController
from controller.user.user_controller import UserController
from controller.user_id.user_id_controller import UserIdController
from utils.constants import env_const

def add_endpoints(api):
    ctr_list = [StatusController, 
        UserController,
        UserIdController]
    ep = env_const.APIENDPOINT
    for ctr in ctr_list:
        api.add_resource(ctr, f'{ep}{ctr.route}')
