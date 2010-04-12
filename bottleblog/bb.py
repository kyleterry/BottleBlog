from bottleblog import bottle, config
import bottleblog

#controllers
from controllers.index import index

from config.middleware import make_app

def app_factory(global_config, **local_conf):
    app = make_app()
    print global_config
    bottleblog.config = global_config
    bottleblog.session = bottle.request.environ.get('beaker.session')
    return app
