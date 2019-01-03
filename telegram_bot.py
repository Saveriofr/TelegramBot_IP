

import time, datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Received: %s' % command

    if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Ciao Maker"))
    elif command == '/ciao':
        telegram_bot.sendMessage (chat_id, str("Ciao Maker"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto (chat_id, photo = "https://i.pinimg.com/avatars/circuitdigest_1464122100_280.jpg")
    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/ip.txt'))
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))

telegram_bot = telepot.Bot('747459880:AAEmp5_ZGtxHzRigwbjo3L9GC_Az4h0thpo')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'

while 1:
    time.sleep(10)

