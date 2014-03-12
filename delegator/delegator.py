from exceptions import NotImplementedError, AttributeError


class Delegator(object):

    def __init__(self, obj):
        self.__setobj__(obj)

    def __setattr__(self, name, value):
        target = self.__getobj__()

        if name in self.__dict__:
            object.__setattr__(self, name, value)
        else:
            setattr(target, name, value)

    def __getattr__(self, name):
        target = self.__getobj__()

        if hasattr(target, name):
            if callable(getattr(target, name)):
                def _missing(*args, **kwargs):
                    return getattr(target, name)(*args, **kwargs)
            else:
                _missing = getattr(target, name)

            return _missing

        raise AttributeError("'{0}' object has no attribute '{1}'".format(
            self.__getobj__().__class__.__name__, name
        ))

    def __setobj__(self, obj):
        raise NotImplementedError("need to define `__setobj__'")

    def __getobj__(self):
        raise NotImplementedError("need to define `__getobj__'")

    def __eq__(self, obj):
        if obj is self:
            return True
        return self.__getobj__() == obj

    def __ne__(self, obj):
        if obj is self:
            return False
        return self.__getobj__() != obj


class SimpleDelegator(Delegator):

    def __getobj__(self):
        return self.__dict__['delegate_sd_obj']

    def __setobj__(self, obj):
        if self is obj:
            raise AttributeError("cannot delegate to self")
        self.__dict__['delegate_sd_obj'] = obj
