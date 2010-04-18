import bottleblog.bottle as bottle
from bottleblog.lib.auth import authenticate

#@authenticate
@bottle.route('/admin/write')
def index():
    return 'index'

@bottle.route('/admin/write/post')
def post():
    return 'post'

@bottle.route('/admin/write/page')
def page():
    return 'page'
