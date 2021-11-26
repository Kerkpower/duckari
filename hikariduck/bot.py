from typing import Union, AnyStr
import hikari
import warning

class NoPrefixSpecified(object):
    def __init__(self): pass

class Bot(object):
    def __init__(self, prefix:Union[None, AnyStr]=NoPrefixSpecified()):
        self.prefix = prefix
    def run(self, token:AnyStr, verbose=False):
        if verbose: print("Checking if bot has a prefix.")
        if type(self.prefix) == NoPrefixSpecified:
            warnings.warn("Bot has no prefix. To prevent this warning, set prefix to None.")
