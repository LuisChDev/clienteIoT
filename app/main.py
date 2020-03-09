from flask import Flask, request, render_template
from datetime import datetime

from .sql import insert_temp as ins_tempS
from .redis import insert_temp as ins_tempR

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_json()
        now = datetime.now()
        stamp = datetime.fromtimestamp(data["timestamp"])
        tempr = float(data["temperature"])

        # agregando a redis
        ins_tempR(tmsp=stamp, tmp=tempr, rcd=now)

        # agregando a mysql
        ins_tempS(tmsp=stamp, tmp=tempr, rcd=now)

        print(request.json)
        return render_template('success.html', tempr=tempr, stamp=stamp, now=now)


##### alternative
# def index_func():
#     pass
# app.add_url_rule('/index', view_func=index_func, methods=["GET", "POST"])
