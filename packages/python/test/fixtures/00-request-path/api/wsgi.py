from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response(request.full_path, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=False, port=8002)
