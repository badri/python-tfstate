# -*- coding: utf-8 -*-

# Python stdlib
import json

# tfstate
from tfstate.base.module import Module


class Tfstate(object):
    """
    Base tfstate object class
    Load tfstate file and parses it

    Usage::

        Tfstate(tfstate)
    """

    def __init__(self, tfstate: str):
        """
        :param str tfstate: tfstate contents
        """

        self.native_data = json.loads(tfstate)
        self.version = self.native_data.get('version', None)
        self.serial = self.native_data.get('serial', None)
        self.terraform_version = self.native_data.get('terraform_version', None)
        self.lineage = self.native_data.get('lineage', None)
        self.modules = Module.load_list(self.native_data.get('modules', []))

    def load_tfstate_data_from_file(self):
        """
        Read the tfstate file and load its contents, parses then as JSON and put the result into the object
        """
        pass
