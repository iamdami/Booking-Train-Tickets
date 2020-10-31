# Rock, paper, scissors game using API function 'getUpdates()'

# import required modules
import sys
import time
import telepot


# function definition
def Determine(bot, unread):
    n = len(unread)

    for i in range(n):
        msg = unread[i]['message']
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id, msg['text'])
        if (msg['text'] == '가위'): # scissor
            bot.sendMessage(chat_id, '보') # paper

        if (msg['text'] == '바위'): # rock
            bot.sendMessage(chat_id, '가위') #scissor

        if (msg['text'] == '보'): # paper
            bot.sendMessage(chat_id, '바위') # rock


# get token
TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)

print('Listening(game)...')
update_id = 0
while 1:
    # Prevent multiple messages from accumulating
    unread = bot.getUpdates(offset=update_id + 1)
    if unread:
        update_id = unread[len(unread) - 1]['update_id']
    else:
        update_id = 0

    if unread:
        # Function execution
        Determine(bot, unread)

    # Action after the specified time
    time.sleep(0.5)
