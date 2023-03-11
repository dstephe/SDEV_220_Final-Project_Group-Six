from bell import bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train(
    [
   "I need help",
   "How can I help?"
    ]
)

trainer.train([
    "I can't login",
    "What is the exact problem",
    "It says it has an error",
    "'Username or Password is incorrect' it what is says",
    "Did you make sure the username and password were correct",
    "yes I made sure they were correct",
    "Have you tried reseting your password?",
    "That's why i'm here",
    "Ok, no issue. I sent you an email verfication",
    "Thanks, that worked",
    "No problem. I'm glad that worked for you"
])

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break