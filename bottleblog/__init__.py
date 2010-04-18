import bottle
from paste.config import DispatchingConfig

__all__ = ['app_config', 'session', 'tmpl_globals']

app_config = {}

# this class holds the global template values
class c(object):
    pass

tmpl_globals = c()
