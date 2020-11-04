# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.10 Python SDK

    Pure Storage FlashBlade REST 1.10 Python SDK. Compatible with REST API versions 1.0 - 1.10. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.10
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PolicyPatch(object):
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
        'id': 'str',
        'enabled': 'bool',
        'rules': 'list[PolicyRule]',
        'add_rules': 'list[PolicyRule]',
        'remove_rules': 'list[PolicyRule]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'enabled': 'enabled',
        'rules': 'rules',
        'add_rules': 'add_rules',
        'remove_rules': 'remove_rules'
    }

    def __init__(self, name=None, id=None, enabled=None, rules=None, add_rules=None, remove_rules=None):  # noqa: E501
        """PolicyPatch - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._enabled = None
        self._rules = None
        self._add_rules = None
        self._remove_rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if rules is not None:
            self.rules = rules
        if add_rules is not None:
            self.add_rules = add_rules
        if remove_rules is not None:
            self.remove_rules = remove_rules

    @property
    def name(self):
        """Gets the name of this PolicyPatch.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this PolicyPatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyPatch.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this PolicyPatch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this PolicyPatch.  # noqa: E501

        A unique ID chosen by the system. Cannot change.  # noqa: E501

        :return: The id of this PolicyPatch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyPatch.

        A unique ID chosen by the system. Cannot change.  # noqa: E501

        :param id: The id of this PolicyPatch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this PolicyPatch.  # noqa: E501

        Indicates if policy is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :return: The enabled of this PolicyPatch.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PolicyPatch.

        Indicates if policy is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :param enabled: The enabled of this PolicyPatch.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def rules(self):
        """Gets the rules of this PolicyPatch.  # noqa: E501


        :return: The rules of this PolicyPatch.  # noqa: E501
        :rtype: list[PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PolicyPatch.


        :param rules: The rules of this PolicyPatch.  # noqa: E501
        :type: list[PolicyRule]
        """

        self._rules = rules

    @property
    def add_rules(self):
        """Gets the add_rules of this PolicyPatch.  # noqa: E501


        :return: The add_rules of this PolicyPatch.  # noqa: E501
        :rtype: list[PolicyRule]
        """
        return self._add_rules

    @add_rules.setter
    def add_rules(self, add_rules):
        """Sets the add_rules of this PolicyPatch.


        :param add_rules: The add_rules of this PolicyPatch.  # noqa: E501
        :type: list[PolicyRule]
        """

        self._add_rules = add_rules

    @property
    def remove_rules(self):
        """Gets the remove_rules of this PolicyPatch.  # noqa: E501


        :return: The remove_rules of this PolicyPatch.  # noqa: E501
        :rtype: list[PolicyRule]
        """
        return self._remove_rules

    @remove_rules.setter
    def remove_rules(self, remove_rules):
        """Sets the remove_rules of this PolicyPatch.


        :param remove_rules: The remove_rules of this PolicyPatch.  # noqa: E501
        :type: list[PolicyRule]
        """

        self._remove_rules = remove_rules

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
        if issubclass(PolicyPatch, dict):
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
        if not isinstance(other, PolicyPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
