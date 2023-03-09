from bell import bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    "Hi there!",
    "Hello",
])