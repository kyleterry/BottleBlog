import sqlalchemy as sa
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

import bottleblog

__all__ = ['Session', 'metadata', 'engine']

config = bottleblog.app_config
#engine_string = config['sqlalchemy_connect']
engine_string = 'sqlite:///bottleblog.db'
if engine_string is None:
    raise Exception('`engine_string` cannot be blank')

engine = sa.create_engine(engine_string)
Session = scoped_session(sessionmaker())
metadata = MetaData()
