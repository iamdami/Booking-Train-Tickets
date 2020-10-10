import telegram

my_token = 'put your token' #put your token
bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()
print(updates)
for i in updates:
    print(i)
print('start telegram chat bot')
