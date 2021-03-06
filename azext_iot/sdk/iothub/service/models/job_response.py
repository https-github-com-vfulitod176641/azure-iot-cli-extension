# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobResponse(Model):
    """JobResponse.

    :param job_id: System generated.  Ignored at creation.
    :type job_id: str
    :param query_condition: Device query condition.
    :type query_condition: str
    :param created_time: System generated.  Ignored at creation.
    :type created_time: datetime
    :param start_time: Scheduled job start time in UTC.
    :type start_time: datetime
    :param end_time: System generated.  Ignored at creation.
     Represents the time the job stopped processing.
    :type end_time: datetime
    :param max_execution_time_in_seconds: Max execution time in secounds (ttl
     duration)
    :type max_execution_time_in_seconds: long
    :param type: Required.
     The type of job to execute. Possible values include: 'unknown', 'export',
     'import', 'backup', 'readDeviceProperties', 'writeDeviceProperties',
     'updateDeviceConfiguration', 'rebootDevice', 'factoryResetDevice',
     'firmwareUpdate', 'scheduleDeviceMethod', 'scheduleUpdateTwin',
     'restoreFromBackup', 'failoverDataCopy'
    :type type: str or ~service.models.enum
    :param cloud_to_device_method: Required if jobType is cloudToDeviceMethod.
     The method type and parameters.
    :type cloud_to_device_method: ~service.models.CloudToDeviceMethod
    :param update_twin:
    :type update_twin: ~service.models.Twin
    :param status: System generated.  Ignored at creation. Possible values
     include: 'unknown', 'enqueued', 'running', 'completed', 'failed',
     'cancelled', 'scheduled', 'queued'
    :type status: str or ~service.models.enum
    :param failure_reason: System generated.  Ignored at creation.
     If status == failure, this represents a string containing the reason.
    :type failure_reason: str
    :param status_message: Status message for the job
    :type status_message: str
    :param device_job_statistics: Job details
    :type device_job_statistics: ~service.models.DeviceJobStatistics
    """

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'query_condition': {'key': 'queryCondition', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'max_execution_time_in_seconds': {'key': 'maxExecutionTimeInSeconds', 'type': 'long'},
        'type': {'key': 'type', 'type': 'str'},
        'cloud_to_device_method': {'key': 'cloudToDeviceMethod', 'type': 'CloudToDeviceMethod'},
        'update_twin': {'key': 'updateTwin', 'type': 'Twin'},
        'status': {'key': 'status', 'type': 'str'},
        'failure_reason': {'key': 'failureReason', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'device_job_statistics': {'key': 'deviceJobStatistics', 'type': 'DeviceJobStatistics'},
    }

    def __init__(self, **kwargs):
        super(JobResponse, self).__init__(**kwargs)
        self.job_id = kwargs.get('job_id', None)
        self.query_condition = kwargs.get('query_condition', None)
        self.created_time = kwargs.get('created_time', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.max_execution_time_in_seconds = kwargs.get('max_execution_time_in_seconds', None)
        self.type = kwargs.get('type', None)
        self.cloud_to_device_method = kwargs.get('cloud_to_device_method', None)
        self.update_twin = kwargs.get('update_twin', None)
        self.status = kwargs.get('status', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.status_message = kwargs.get('status_message', None)
        self.device_job_statistics = kwargs.get('device_job_statistics', None)
