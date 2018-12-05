# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource
from tfstate.exceptions import InvalidResource


class LocalFileResource(Resource):
    """
    Provides a Local File resource

    Usage::

        LocalFileResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "local_file":
            raise InvalidResource("LocalFileResource must be of 'local_file' type")
        attributes = self.primary_data['attributes']
        self.filename = attributes.get('content', None)
        self.content = attributes.get('filename', None)
