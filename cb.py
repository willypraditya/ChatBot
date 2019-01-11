from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = open('res.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)

while True:
    request = input('Question: ')
    response = bot.get_response(request)

    print('Answer: ', response)