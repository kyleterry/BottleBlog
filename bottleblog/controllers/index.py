from bottleblog.bottle import route, request, response, abort
from bottleblog import config

@route('/')
def index():
    print config
    return '/ index'
