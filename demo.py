#!/usr/bin/python

import sys
from flask import Flask, request
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
    logger.info("Called hello")
    return "Hello"


@app.route("/hello")
def sayHello():
    name = request.args.get("name")
    return "Hello {}".format(name)

def main(args):
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=5001, debug=True)


if __name__=='__main__':
    main(sys.argv)

