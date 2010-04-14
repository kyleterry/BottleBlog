from bottleblog.model import *

init_model()

def create_db():
    meta.metadata.bind = meta.engine
    meta.metadata.create_all(checkfirst=True)

if __name__=='__main__':
    create_db()
