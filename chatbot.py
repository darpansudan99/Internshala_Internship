from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def create_chatbot():
    chatbot = ChatBot("SimpleBot")
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

    return chatbot

def main():
    print("Initializing Chatbot...")
    chatbot = create_chatbot()
    print("Chatbot ready. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
