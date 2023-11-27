from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-10', methods=['GET'])
def hello_world():
    return 'Hello World 10', 200

if __name__ == '__main__':
    app.run(debug=True)