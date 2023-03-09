from chatterbot import ChatBot

bot = ChatBot(
    'Bell',#chatbot name
    storage_adaptor='chatterbot.storage.SQLStorageAdapter',#what database system we are using
    
    #how it determines what to reponse with
    logic_adaptors=[ 
        'chatterbot.logic.SpecificResponseAdapter',#repsonses to specifc questiosn with specfic answers
        'chatterbot.logic.MathematicalEvaluation',#responses to math questions
        'chatterbot.logic.BestMatch'#matches the input with the best output
    ],
    database_url='sqlite:///database.sqlite3'#location of database
)