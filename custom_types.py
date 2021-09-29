class ContainerDict(dict):
    def __init__(self, instances=None):
        self.instances = instances
    
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value