from decorator import decorator
import bottleblog.model as model
import bottleblog.bottle as bottle

def authenticate():
    """Attempts to authenticate a request by checking if
    there is a logged in session.
    """
    session = bottle.request.environ.get('beaker.session')

