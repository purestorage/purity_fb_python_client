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


class ReplicationPerformance(object):
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
        'transmitted_bytes_per_sec': 'int',
        'received_bytes_per_sec': 'int'
    }

    attribute_map = {
        'transmitted_bytes_per_sec': 'transmitted_bytes_per_sec',
        'received_bytes_per_sec': 'received_bytes_per_sec'
    }

    def __init__(self, transmitted_bytes_per_sec=None, received_bytes_per_sec=None):  # noqa: E501
        """ReplicationPerformance - a model defined in Swagger"""  # noqa: E501

        self._transmitted_bytes_per_sec = None
        self._received_bytes_per_sec = None
        self.discriminator = None

        if transmitted_bytes_per_sec is not None:
            self.transmitted_bytes_per_sec = transmitted_bytes_per_sec
        if received_bytes_per_sec is not None:
            self.received_bytes_per_sec = received_bytes_per_sec

    @property
    def transmitted_bytes_per_sec(self):
        """Gets the transmitted_bytes_per_sec of this ReplicationPerformance.  # noqa: E501

        Total bytes transmitted per second.  # noqa: E501

        :return: The transmitted_bytes_per_sec of this ReplicationPerformance.  # noqa: E501
        :rtype: int
        """
        return self._transmitted_bytes_per_sec

    @transmitted_bytes_per_sec.setter
    def transmitted_bytes_per_sec(self, transmitted_bytes_per_sec):
        """Sets the transmitted_bytes_per_sec of this ReplicationPerformance.

        Total bytes transmitted per second.  # noqa: E501

        :param transmitted_bytes_per_sec: The transmitted_bytes_per_sec of this ReplicationPerformance.  # noqa: E501
        :type: int
        """
        if transmitted_bytes_per_sec is not None and transmitted_bytes_per_sec < 0:  # noqa: E501
            raise ValueError("Invalid value for `transmitted_bytes_per_sec`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transmitted_bytes_per_sec = transmitted_bytes_per_sec

    @property
    def received_bytes_per_sec(self):
        """Gets the received_bytes_per_sec of this ReplicationPerformance.  # noqa: E501

        Total bytes received per second.  # noqa: E501

        :return: The received_bytes_per_sec of this ReplicationPerformance.  # noqa: E501
        :rtype: int
        """
        return self._received_bytes_per_sec

    @received_bytes_per_sec.setter
    def received_bytes_per_sec(self, received_bytes_per_sec):
        """Sets the received_bytes_per_sec of this ReplicationPerformance.

        Total bytes received per second.  # noqa: E501

        :param received_bytes_per_sec: The received_bytes_per_sec of this ReplicationPerformance.  # noqa: E501
        :type: int
        """
        if received_bytes_per_sec is not None and received_bytes_per_sec < 0:  # noqa: E501
            raise ValueError("Invalid value for `received_bytes_per_sec`, must be a value greater than or equal to `0`")  # noqa: E501

        self._received_bytes_per_sec = received_bytes_per_sec

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
        if issubclass(ReplicationPerformance, dict):
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
        if not isinstance(other, ReplicationPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other