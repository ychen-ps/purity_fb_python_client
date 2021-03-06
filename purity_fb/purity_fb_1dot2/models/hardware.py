# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.2 Python SDK

    Pure Storage FlashBlade REST 1.2 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.2
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Hardware(object):
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
        'details': 'str',
        'identify_enabled': 'bool',
        'index': 'int',
        'model': 'str',
        'name': 'str',
        'serial': 'str',
        'slot': 'int',
        'speed': 'int',
        'status': 'str',
        'temperature': 'int',
        'type': 'str'
    }

    attribute_map = {
        'details': 'details',
        'identify_enabled': 'identify_enabled',
        'index': 'index',
        'model': 'model',
        'name': 'name',
        'serial': 'serial',
        'slot': 'slot',
        'speed': 'speed',
        'status': 'status',
        'temperature': 'temperature',
        'type': 'type'
    }

    def __init__(self, details=None, identify_enabled=None, index=None, model=None, name=None, serial=None, slot=None, speed=None, status=None, temperature=None, type=None):  # noqa: E501
        """Hardware - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._identify_enabled = None
        self._index = None
        self._model = None
        self._name = None
        self._serial = None
        self._slot = None
        self._speed = None
        self._status = None
        self._temperature = None
        self._type = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if identify_enabled is not None:
            self.identify_enabled = identify_enabled
        if index is not None:
            self.index = index
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if serial is not None:
            self.serial = serial
        if slot is not None:
            self.slot = slot
        if speed is not None:
            self.speed = speed
        if status is not None:
            self.status = status
        if temperature is not None:
            self.temperature = temperature
        if type is not None:
            self.type = type

    @property
    def details(self):
        """Gets the details of this Hardware.  # noqa: E501

        detailed component status if not healthy  # noqa: E501

        :return: The details of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Hardware.

        detailed component status if not healthy  # noqa: E501

        :param details: The details of this Hardware.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def identify_enabled(self):
        """Gets the identify_enabled of this Hardware.  # noqa: E501

        is visual identifier LED enabled? Modifiable  # noqa: E501

        :return: The identify_enabled of this Hardware.  # noqa: E501
        :rtype: bool
        """
        return self._identify_enabled

    @identify_enabled.setter
    def identify_enabled(self, identify_enabled):
        """Sets the identify_enabled of this Hardware.

        is visual identifier LED enabled? Modifiable  # noqa: E501

        :param identify_enabled: The identify_enabled of this Hardware.  # noqa: E501
        :type: bool
        """

        self._identify_enabled = identify_enabled

    @property
    def index(self):
        """Gets the index of this Hardware.  # noqa: E501

        position of the component within the array  # noqa: E501

        :return: The index of this Hardware.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Hardware.

        position of the component within the array  # noqa: E501

        :param index: The index of this Hardware.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def model(self):
        """Gets the model of this Hardware.  # noqa: E501

        model number of the component  # noqa: E501

        :return: The model of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Hardware.

        model number of the component  # noqa: E501

        :param model: The model of this Hardware.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this Hardware.  # noqa: E501

        component name  # noqa: E501

        :return: The name of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Hardware.

        component name  # noqa: E501

        :param name: The name of this Hardware.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this Hardware.  # noqa: E501

        serial number of the component  # noqa: E501

        :return: The serial of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this Hardware.

        serial number of the component  # noqa: E501

        :param serial: The serial of this Hardware.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def slot(self):
        """Gets the slot of this Hardware.  # noqa: E501

        slot number of the PCI Express card that hosts the component  # noqa: E501

        :return: The slot of this Hardware.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this Hardware.

        slot number of the PCI Express card that hosts the component  # noqa: E501

        :param slot: The slot of this Hardware.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def speed(self):
        """Gets the speed of this Hardware.  # noqa: E501

        speed (in b/s) at which the component is operating  # noqa: E501

        :return: The speed of this Hardware.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this Hardware.

        speed (in b/s) at which the component is operating  # noqa: E501

        :param speed: The speed of this Hardware.  # noqa: E501
        :type: int
        """

        self._speed = speed

    @property
    def status(self):
        """Gets the status of this Hardware.  # noqa: E501

        Component status. Possible values are critical, healthy, identifying, unhealthy, unknown and unused.  # noqa: E501

        :return: The status of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Hardware.

        Component status. Possible values are critical, healthy, identifying, unhealthy, unknown and unused.  # noqa: E501

        :param status: The status of this Hardware.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def temperature(self):
        """Gets the temperature of this Hardware.  # noqa: E501

        temperature reported by the component  # noqa: E501

        :return: The temperature of this Hardware.  # noqa: E501
        :rtype: int
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this Hardware.

        temperature reported by the component  # noqa: E501

        :param temperature: The temperature of this Hardware.  # noqa: E501
        :type: int
        """

        self._temperature = temperature

    @property
    def type(self):
        """Gets the type of this Hardware.  # noqa: E501

        Component type. Possible values are ch, eth, fb, fm and pwr.  # noqa: E501

        :return: The type of this Hardware.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Hardware.

        Component type. Possible values are ch, eth, fb, fm and pwr.  # noqa: E501

        :param type: The type of this Hardware.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Hardware, dict):
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
        if not isinstance(other, Hardware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
