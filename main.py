# -*- encoding: utf-8 -*-

import sys
from os.path import dirname
from os.path import realpath

sys.path.append(dirname(dirname(dirname(dirname(realpath(__file__))))))
import doubanbook.script
import qiubai.script


def crawl_douban():
    print "Start do crawl douban book"
    doubanbook.script.thread_douban()


def crawl_qiubai():
    print "Start do crawl qiubai hot text"
    qiubai.script.thread_qiubai()


def doHint():
    print "Usage: python main.py [douban|qiubai]"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        req = sys.argv[1]
        operator = {
            'douban': crawl_douban,
            'qiubai': crawl_qiubai
        }
        operator.get(req, doHint)()
    else:
        print "Usage: python main.py [douban|qiubai]"
