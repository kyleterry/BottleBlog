import bottleblog.bottle as bottle
import bottleblog.lib.auth as auth

@bottle.route('/login')
def login():
    session = bottle.request.environ.get('beaker.session')
    
    if 'authenticated' in session and session['authenticated'] == 1:
        if 'redirect_to' in session:
            bottle.redirect(session['redirect_to')
        bottle.redirect('/')

    
