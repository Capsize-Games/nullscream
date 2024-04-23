import types
import sys
import importlib.machinery
from importlib import abc

from nullscream.noop_class import NoopClass


class NoopLoader(abc.Loader):
    """
    Loader that creates noop stand-in modules.
    """
    def create_module(self, spec):
        return types.ModuleType(spec.name)

    def exec_module(self, module):
        module.__dict__.update({
            "__all__": [],  # Empty export list
            "__doc__": "This is a noop stand-in module.",
            "__getattr__": NoopClass(),
            "__setattr__": NoopClass(),
            "__delattr__": NoopClass(),
            "__dir__": NoopClass(),
        })

class NoopFinder(importlib.abc.MetaPathFinder):
    def __init__(self, blacklist=None, whitelist=None):
        self.blacklist = blacklist or []
        self.whitelist = whitelist or []

    def find_spec(self, fullname, path, target=None):
        root = fullname.split('.')[0]

        if (
            (
                fullname in self.blacklist and fullname not in self.whitelist
            )
        ):
            return importlib.machinery.ModuleSpec(fullname, NoopLoader())
        return None


def install_nullscream(blacklist=None, whitelist=None):
    sys.meta_path.insert(0, NoopFinder(blacklist, whitelist))


def uninstall_nullscream(blacklist=None):
    sys.meta_path = [finder for finder in sys.meta_path if not isinstance(finder, NoopFinder)]
    if blacklist:
        for module_name in blacklist:
            try:
                sys.modules.pop(module_name, None)
            except KeyError:
                pass
