# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.4 Python SDK

    Pure Storage FlashBlade REST 1.4 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.4
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PureError(object):
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
        'code': 'int',
        'context': 'str',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'context': 'context',
        'message': 'message'
    }

    def __init__(self, code=None, context=None, message=None):  # noqa: E501
        """PureError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._context = None
        self._message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if context is not None:
            self.context = context
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this PureError.  # noqa: E501

        error code  # noqa: E501

        :return: The code of this PureError.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PureError.

        error code  # noqa: E501

        :param code: The code of this PureError.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def context(self):
        """Gets the context of this PureError.  # noqa: E501

        context of the error  # noqa: E501

        :return: The context of this PureError.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PureError.

        context of the error  # noqa: E501

        :param context: The context of this PureError.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def message(self):
        """Gets the message of this PureError.  # noqa: E501

        error message  # noqa: E501

        :return: The message of this PureError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PureError.

        error message  # noqa: E501

        :param message: The message of this PureError.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(PureError, dict):
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
        if not isinstance(other, PureError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
