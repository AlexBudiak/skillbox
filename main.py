# словарь, объект, хэш-таблица

from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

def add_message(text, sender): # объявим функцию которая добавит сообщение в список
    new_message = {
        'text': text,
        'sender': sender,
        'time': '23:59', # toDO: указать правильное время или дату
    }
    messages.append(new_message) # добавляем новое сообщение в список

def print_message(message): # объявляем функцию которая будет печатать одно сообщение
    print(f" [{message['sender']}]: {message['text']} / {message['time']} ")


# главная страница
@app.route("/")
def index_page():
    return 'Здравствуйте! Вас приветствует проект мессенжера v.0'

# показать все сообщения в формате JSON
@app.route("/get_messages")
def get_messages():
    return {'messages': messages}

# Показать форму чата
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send_message")
def send_message():
    # Получить имя и текст от пользователя
    name = request.args["name"]  # Получаем имя
    text = request.args["text"] # Получаем текст
    # Вызвать функцию add_message
    add_message(text, name)
    return "OK"

app.run() # запускаем веб приложение

# ПЛАН
# 1. Создали внутреннюю возможность зранить сообщения, добавлять новые и читать чат
# 2. Подключить вицзуальный интерфейс к этим внутренним возможностям:
#       Превратить наш код в работающий веб-сервер. Flask
#       Создать интерфейс и подключить его к веб-серверу