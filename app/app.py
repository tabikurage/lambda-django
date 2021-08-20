import importlib
import os

def application(env, start_response):
    f = open('/mnt/efs/test.txt', 'w')
    f.close()
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    return [b'Hello World']