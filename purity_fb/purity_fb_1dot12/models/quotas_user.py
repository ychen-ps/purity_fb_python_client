# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.12 Python SDK

    Pure Storage FlashBlade REST 1.12 Python SDK. Compatible with REST API versions 1.0 - 1.12. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.12
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class QuotasUser(object):
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
        'name': 'str',
        'file_system': 'FixedReference',
        'file_system_default_quota': 'int',
        'quota': 'int',
        'usage': 'int',
        'user': 'QuotasuserUser'
    }

    attribute_map = {
        'name': 'name',
        'file_system': 'file_system',
        'file_system_default_quota': 'file_system_default_quota',
        'quota': 'quota',
        'usage': 'usage',
        'user': 'user'
    }

    def __init__(self, name=None, file_system=None, file_system_default_quota=None, quota=None, usage=None, user=None):  # noqa: E501
        """QuotasUser - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._file_system = None
        self._file_system_default_quota = None
        self._quota = None
        self._usage = None
        self._user = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if file_system is not None:
            self.file_system = file_system
        if file_system_default_quota is not None:
            self.file_system_default_quota = file_system_default_quota
        if quota is not None:
            self.quota = quota
        if usage is not None:
            self.usage = usage
        if user is not None:
            self.user = user

    @property
    def name(self):
        """Gets the name of this QuotasUser.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this QuotasUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuotasUser.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this QuotasUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_system(self):
        """Gets the file_system of this QuotasUser.  # noqa: E501


        :return: The file_system of this QuotasUser.  # noqa: E501
        :rtype: FixedReference
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this QuotasUser.


        :param file_system: The file_system of this QuotasUser.  # noqa: E501
        :type: FixedReference
        """

        self._file_system = file_system

    @property
    def file_system_default_quota(self):
        """Gets the file_system_default_quota of this QuotasUser.  # noqa: E501

        File system's default user quota (in bytes). If it is 0, it means there is no default quota. This will be the effective user quota if the user doesn't have an individual quota. This default quota is set through the file-system endpoint.  # noqa: E501

        :return: The file_system_default_quota of this QuotasUser.  # noqa: E501
        :rtype: int
        """
        return self._file_system_default_quota

    @file_system_default_quota.setter
    def file_system_default_quota(self, file_system_default_quota):
        """Sets the file_system_default_quota of this QuotasUser.

        File system's default user quota (in bytes). If it is 0, it means there is no default quota. This will be the effective user quota if the user doesn't have an individual quota. This default quota is set through the file-system endpoint.  # noqa: E501

        :param file_system_default_quota: The file_system_default_quota of this QuotasUser.  # noqa: E501
        :type: int
        """

        self._file_system_default_quota = file_system_default_quota

    @property
    def quota(self):
        """Gets the quota of this QuotasUser.  # noqa: E501

        The limit of the quota (in bytes) for the specified user, cannot be 0. Modifiable. If specified, this value will override the file system's default user quota.  # noqa: E501

        :return: The quota of this QuotasUser.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotasUser.

        The limit of the quota (in bytes) for the specified user, cannot be 0. Modifiable. If specified, this value will override the file system's default user quota.  # noqa: E501

        :param quota: The quota of this QuotasUser.  # noqa: E501
        :type: int
        """

        self._quota = quota

    @property
    def usage(self):
        """Gets the usage of this QuotasUser.  # noqa: E501

        The usage of the file system (in bytes) by the specified user.  # noqa: E501

        :return: The usage of this QuotasUser.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this QuotasUser.

        The usage of the file system (in bytes) by the specified user.  # noqa: E501

        :param usage: The usage of this QuotasUser.  # noqa: E501
        :type: int
        """

        self._usage = usage

    @property
    def user(self):
        """Gets the user of this QuotasUser.  # noqa: E501


        :return: The user of this QuotasUser.  # noqa: E501
        :rtype: QuotasuserUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this QuotasUser.


        :param user: The user of this QuotasUser.  # noqa: E501
        :type: QuotasuserUser
        """

        self._user = user

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
        if issubclass(QuotasUser, dict):
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
        if not isinstance(other, QuotasUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
