# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.11 Python SDK

    Pure Storage FlashBlade REST 1.11 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.11
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RelationshipPerformanceReplication(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

#BEGIN_CUSTOM
    # IR-51527: Prevent Pytest from attempting to collect this class based on name.
    __test__ = False
#END_CUSTOM

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'async': 'ReplicationPerformance',
        'remote': 'FixedReferenceNoResourceType',
        'time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'async': 'async',
        'remote': 'remote',
        'time': 'time'
    }

    def __init__(self, id=None, async=None, remote=None, time=None):  # noqa: E501
        """RelationshipPerformanceReplication - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._async = None
        self._remote = None
        self._time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if async is not None:
            self.async = async
        if remote is not None:
            self.remote = remote
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this RelationshipPerformanceReplication.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this RelationshipPerformanceReplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationshipPerformanceReplication.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this RelationshipPerformanceReplication.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def async(self):
        """Gets the async of this RelationshipPerformanceReplication.  # noqa: E501

        Total bytes transmitted or received per second for asynchronous replication.  # noqa: E501

        :return: The async of this RelationshipPerformanceReplication.  # noqa: E501
        :rtype: ReplicationPerformance
        """
        return self._async

    @async.setter
    def async(self, async):
        """Sets the async of this RelationshipPerformanceReplication.

        Total bytes transmitted or received per second for asynchronous replication.  # noqa: E501

        :param async: The async of this RelationshipPerformanceReplication.  # noqa: E501
        :type: ReplicationPerformance
        """

        self._async = async

    @property
    def remote(self):
        """Gets the remote of this RelationshipPerformanceReplication.  # noqa: E501

        Reference to a remote array.  # noqa: E501

        :return: The remote of this RelationshipPerformanceReplication.  # noqa: E501
        :rtype: FixedReferenceNoResourceType
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this RelationshipPerformanceReplication.

        Reference to a remote array.  # noqa: E501

        :param remote: The remote of this RelationshipPerformanceReplication.  # noqa: E501
        :type: FixedReferenceNoResourceType
        """

        self._remote = remote

    @property
    def time(self):
        """Gets the time of this RelationshipPerformanceReplication.  # noqa: E501

        Sample time in milliseconds since UNIX epoch.  # noqa: E501

        :return: The time of this RelationshipPerformanceReplication.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RelationshipPerformanceReplication.

        Sample time in milliseconds since UNIX epoch.  # noqa: E501

        :param time: The time of this RelationshipPerformanceReplication.  # noqa: E501
        :type: int
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RelationshipPerformanceReplication, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationshipPerformanceReplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
