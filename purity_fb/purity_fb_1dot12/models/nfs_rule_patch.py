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


class NfsRulePatch(object):
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
        'enabled': 'bool',
        'rules': 'str',
        'v3_enabled': 'bool',
        'v4_1_enabled': 'bool',
        'add_rules': 'str',
        'remove_rules': 'str',
        'after': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'rules': 'rules',
        'v3_enabled': 'v3_enabled',
        'v4_1_enabled': 'v4_1_enabled',
        'add_rules': 'add_rules',
        'remove_rules': 'remove_rules',
        'after': 'after'
    }

    def __init__(self, enabled=None, rules=None, v3_enabled=None, v4_1_enabled=None, add_rules=None, remove_rules=None, after=None):  # noqa: E501
        """NfsRulePatch - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._rules = None
        self._v3_enabled = None
        self._v4_1_enabled = None
        self._add_rules = None
        self._remove_rules = None
        self._after = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if rules is not None:
            self.rules = rules
        if v3_enabled is not None:
            self.v3_enabled = v3_enabled
        if v4_1_enabled is not None:
            self.v4_1_enabled = v4_1_enabled
        if add_rules is not None:
            self.add_rules = add_rules
        if remove_rules is not None:
            self.remove_rules = remove_rules
        if after is not None:
            self.after = after

    @property
    def enabled(self):
        """Gets the enabled of this NfsRulePatch.  # noqa: E501

        Is the NFSv3 protocol enabled? Default is false (deprecated).  # noqa: E501

        :return: The enabled of this NfsRulePatch.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NfsRulePatch.

        Is the NFSv3 protocol enabled? Default is false (deprecated).  # noqa: E501

        :param enabled: The enabled of this NfsRulePatch.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def rules(self):
        """Gets the rules of this NfsRulePatch.  # noqa: E501

        NFS rules.  # noqa: E501

        :return: The rules of this NfsRulePatch.  # noqa: E501
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this NfsRulePatch.

        NFS rules.  # noqa: E501

        :param rules: The rules of this NfsRulePatch.  # noqa: E501
        :type: str
        """

        self._rules = rules

    @property
    def v3_enabled(self):
        """Gets the v3_enabled of this NfsRulePatch.  # noqa: E501

        Is the NFSv3 protocol enabled? Default is false.  # noqa: E501

        :return: The v3_enabled of this NfsRulePatch.  # noqa: E501
        :rtype: bool
        """
        return self._v3_enabled

    @v3_enabled.setter
    def v3_enabled(self, v3_enabled):
        """Sets the v3_enabled of this NfsRulePatch.

        Is the NFSv3 protocol enabled? Default is false.  # noqa: E501

        :param v3_enabled: The v3_enabled of this NfsRulePatch.  # noqa: E501
        :type: bool
        """

        self._v3_enabled = v3_enabled

    @property
    def v4_1_enabled(self):
        """Gets the v4_1_enabled of this NfsRulePatch.  # noqa: E501

        Is the NFSv4.1 protocol enabled? Default is false.  # noqa: E501

        :return: The v4_1_enabled of this NfsRulePatch.  # noqa: E501
        :rtype: bool
        """
        return self._v4_1_enabled

    @v4_1_enabled.setter
    def v4_1_enabled(self, v4_1_enabled):
        """Sets the v4_1_enabled of this NfsRulePatch.

        Is the NFSv4.1 protocol enabled? Default is false.  # noqa: E501

        :param v4_1_enabled: The v4_1_enabled of this NfsRulePatch.  # noqa: E501
        :type: bool
        """

        self._v4_1_enabled = v4_1_enabled

    @property
    def add_rules(self):
        """Gets the add_rules of this NfsRulePatch.  # noqa: E501

        The rules which will be added to the existing NFS export rules for the file system.  # noqa: E501

        :return: The add_rules of this NfsRulePatch.  # noqa: E501
        :rtype: str
        """
        return self._add_rules

    @add_rules.setter
    def add_rules(self, add_rules):
        """Sets the add_rules of this NfsRulePatch.

        The rules which will be added to the existing NFS export rules for the file system.  # noqa: E501

        :param add_rules: The add_rules of this NfsRulePatch.  # noqa: E501
        :type: str
        """

        self._add_rules = add_rules

    @property
    def remove_rules(self):
        """Gets the remove_rules of this NfsRulePatch.  # noqa: E501

        The rules which will be removed from the existing NFS export rules for the file system. Only the first occurrence of the `remove_rules` will be removed.  # noqa: E501

        :return: The remove_rules of this NfsRulePatch.  # noqa: E501
        :rtype: str
        """
        return self._remove_rules

    @remove_rules.setter
    def remove_rules(self, remove_rules):
        """Sets the remove_rules of this NfsRulePatch.

        The rules which will be removed from the existing NFS export rules for the file system. Only the first occurrence of the `remove_rules` will be removed.  # noqa: E501

        :param remove_rules: The remove_rules of this NfsRulePatch.  # noqa: E501
        :type: str
        """

        self._remove_rules = remove_rules

    @property
    def after(self):
        """Gets the after of this NfsRulePatch.  # noqa: E501

        The `after` field can be used with `add_rules` or `remove_rules` or both. If used with `add_rules`, then the `add_rules` string will be inserted after the first occurrence of the `after` string. If used with `remove_rules`, then remove the first occurrence of `remove_rules` after the first occurrence of the `after` string. The `remove_rules` will be processed before the `add_rules`.  # noqa: E501

        :return: The after of this NfsRulePatch.  # noqa: E501
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this NfsRulePatch.

        The `after` field can be used with `add_rules` or `remove_rules` or both. If used with `add_rules`, then the `add_rules` string will be inserted after the first occurrence of the `after` string. If used with `remove_rules`, then remove the first occurrence of `remove_rules` after the first occurrence of the `after` string. The `remove_rules` will be processed before the `add_rules`.  # noqa: E501

        :param after: The after of this NfsRulePatch.  # noqa: E501
        :type: str
        """

        self._after = after

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
        if issubclass(NfsRulePatch, dict):
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
        if not isinstance(other, NfsRulePatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
