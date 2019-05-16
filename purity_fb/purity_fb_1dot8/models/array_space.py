# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.8), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ArraySpace(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'capacity': 'int',
        'parity': 'float',
        'space': 'Space',
        'time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'capacity': 'capacity',
        'parity': 'parity',
        'space': 'space',
        'time': 'time'
    }

    def __init__(self, name=None, capacity=None, parity=None, space=None, time=None):
        """
        ArraySpace - a model defined in Swagger
        """

        self._name = None
        self._capacity = None
        self._parity = None
        self._space = None
        self._time = None

        if name is not None:
          self.name = name
        if capacity is not None:
          self.capacity = capacity
        if parity is not None:
          self.parity = parity
        if space is not None:
          self.space = space
        if time is not None:
          self.time = time

    @property
    def name(self):
        """
        Gets the name of this ArraySpace.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this ArraySpace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ArraySpace.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this ArraySpace.
        :type: str
        """

        self._name = name

    @property
    def capacity(self):
        """
        Gets the capacity of this ArraySpace.
        usable capacity in bytes

        :return: The capacity of this ArraySpace.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ArraySpace.
        usable capacity in bytes

        :param capacity: The capacity of this ArraySpace.
        :type: int
        """

        self._capacity = capacity

    @property
    def parity(self):
        """
        Gets the parity of this ArraySpace.

        :return: The parity of this ArraySpace.
        :rtype: float
        """
        return self._parity

    @parity.setter
    def parity(self, parity):
        """
        Sets the parity of this ArraySpace.

        :param parity: The parity of this ArraySpace.
        :type: float
        """

        self._parity = parity

    @property
    def space(self):
        """
        Gets the space of this ArraySpace.
        the space measurement of the array

        :return: The space of this ArraySpace.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this ArraySpace.
        the space measurement of the array

        :param space: The space of this ArraySpace.
        :type: Space
        """

        self._space = space

    @property
    def time(self):
        """
        Gets the time of this ArraySpace.
        Sample time in milliseconds since UNIX epoch

        :return: The time of this ArraySpace.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this ArraySpace.
        Sample time in milliseconds since UNIX epoch

        :param time: The time of this ArraySpace.
        :type: int
        """

        self._time = time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ArraySpace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
