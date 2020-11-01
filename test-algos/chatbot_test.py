from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from flask import Flask, render_template, request
import spacy

spacy.load('en')
# --------------------------------------
# Instantiate agent
# BestMatch = selects response by best known match to statement
# response_selection_method has 3 options:
# get_first_response,get_most_frequent_response or get_random_response
bot = ChatBot('chatbot_test',
              read_only=False,
              response_selection_method=get_random_response,
              logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'}],
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database='test1.sqlite3')

# --------------------------------------
# List Trainer
talk = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
        'Você gosta de programar?', 'Sim, eu programo em Python']

list_trainer = ListTrainer(bot)
# NOT WORKING - AttributeError: 'ChatBot' object has no attribute 'train'
# bot.train(talk)

# --------------------------------------
# Corpus Trainer
corpus_trainer = ChatterBotCorpusTrainer(bot)

# corpus_trainer.train('data/greetings.yml')


corpus_trainer.train('data/botprofile.yml', 'data/compliment.yml', 'data/computers.yml', 'data/context_free_br.yml',
                     'data/conversations.yml', 'data/emotion.yml', 'data/food.yml', 'data/games.yml',
                     'data/gossip.yml', 'data/greetings.yml', 'data/health.yml', 'data/history.yml',
                     'data/linguistic_knowledge.yml', 'data/literature.yml', 'data/money.yml', 'data/movies.yml',
                     'data/politics.yml', 'data/proverbs.yml', 'data/psychology.yml', 'data/science.yml',
                     'data/sports.yml', 'data/suggestions.yml', 'data/trivia.yml', 'data/unilab.yml')


# --------------------------------------
# Conversation Loop
def conversation():
    while True:
        try:
            question = input('Usuário: ')
            answer = bot.get_response(question)
            if answer.confidence > 0.5:
                print('chatbot_test: ', answer)
                print('confidence', answer.confidence)
            else:
                print('chatbot_test: ', 'Ainda não sei responder essa frase')
                print('confidence', answer.confidence)
        # CONTROL+D to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


# --------------------------------------
# GUI + website

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(bot.get_response(usertext))


if __name__ == "__main__":
    app.run()
