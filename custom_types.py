class AttrDict(dict):
    def __getattr__(self, attr):
        item = self[attr]['callable']
        instance_type = self[attr]['instance_type']
        return item if instance_type == 'singleton' else item()
        #return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


class Singleton(dict):
    def __init__(self, instances=None):
        self.instances = instances
    
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


class Transient(dict):
    def __init__(self, instances=None):
        self.instances = instances
    
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value