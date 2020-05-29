registry = {}

class MultiMethod(object):
    # Create a function
    def __init__(self, name):
        self.name = name
        self.typemap = {}
    #Make the object itself callable
    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args) # a generator expression!
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)
    #Add a new function to the type diagram
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function

#Returns a multimethod object and calls the register method
def multimethod(*types):
        def register(function):
            # add
            function = getattr(function, "__lastreg__", function)
            name = function.__name__
            mm = registry.get(name)
            if mm is None:
                mm = registry[name] = MultiMethod(name)
            mm.register(types, function)
            # add
            mm.__lastreg__ = function
            return mm

        return register
