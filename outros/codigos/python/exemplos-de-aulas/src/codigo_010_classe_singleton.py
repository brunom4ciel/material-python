class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance

    def __init__(self, wrapped_class=None, *args, **kwargs):
        if wrapped_class and not self._initialized:
            self._initialized = True
            self.wrapped_class_instance = wrapped_class(*args, **kwargs)

    def update_instance(self, *args, **kwargs):
        if hasattr(self, 'wrapped_class_instance'):
            for key, value in kwargs.items():
                setattr(self.wrapped_class_instance, key, value)

    def __getattr__(self, name):
        return getattr(self.wrapped_class_instance, name)