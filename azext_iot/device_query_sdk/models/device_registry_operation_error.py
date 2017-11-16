# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceRegistryOperationError(Model):
    """Encapsulated device identity operation error details.

    :param device_id:
    :type device_id: str
    :param error_code: Possible values include: 'InvalidErrorCode',
     'InvalidProtocolVersion', 'DeviceInvalidResultCount', 'InvalidOperation',
     'ArgumentInvalid', 'ArgumentNull', 'IotHubFormatError',
     'DeviceStorageEntitySerializationError', 'BlobContainerValidationError',
     'ImportWarningExistsError', 'InvalidSchemaVersion',
     'DeviceDefinedMultipleTimes', 'DeserializationError',
     'BulkRegistryOperationFailure', 'DefaultStorageEndpointNotConfigured',
     'InvalidFileUploadCorrelationId', 'ExpiredFileUploadCorrelationId',
     'InvalidStorageEndpoint', 'InvalidMessagingEndpoint',
     'InvalidFileUploadCompletionStatus', 'InvalidStorageEndpointOrBlob',
     'RequestCanceled', 'InvalidStorageEndpointProperty',
     'InvalidRouteTestInput', 'InvalidSourceOnRoute', 'IotHubNotFound',
     'IotHubUnauthorizedAccess', 'IotHubUnauthorized', 'IotHubSuspended',
     'IotHubQuotaExceeded', 'JobQuotaExceeded',
     'DeviceMaximumQueueDepthExceeded', 'IotHubMaxCbsTokenExceeded',
     'DeviceMaximumActiveFileUploadLimitExceeded',
     'DeviceMaximumQueueSizeExceeded', 'DeviceModelMaxPropertiesExceeded',
     'DeviceModelMaxIndexablePropertiesExceeded', 'DeviceNotFound',
     'JobNotFound', 'PartitionNotFound', 'QuotaMetricNotFound',
     'SystemPropertyNotFound', 'AmqpAddressNotFound',
     'QueryStoreClusterNotFound', 'DeviceNotOnline',
     'OperationNotAllowedInCurrentState', 'ImportDevicesNotSupported',
     'BulkAddDevicesNotSupported', 'DeviceAlreadyExists',
     'LinkCreationConflict', 'ModelAlreadyExists', 'DeviceLocked',
     'DeviceJobAlreadyExists', 'PreconditionFailed', 'DeviceMessageLockLost',
     'JobRunPreconditionFailed', 'MessageTooLarge', 'TooManyDevices',
     'IncompatibleDataType', 'ThrottlingException',
     'ThrottleBacklogLimitExceeded', 'ThrottlingBacklogTimeout',
     'ThrottlingMaxActiveJobCountExceeded', 'ServerError', 'JobCancelled',
     'StatisticsRetrievalError', 'ConnectionForcefullyClosed',
     'InvalidBlobState', 'BackupTimedOut', 'AzureStorageTimeout',
     'GenericTimeout', 'InvalidThrottleParameter', 'EventHubLinkAlreadyClosed',
     'ReliableBlobStoreError', 'RetryAttemptsExhausted',
     'UnexpectedPropertyValue', 'OrchestrationOperationFailed',
     'InvalidResponseWhileProxying', 'ServiceUnavailable', 'IotHubFailingOver',
     'ConnectionUnavailable', 'DeviceUnavailable', 'GatewayTimeout'
    :type error_code: str or :class:`ErrorCode <device_api.models.ErrorCode>`
    :param error_status:
    :type error_status: str
    """

    _validation = {
        'device_id': {'required': True},
        'error_code': {'required': True},
        'error_status': {'required': True},
    }

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_status': {'key': 'errorStatus', 'type': 'str'},
    }

    def __init__(self, device_id, error_code, error_status):
        self.device_id = device_id
        self.error_code = error_code
        self.error_status = error_status
