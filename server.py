# -*- encoding: utf-8 -*-

import sys
from os.path import dirname
from os.path import realpath

from flask import Flask

import doubanbook.script
import qiubai.script

app = Flask(__name__)
sys.path.append(dirname(dirname(dirname(dirname(realpath(__file__))))))


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/douban')
def crawl_douban():
    doubanbook.script.thread_douban()
    return 'success'


@app.route('/qiubai')
def crawl_qiubai():
    qiubai.script.thread_qiubai()
    return 'success'


if __name__ == '__main__':
    app.run()
