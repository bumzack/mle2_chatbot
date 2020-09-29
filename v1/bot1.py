from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Edureka')
trainer = ListTrainer(chatbot)
trainer.train(
    ["hi, can I help you find a course", "sure I'd love to find you a course", "your course have been selected",
       "how fast can i drive", "what is the speed limit"])

# getting a response from the chatbot
response = chatbot.get_response("I am looking for a course")
print(response)

response1 = chatbot.get_response("Am i too fast?")
print(response1)


#
# # creating a new chatbot
# chatbot = ChatBot('Ron Obvious')
#
# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)
#
# # Train the chatbot based on the english corpus
# # trainer.train("chatterbot.corpus.english")
#
# # Get a response to an input statement
# # chatbot.get_response("Hello, how are you today?")
#
# trainer.train(
#     ["hi, can I help you find a course", "sure I'd love to find you a course", "your course have been selected"])
#
# # getting a response from the chatbot
# response = chatbot.get_response("I want a course")
# print(response)
