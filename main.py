import os
import yaml
import subprocess
import cherrypy
import html

from flask import Flask, render_template, redirect, Response
from form.new import MainForm
from subprocess import Popen, PIPE, STDOUT, DEVNULL
from flask_script import Manager
from time import sleep

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
manager = Manager(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    form = MainForm()
    if form.validate_on_submit():
        master = int(form.master.data)
        lb = int(form.lb.data)
        router = int(form.router.data)
        service_logging = int(form.service_logging.data)
        service_monitoring = int(form.service_monitoring.data)
        worker = int(form.worker.data)
        network = str(form.network.data)
        com1 = form.com1.data
        com2 = form.com2.data
        com3 = form.com3.data
        com4 = form.com4.data
        com5 = form.com5.data
        components = []
        check = {
            'com1': com1,
            'com2': com2,
            'com3': com3,
            'com4': com4,
            'com5': com5
            }

        for keys, items in check.items():
            if items == True:
                components.append(keys)

        
        d = {
            'cluster': {
            'domain': form.domain.data,
            'components': components,
            'network': {
                'node': network
                },
                'nodes': {
                    'lb': {
                        'count': lb
                    },
                    'master': {
                        'count': master
                    },
                    'router': {
                        'count': router
                    },
                    'service_logging': {
                        'count': service_logging
                    },
                    'service_monitoring': {
                        'count': service_monitoring
                    },
                    'worker': {
                        'count': worker
                    }
                }
            },
            'vcd': {
                'network_main': form.network_main.data,
                'org': form.org.data,
                'password': form.password.data,
                'user': form.username.data,
                'vdc': form.vdc.data
                }
            }
        file = open('static/output.yaml','w')
        file.write(yaml.dump(d))
        file.close
        

        return redirect('/log')
    return render_template('index.html', form=form)

@app.route('/log', methods=('GET', 'POST'))
def log():
    def g():
        a = []
        with Popen(['python', 'slowprint.py'], stdin=DEVNULL, stdout=PIPE, stderr=STDOUT,
                   bufsize=1, universal_newlines=True) as p:
            for line in p.stdout: # Чтобы выключить нужно закоментировать след строку
                yield """<div class="container"><code">{}</code></div>""".format(html.escape(line.rstrip("\n")))
                pass
        yield """Завершенно"""
    return Response(g(), mimetype='text/html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 