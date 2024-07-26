import openai
class Chatbot:
    def __init__(self):
        openai.api_key = "sk-None-KaQ1HurkojbYe7LIPS71T3BlbkFJwnAAEXPQG7fibwZePmoB"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "gpt-3.5-turbo-instruct",
            prompt = user_input,
            max_tokens = 3400,
            temperature = 0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)