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


class Support(object):
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
        'created': 'int',
        'phonehome_enabled': 'bool',
        'proxy': 'str',
        'remote_assist_active': 'bool',
        'remote_assist_opened': 'str',
        'remote_assist_expires': 'str',
        'remote_assist_status': 'str',
        'remote_assist_paths': 'list[SupportRemoteAssistPaths]'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'phonehome_enabled': 'phonehome_enabled',
        'proxy': 'proxy',
        'remote_assist_active': 'remote_assist_active',
        'remote_assist_opened': 'remote_assist_opened',
        'remote_assist_expires': 'remote_assist_expires',
        'remote_assist_status': 'remote_assist_status',
        'remote_assist_paths': 'remote_assist_paths'
    }

    def __init__(self, name=None, created=None, phonehome_enabled=None, proxy=None, remote_assist_active=None, remote_assist_opened=None, remote_assist_expires=None, remote_assist_status=None, remote_assist_paths=None):  # noqa: E501
        """Support - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._created = None
        self._phonehome_enabled = None
        self._proxy = None
        self._remote_assist_active = None
        self._remote_assist_opened = None
        self._remote_assist_expires = None
        self._remote_assist_status = None
        self._remote_assist_paths = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if phonehome_enabled is not None:
            self.phonehome_enabled = phonehome_enabled
        if proxy is not None:
            self.proxy = proxy
        if remote_assist_active is not None:
            self.remote_assist_active = remote_assist_active
        if remote_assist_opened is not None:
            self.remote_assist_opened = remote_assist_opened
        if remote_assist_expires is not None:
            self.remote_assist_expires = remote_assist_expires
        if remote_assist_status is not None:
            self.remote_assist_status = remote_assist_status
        if remote_assist_paths is not None:
            self.remote_assist_paths = remote_assist_paths

    @property
    def name(self):
        """Gets the name of this Support.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this Support.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Support.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this Support.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this Support.  # noqa: E501

        Creation timestamp of the object  # noqa: E501

        :return: The created of this Support.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Support.

        Creation timestamp of the object  # noqa: E501

        :param created: The created of this Support.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def phonehome_enabled(self):
        """Gets the phonehome_enabled of this Support.  # noqa: E501

        Is phonehome of logs enabled?  # noqa: E501

        :return: The phonehome_enabled of this Support.  # noqa: E501
        :rtype: bool
        """
        return self._phonehome_enabled

    @phonehome_enabled.setter
    def phonehome_enabled(self, phonehome_enabled):
        """Sets the phonehome_enabled of this Support.

        Is phonehome of logs enabled?  # noqa: E501

        :param phonehome_enabled: The phonehome_enabled of this Support.  # noqa: E501
        :type: bool
        """

        self._phonehome_enabled = phonehome_enabled

    @property
    def proxy(self):
        """Gets the proxy of this Support.  # noqa: E501

        Server to use as the HTTP or HTTPS proxy. Specify the server name, including the scheme and proxy port number.  # noqa: E501

        :return: The proxy of this Support.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this Support.

        Server to use as the HTTP or HTTPS proxy. Specify the server name, including the scheme and proxy port number.  # noqa: E501

        :param proxy: The proxy of this Support.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def remote_assist_active(self):
        """Gets the remote_assist_active of this Support.  # noqa: E501

        The switch to open all remote-assist sessions. Modifiable.  # noqa: E501

        :return: The remote_assist_active of this Support.  # noqa: E501
        :rtype: bool
        """
        return self._remote_assist_active

    @remote_assist_active.setter
    def remote_assist_active(self, remote_assist_active):
        """Sets the remote_assist_active of this Support.

        The switch to open all remote-assist sessions. Modifiable.  # noqa: E501

        :param remote_assist_active: The remote_assist_active of this Support.  # noqa: E501
        :type: bool
        """

        self._remote_assist_active = remote_assist_active

    @property
    def remote_assist_opened(self):
        """Gets the remote_assist_opened of this Support.  # noqa: E501

        The time when the session opened.  # noqa: E501

        :return: The remote_assist_opened of this Support.  # noqa: E501
        :rtype: str
        """
        return self._remote_assist_opened

    @remote_assist_opened.setter
    def remote_assist_opened(self, remote_assist_opened):
        """Sets the remote_assist_opened of this Support.

        The time when the session opened.  # noqa: E501

        :param remote_assist_opened: The remote_assist_opened of this Support.  # noqa: E501
        :type: str
        """

        self._remote_assist_opened = remote_assist_opened

    @property
    def remote_assist_expires(self):
        """Gets the remote_assist_expires of this Support.  # noqa: E501

        The time when the session expires.  # noqa: E501

        :return: The remote_assist_expires of this Support.  # noqa: E501
        :rtype: str
        """
        return self._remote_assist_expires

    @remote_assist_expires.setter
    def remote_assist_expires(self, remote_assist_expires):
        """Sets the remote_assist_expires of this Support.

        The time when the session expires.  # noqa: E501

        :param remote_assist_expires: The remote_assist_expires of this Support.  # noqa: E501
        :type: str
        """

        self._remote_assist_expires = remote_assist_expires

    @property
    def remote_assist_status(self):
        """Gets the remote_assist_status of this Support.  # noqa: E501

        The status of the remote-assist sessions. Possible values are connected, partially_connected, reconnecting, and disconnected.  # noqa: E501

        :return: The remote_assist_status of this Support.  # noqa: E501
        :rtype: str
        """
        return self._remote_assist_status

    @remote_assist_status.setter
    def remote_assist_status(self, remote_assist_status):
        """Sets the remote_assist_status of this Support.

        The status of the remote-assist sessions. Possible values are connected, partially_connected, reconnecting, and disconnected.  # noqa: E501

        :param remote_assist_status: The remote_assist_status of this Support.  # noqa: E501
        :type: str
        """

        self._remote_assist_status = remote_assist_status

    @property
    def remote_assist_paths(self):
        """Gets the remote_assist_paths of this Support.  # noqa: E501


        :return: The remote_assist_paths of this Support.  # noqa: E501
        :rtype: list[SupportRemoteAssistPaths]
        """
        return self._remote_assist_paths

    @remote_assist_paths.setter
    def remote_assist_paths(self, remote_assist_paths):
        """Sets the remote_assist_paths of this Support.


        :param remote_assist_paths: The remote_assist_paths of this Support.  # noqa: E501
        :type: list[SupportRemoteAssistPaths]
        """

        self._remote_assist_paths = remote_assist_paths

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
        if issubclass(Support, dict):
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
        if not isinstance(other, Support):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
