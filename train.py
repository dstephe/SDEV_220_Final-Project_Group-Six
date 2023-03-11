from bell import bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train(
    [
    "Hello",
    "Please hold"
    ]
)

trainer.train([
    "Hi there!",
    "Hello",
    "What kind of phone plans do you offer?",
    "We have our 'basic' plan,'Plus' plan, 'Old People' plan, and 'Deluxe' plan. ",
    "Tell me about old people",
    "The 'Old People' plan has unlimited calls with throttled data and a free rotary phone app.",
    "How much does it cost?"
    "How many phones are you wanting to add to this plan?",
    "five",
    "This plan costs $77/month for five phones.",
    "That sounds expensive"
    "Well, we offer a $5/month discount for new and joining members",
    "Ok I want this plan",
    "Alright, I'll send you to billing"
])

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break