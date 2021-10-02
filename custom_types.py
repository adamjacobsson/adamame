class AttrDict(dict):
    def __getattr__(self, attr):
        item = self[attr]['callable']
        instance_type = self[attr]['instance_type']
        return item if instance_type == 'singleton' else item()
