from pathlib import Path
from importlib import import_module

class DSHandler_Factory():
    def build(self, desc):
        """Returns a datasource handler ready to handle `desc`."""

        """`desc` is a dictionary drawn from the data-sources section of 
            furnace.project.yaml."""
        
        #TODO: Error handling.
        handler_type = desc['type']
        mod = import_module('.' + handler_type + '_dshandler', 'tools.datasource_handlers')
        clsname = handler_type.title() + "_DSHandler"
        handler = getattr(mod, clsname)
        return handler(desc)