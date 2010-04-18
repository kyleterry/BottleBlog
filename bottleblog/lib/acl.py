import simpleacl

class BuildAcl(object):
    def __init__(self):
        pass

    def __call__(self):
        acl = simpleacl.Acl()
        acl.addRole('admin')
        acl.addRole('member')
        acl.addRole('guest')
        acl.addResource('view_blog')
        acl.addResource('add_blog')
        acl.addResource('edit_blog')
        acl.addResource('delete_blog')
        acl.allow('admin', 'all')
        acl.allow('member', 'view_blog')
        acl.allow('guest', 'view_blog')

        return acl
