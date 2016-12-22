import vk
import time
import random


token = "e6caabc238b1190aabe95651188e7ad790ea94e93484dd6002a562a94c335196794073b1758d5848910b7"

print('Бот работает.')
print('By Vovidze/')

session = vk.Session(token)
#session = vk.Session("23b101f6238bb98824d0617bd9fd1d1c42dec8b4ae2314fb9c1a035c3233202fd66f7ca30a488afa2c463")
api = vk.API(session)

while (True):
    #try:
        messages = api.messages.get()
        messages = [(m['uid'], m['mid'], m['body'])
                    for m in messages[1:] if m['read_state'] == 0]

        for m in messages:
            user_id = m[0]
            messages_id = m[1]
            command = m[2]

            if str(command)=='ауе':
                api.messages.send(user_id=user_id,
                                  message='ауе братан')
                break

        ids = ', '.join([str(m[1]) for m in messages])

        if ids:
            api.messages.markAsRead(message_ids=ids)

        time.sleep(3)


