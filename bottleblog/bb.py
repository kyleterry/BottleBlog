from bottleblog import bottle
import bottleblog

#controllers
from controllers.index import index

from config.middleware import make_app

def app_factory(global_config, **local_conf):
    app = make_app()
    bottleblog.app_config = global_config
    return app
