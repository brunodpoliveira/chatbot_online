from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from flask import Flask, render_template, request
import spacy

spacy.load('pt_core_news_sm')
# --------------------------------------
# Instantiate agent
# BestMatch = selects response by best known match to statement
# response_selection_method has 3 options:
# get_first_response,get_most_frequent_response or get_random_response
# statement_comparison_function has 4 options:
# read options and explanations here: https://chatterbot.readthedocs.io/en/stable/comparisons.html#statement-comparison
# default_response is a response in case the bot doesn't know what to say
# maximum_similarity_threshold:
# maximum amount of similarity between 2 statement required before the search process is halted(default:0.95)
bot = ChatBot('chatbot_test',
              read_only=False,
              response_selection_method=get_random_response,
              logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
                               "response_selection_method": 'chatterbot.response_selection.get_random_response',
                               "statement_comparison_function": 'chatterbot.comparisons.SynsetDistance',
                               'default_response': 'Ainda não sei responder essa frase.',
                               'maximum_similarity_threshold': 0.90
                               }],
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database='test1.sqlite3')

# --------------------------------------
# Corpus Trainer
corpus_trainer = ChatterBotCorpusTrainer(bot)

corpus_trainer.train('data/greetings.yml', 'data/bank.yml', 'data/money.yml', 'data/suggestions.yml')


# --------------------------------------
# Conversation Loop - for testing purposes only
def conversation():
    while True:
        try:
            question = input('Usuário: ')
            answer = bot.get_response(question)
            if answer.confidence > 0.5:
                print('bot: ', answer)
                print('confidence', answer.confidence)
            else:
                print('bot: ', 'Ainda não sei responder essa frase')
                print('confidence', answer.confidence)
        # CONTROL+D to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


conversation()

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

# if __name__ == "__main__":
#    app.run()
