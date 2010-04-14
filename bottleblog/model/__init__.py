import sqlalchemy as sa
from sqlalchemy import types
from sqlalchemy import orm
from bottleblog.model import meta
import datetime

def init_model():
    engine = meta.engine
    
    bb_post_table = sa.Table('bb_post', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('title', types.String(255)),
            sa.Column('slug', types.String(255)),
            sa.Column('body', types.Text),
            sa.Column('userId', types.Integer, sa.ForeignKey('bb_user.id')),
            sa.Column('posted', types.DateTime, onupdate=datetime.datetime.now),
            sa.Column('edited', types.DateTime))
    orm.mapper(Post, bb_post_table, \
            properties={'user':orm.relation(User), \
                        'comments':orm.relation(Comment)})

    bb_tag_table = sa.Table('bb_tag', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('name', types.String(255)),
            sa.Column('slug', types.String(255)))
    orm.mapper(Tag, bb_tag_table)

    bb_post_tag_table = sa.Table('bb_post_tag', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('postId', types.Integer, sa.ForeignKey('bb_post.id')),
            sa.Column('tagId', types.Integer, sa.ForeignKey('bb_tag.id')))

    bb_comment_table = sa.Table('bb_comment_table', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('name', types.String(60)),
            sa.Column('email', types.String(100)),
            sa.Column('url', types.String(255)),
            sa.Column('body', types.Text),
            sa.Column('postId', types.Integer, sa.ForeignKey('bb_post.id')),
            sa.Column('userId', types.Integer, sa.ForeignKey('bb_user.id')),
            sa.Column('posted', types.DateTime, onupdate=datetime.datetime.now))
    orm.mapper(Comment, bb_comment_table, \
            properties={'post':orm.relation(Post)})

    bb_user_table = sa.Table('bb_user', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('username', types.String(255)),
            sa.Column('password', types.String(64)),
            sa.Column('nickname', types.String(255)),
            sa.Column('roleId', types.Integer, sa.ForeignKey('bb_role.id')),
            sa.Column('status', types.String(30)))
    orm.mapper(User, bb_user_table, properties={'role':orm.relation(Role)})

    bb_role_table = sa.Table('bb_role', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('name', types.String(60)))
    orm.mapper(Role, bb_role_table)

    bb_resource_table = sa.Table('bb_resource', meta.metadata,
            sa.Column('id', types.Integer, primary_key=True),
            sa.Column('name', types.String(90)))
    orm.mapper(Resource, bb_resource_table)

    meta.Session.configure(bind=engine)

class Post(object):
    pass

class Tag(object):
    pass

class Comment(object):
    pass

class User(object):
    pass

class Role(object):
    pass

class Resource(object):
    pass
