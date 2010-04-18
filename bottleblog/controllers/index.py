from bottleblog.bottle import route, request, response, abort
from bottleblog.bottle import mako_view as view
import bottleblog
from bottleblog import tmpl_globals as c
import bottleblog.model as model

@route('/')
@view('blog/index')
def index():
    acl = request.environ.get('simpleacl')
    print acl
    c.name = 'kyle'
    return dict(c=c)
