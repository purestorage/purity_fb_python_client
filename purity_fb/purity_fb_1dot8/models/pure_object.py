# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.8 Python SDK

    Pure Storage FlashBlade REST 1.8 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PureObject(object):
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
        'created': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created'
    }

    def __init__(self, name=None, created=None):  # noqa: E501
        """PureObject - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._created = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created is not None:
            self.created = created

    @property
    def name(self):
        """Gets the name of this PureObject.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this PureObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PureObject.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this PureObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this PureObject.  # noqa: E501

        Creation timestamp of the object  # noqa: E501

        :return: The created of this PureObject.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PureObject.

        Creation timestamp of the object  # noqa: E501

        :param created: The created of this PureObject.  # noqa: E501
        :type: int
        """

        self._created = created

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
        if issubclass(PureObject, dict):
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
        if not isinstance(other, PureObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
