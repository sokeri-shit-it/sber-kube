import html
import sys
from subprocess import Popen, PIPE, STDOUT, DEVNULL
from textwrap import dedent

from flask import Flask, Response, render_template # $ pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    def g():
        yield "<!doctype html><title>Stream subprocess output</title>"

        with Popen(['python', 'main.py'], stdin=DEVNULL, stdout=PIPE, stderr=STDOUT,
                   bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                yield "<code>{}</code>".format(html.escape(line.rstrip("\n")))

                yield "<br>\n"
    return Response(g(), mimetype='text/html')
    
    


if __name__ == "__main__":
    app.run(host='localhost', port=23423, debug=True) # run the server
