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


class Permission(object):
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
        'action': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'resource_type': 'resource_type'
    }

    def __init__(self, action=None, resource_type=None):  # noqa: E501
        """Permission - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._resource_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def action(self):
        """Gets the action of this Permission.  # noqa: E501

        The `action` that the user can perform on the `resource_type`. Typical values include `get`, `patch`, `post`, and `delete`. Values can also be finer grained.  # noqa: E501

        :return: The action of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Permission.

        The `action` that the user can perform on the `resource_type`. Typical values include `get`, `patch`, `post`, and `delete`. Values can also be finer grained.  # noqa: E501

        :param action: The action of this Permission.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def resource_type(self):
        """Gets the resource_type of this Permission.  # noqa: E501

        The `resource_type` that this `permission` affects.  # noqa: E501

        :return: The resource_type of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Permission.

        The `resource_type` that this `permission` affects.  # noqa: E501

        :param resource_type: The resource_type of this Permission.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

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
        if issubclass(Permission, dict):
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
        if not isinstance(other, Permission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
