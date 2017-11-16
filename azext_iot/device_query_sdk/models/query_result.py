# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryResult(Model):
    """Results produced from a query. It contains the type of result, a list of
    result items, and a continuation token if appropriate.

    :param type: Possible values include: 'unknown', 'twin', 'deviceJob',
     'jobResponse', 'raw'
    :type type: str or :class:`QueryResultType
     <device_api.models.QueryResultType>`
    :param items:
    :type items: list of object
    :param continuation_token:
    :type continuation_token: str
    """

    _validation = {
        'type': {'required': True},
        'items': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'items': {'key': 'items', 'type': '[object]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(self, type, items, continuation_token=None):
        self.type = type
        self.items = items
        self.continuation_token = continuation_token
