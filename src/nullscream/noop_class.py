from nullscream.noop_function import noop


class MagicType:
    def __getattr__(self, name):
        return MagicType()

    def __call__(self, *args, **kwargs):
        return MagicType()

    def __str__(self):
        return "MagicType instance"

    def __fspath__(self):
        return ""


class NoopClass:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return MagicType()

    def __getattr__(self, name):
        return MagicType()

    def __setattr__(self, key, value):
        pass

