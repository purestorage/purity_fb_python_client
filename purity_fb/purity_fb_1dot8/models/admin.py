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


class Admin(object):
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
        'api_token': 'AdminApiToken',
        'create_api_token': 'bool',
        'api_token_timeout': 'int',
        'delete_api_token': 'bool',
        'old_password': 'str',
        'password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'api_token': 'api_token',
        'create_api_token': 'create_api_token',
        'api_token_timeout': 'api_token_timeout',
        'delete_api_token': 'delete_api_token',
        'old_password': 'old_password',
        'password': 'password'
    }

    def __init__(self, name=None, api_token=None, create_api_token=None, api_token_timeout=None, delete_api_token=None, old_password=None, password=None):  # noqa: E501
        """Admin - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._api_token = None
        self._create_api_token = None
        self._api_token_timeout = None
        self._delete_api_token = None
        self._old_password = None
        self._password = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if api_token is not None:
            self.api_token = api_token
        if create_api_token is not None:
            self.create_api_token = create_api_token
        if api_token_timeout is not None:
            self.api_token_timeout = api_token_timeout
        if delete_api_token is not None:
            self.delete_api_token = delete_api_token
        if old_password is not None:
            self.old_password = old_password
        if password is not None:
            self.password = password

    @property
    def name(self):
        """Gets the name of this Admin.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Admin.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this Admin.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def api_token(self):
        """Gets the api_token of this Admin.  # noqa: E501


        :return: The api_token of this Admin.  # noqa: E501
        :rtype: AdminApiToken
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this Admin.


        :param api_token: The api_token of this Admin.  # noqa: E501
        :type: AdminApiToken
        """

        self._api_token = api_token

    @property
    def create_api_token(self):
        """Gets the create_api_token of this Admin.  # noqa: E501

        Create a new API token  # noqa: E501

        :return: The create_api_token of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._create_api_token

    @create_api_token.setter
    def create_api_token(self, create_api_token):
        """Sets the create_api_token of this Admin.

        Create a new API token  # noqa: E501

        :param create_api_token: The create_api_token of this Admin.  # noqa: E501
        :type: bool
        """

        self._create_api_token = create_api_token

    @property
    def api_token_timeout(self):
        """Gets the api_token_timeout of this Admin.  # noqa: E501

        Expire api-token after this period (in milliseconds).  # noqa: E501

        :return: The api_token_timeout of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._api_token_timeout

    @api_token_timeout.setter
    def api_token_timeout(self, api_token_timeout):
        """Sets the api_token_timeout of this Admin.

        Expire api-token after this period (in milliseconds).  # noqa: E501

        :param api_token_timeout: The api_token_timeout of this Admin.  # noqa: E501
        :type: int
        """

        self._api_token_timeout = api_token_timeout

    @property
    def delete_api_token(self):
        """Gets the delete_api_token of this Admin.  # noqa: E501

        Delete this user's API token  # noqa: E501

        :return: The delete_api_token of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._delete_api_token

    @delete_api_token.setter
    def delete_api_token(self, delete_api_token):
        """Sets the delete_api_token of this Admin.

        Delete this user's API token  # noqa: E501

        :param delete_api_token: The delete_api_token of this Admin.  # noqa: E501
        :type: bool
        """

        self._delete_api_token = delete_api_token

    @property
    def old_password(self):
        """Gets the old_password of this Admin.  # noqa: E501

        Old user password  # noqa: E501

        :return: The old_password of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this Admin.

        Old user password  # noqa: E501

        :param old_password: The old_password of this Admin.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

    @property
    def password(self):
        """Gets the password of this Admin.  # noqa: E501

        User password  # noqa: E501

        :return: The password of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Admin.

        User password  # noqa: E501

        :param password: The password of this Admin.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(Admin, dict):
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
        if not isinstance(other, Admin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
