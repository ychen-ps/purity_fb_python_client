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


class ArrayConnectionKey(object):
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
        'connection_key': 'str',
        'created': 'int',
        'expires': 'int'
    }

    attribute_map = {
        'connection_key': 'connection_key',
        'created': 'created',
        'expires': 'expires'
    }

    def __init__(self, connection_key=None, created=None, expires=None):  # noqa: E501
        """ArrayConnectionKey - a model defined in Swagger"""  # noqa: E501

        self._connection_key = None
        self._created = None
        self._expires = None
        self.discriminator = None

        if connection_key is not None:
            self.connection_key = connection_key
        if created is not None:
            self.created = created
        if expires is not None:
            self.expires = expires

    @property
    def connection_key(self):
        """Gets the connection_key of this ArrayConnectionKey.  # noqa: E501

        Connection-key, used on another array to connect to this array. After creation, listing will only show ****.  # noqa: E501

        :return: The connection_key of this ArrayConnectionKey.  # noqa: E501
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """Sets the connection_key of this ArrayConnectionKey.

        Connection-key, used on another array to connect to this array. After creation, listing will only show ****.  # noqa: E501

        :param connection_key: The connection_key of this ArrayConnectionKey.  # noqa: E501
        :type: str
        """

        self._connection_key = connection_key

    @property
    def created(self):
        """Gets the created of this ArrayConnectionKey.  # noqa: E501

        Creation time in milliseconds since UNIX epoch.  # noqa: E501

        :return: The created of this ArrayConnectionKey.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ArrayConnectionKey.

        Creation time in milliseconds since UNIX epoch.  # noqa: E501

        :param created: The created of this ArrayConnectionKey.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def expires(self):
        """Gets the expires of this ArrayConnectionKey.  # noqa: E501

        Expiration time in milliseconds since UNIX epoch.  # noqa: E501

        :return: The expires of this ArrayConnectionKey.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this ArrayConnectionKey.

        Expiration time in milliseconds since UNIX epoch.  # noqa: E501

        :param expires: The expires of this ArrayConnectionKey.  # noqa: E501
        :type: int
        """

        self._expires = expires

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
        if issubclass(ArrayConnectionKey, dict):
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
        if not isinstance(other, ArrayConnectionKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
