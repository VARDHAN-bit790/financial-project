from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get("query", "").strip()
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
