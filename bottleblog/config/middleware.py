from bottleblog.bottle import default_app
from beaker.middleware import SessionMiddleware
from simpleacl.middleware import AclMiddleware
import bottleblog

def make_app():
    app = default_app()

    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './bottleblog/data',
        'session.auto': True
    }
    app = SessionMiddleware(app, session_opts)
    app = AclMiddleware(app, bottleblog.app_config)

    return app
