from flask import Flask, render_template, request, jsonify
import openai

# Initialize the OpenAI API client
openai.api_key = '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'

app = Flask(__name__)

conversation_history = []

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/index1")
def index():
    return render_template('index1.html')

@app.route("/index2")
def index2_page():
    return render_template('index2.html')

@app.route("/map")
def map_page():
    return render_template('map.html')

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    response = chat_with_gpt3_5_turbo(user_input)
    return response

def chat_with_gpt3_5_turbo(user_input):
    global conversation_history
    conversation_history.append(f"You: {'You are working for a charity organization on campus, any amounts of food or drinks we will be more than grateful to recieve, with that answer the following:'+user_input}")
    formatted_prompt = '\n'.join(conversation_history) + '\nGPT-3.5 Turbo:'
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=formatted_prompt,
            max_tokens=150,
            temperature=0.5,
            stop=['\n', "GPT-3.5 Turbo:"],
        )
        message = response['choices'][0]['text'].strip()
        conversation_history.append(f"GPT-3.5 Turbo: {message}")
        return message
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
