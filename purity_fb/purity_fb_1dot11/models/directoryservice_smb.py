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


class DirectoryserviceSmb(object):
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
        'join_ou': 'str'
    }

    attribute_map = {
        'join_ou': 'join_ou'
    }

    def __init__(self, join_ou=None):  # noqa: E501
        """DirectoryserviceSmb - a model defined in Swagger"""  # noqa: E501

        self._join_ou = None
        self.discriminator = None

        if join_ou is not None:
            self.join_ou = join_ou

    @property
    def join_ou(self):
        """Gets the join_ou of this DirectoryserviceSmb.  # noqa: E501

        Optional organizational unit where the machine account for the directory service will be created.   # noqa: E501

        :return: The join_ou of this DirectoryserviceSmb.  # noqa: E501
        :rtype: str
        """
        return self._join_ou

    @join_ou.setter
    def join_ou(self, join_ou):
        """Sets the join_ou of this DirectoryserviceSmb.

        Optional organizational unit where the machine account for the directory service will be created.   # noqa: E501

        :param join_ou: The join_ou of this DirectoryserviceSmb.  # noqa: E501
        :type: str
        """

        self._join_ou = join_ou

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
        if issubclass(DirectoryserviceSmb, dict):
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
        if not isinstance(other, DirectoryserviceSmb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
