from bottleblog.bottle import route, request, response, abort
import bottleblog

@route('/')
def index():
    print bottleblog.app_config
    return '/ index'
