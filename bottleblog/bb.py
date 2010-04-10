import bottle
from bottle import route

@route('/')
def index():
    return 'hello, world'

bottle.run(server=bottle.PasteServer)
