from flask import Flask, render_template, request
from chatgpt import GPT

app = Flask(__name__)
  # initialize GPT with a unique ID

@app.route("/")
def home():
    return render_template("index.html")

# Define route for home page
@app.route("/get", methods=["GET", "POST"])
def get_response():
    chat_model = GPT(str(request.values.get("WaId", "")))
    
    
    userText = request.args.get('msg')
    return str(chat_model.bot(userText))

if __name__ == "__main__":
    app.run(debug=True)

