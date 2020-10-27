#`````````````````````````````
#
#    Developed by Ivan Seagull
#
#`````````````````````````````

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random


login, password = "login", "password"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and not (event.from_me):
            print('Notice has arrived: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Message: ' + str(event.text))
            print('From', event.user_id)
