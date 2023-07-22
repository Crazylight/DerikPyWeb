import os

from OpenAI import aichat
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


@app.route("/sayhello")
def hello_world():
    return "Derik say Hello to You."



@app.route('/tochat')
def tochat():
   print("request for chatpage.")
   return render_template('chatpage.html')

@app.route("/chat", methods=['POST'])
def chat():
    question = request.form.get('question')
    if question:

        print(question)

        charter = aichat.charter()
        answer = charter.chat(question)
        print(answer)
        return render_template('chatpage.html', answer=answer)
    else:
        print("There is no quest.")
        return render_template('chatpage.html', answer="There is no question. Please input a question")


if __name__ == '__main__':
    app.run()