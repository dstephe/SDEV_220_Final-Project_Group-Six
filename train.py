from bell import bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train(
    [
   "I forgot my password",
   "Sorry about that"
    ]
)

trainer.train([
    "I can't login",
    "What is the exact problem",
    "It says it has an error",
    "What the error say?",
    "I don't get it",
    "Read it to me",
    "'Username or Password is incorrect' it what is says",
    "Did you make sure the username and password were correct",
    "yes",
    "Have you tried reseting your password?",
    "That's why i'm here",
    "Ok, no issue. I sent you an email verfication"
])

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break