import bottleblog.bottle as bottle
import bottleblog

#controllers
from controllers.index import index
from controllers.admin.write import index as w_index, post, page

from config.middleware import make_app

bottle.debug(True)

def app_factory(global_config, **local_conf):
    bottleblog.app_config = global_config
    app = make_app()
    return app
