import vk
from vk.exceptions import VkAPIError

def job():
    my_app_id = 111111
    user_login = ''

    user_password = 'xxxxxx'

    session = vk.AuthSession(scope='groups', app_id=my_app_id, user_login=user_login, user_password=user_password)

    api = vk.API(session)

    api.board.createComment(group_id='111111',topic_id='111111', message='1111111', v="5.92")

n = 0
while n != 1:
    try:
        job()
        n += 1
    except vk.exceptions.VkAPIError as vk_error:
        pass