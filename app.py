from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Друкуємо дані, щоб переконатися, що сервер отримує їх від Facebook
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
