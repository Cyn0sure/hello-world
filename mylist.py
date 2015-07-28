class MyClass(object):
    def __unicode__(self):
        return tenants

    tenant={'name':'zx','id':'ed45'}

instance_list = [MyClass().tenant for i in range(10)]

print dir(instance_list[1])
