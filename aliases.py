
import sys

class AliasDB:
    aliases = {}
    
    def __init__(self, filename):
        try:
            import yaml
            cfg = open(filename, 'r')
            self.aliases = yaml.safe_load(cfg)
        except Exception as err:
            sys.stderr.write('Config issue: ' + str(err) +'\n')
    
    def get(self, alias):
        if alias in self.aliases:
            return self.aliases[alias]

    def list(self):
        return list(self.aliases.keys())
        

