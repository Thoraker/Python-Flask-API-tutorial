from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_todo():
    print(todos, 'todo')
    json_text = jsonify(todos)
    print(json_text, 'json')
    return(json_text)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
