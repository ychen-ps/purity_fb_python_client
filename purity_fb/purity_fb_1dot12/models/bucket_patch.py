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


class BucketPatch(object):
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
        'destroyed': 'bool',
        'versioning': 'str'
    }

    attribute_map = {
        'destroyed': 'destroyed',
        'versioning': 'versioning'
    }

    def __init__(self, destroyed=None, versioning=None):  # noqa: E501
        """BucketPatch - a model defined in Swagger"""  # noqa: E501

        self._destroyed = None
        self._versioning = None
        self.discriminator = None

        if destroyed is not None:
            self.destroyed = destroyed
        if versioning is not None:
            self.versioning = versioning

    @property
    def destroyed(self):
        """Gets the destroyed of this BucketPatch.  # noqa: E501

        Is the bucket destroyed?  # noqa: E501

        :return: The destroyed of this BucketPatch.  # noqa: E501
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """Sets the destroyed of this BucketPatch.

        Is the bucket destroyed?  # noqa: E501

        :param destroyed: The destroyed of this BucketPatch.  # noqa: E501
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def versioning(self):
        """Gets the versioning of this BucketPatch.  # noqa: E501

        The versioning state for objects within the bucket. Valid values are `none`, `enabled`, and `suspended`.  # noqa: E501

        :return: The versioning of this BucketPatch.  # noqa: E501
        :rtype: str
        """
        return self._versioning

    @versioning.setter
    def versioning(self, versioning):
        """Sets the versioning of this BucketPatch.

        The versioning state for objects within the bucket. Valid values are `none`, `enabled`, and `suspended`.  # noqa: E501

        :param versioning: The versioning of this BucketPatch.  # noqa: E501
        :type: str
        """

        self._versioning = versioning

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
        if issubclass(BucketPatch, dict):
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
        if not isinstance(other, BucketPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
