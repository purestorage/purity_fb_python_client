# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.6 Python SDK

    Pure Storage FlashBlade REST 1.6 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DirectoryService(object):
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
        'base_dn': 'str',
        'bind_password': 'str',
        'bind_user': 'str',
        'enabled': 'bool',
        'services': 'list[str]',
        'uris': 'list[str]',
        'smb': 'DirectoryserviceSmb'
    }

    attribute_map = {
        'name': 'name',
        'base_dn': 'base_dn',
        'bind_password': 'bind_password',
        'bind_user': 'bind_user',
        'enabled': 'enabled',
        'services': 'services',
        'uris': 'uris',
        'smb': 'smb'
    }

    def __init__(self, name=None, base_dn=None, bind_password=None, bind_user=None, enabled=None, services=None, uris=None, smb=None):  # noqa: E501
        """DirectoryService - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._base_dn = None
        self._bind_password = None
        self._bind_user = None
        self._enabled = None
        self._services = None
        self._uris = None
        self._smb = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if base_dn is not None:
            self.base_dn = base_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if bind_user is not None:
            self.bind_user = bind_user
        if enabled is not None:
            self.enabled = enabled
        if services is not None:
            self.services = services
        if uris is not None:
            self.uris = uris
        if smb is not None:
            self.smb = smb

    @property
    def name(self):
        """Gets the name of this DirectoryService.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this DirectoryService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectoryService.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this DirectoryService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_dn(self):
        """Gets the base_dn of this DirectoryService.  # noqa: E501

        Base of the Distinguished Name (DN) of the directory service groups.  # noqa: E501

        :return: The base_dn of this DirectoryService.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this DirectoryService.

        Base of the Distinguished Name (DN) of the directory service groups.  # noqa: E501

        :param base_dn: The base_dn of this DirectoryService.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def bind_password(self):
        """Gets the bind_password of this DirectoryService.  # noqa: E501

        Obfuscated password used to query the directory.  # noqa: E501

        :return: The bind_password of this DirectoryService.  # noqa: E501
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this DirectoryService.

        Obfuscated password used to query the directory.  # noqa: E501

        :param bind_password: The bind_password of this DirectoryService.  # noqa: E501
        :type: str
        """

        self._bind_password = bind_password

    @property
    def bind_user(self):
        """Gets the bind_user of this DirectoryService.  # noqa: E501

        Username used to query the directory.  # noqa: E501

        :return: The bind_user of this DirectoryService.  # noqa: E501
        :rtype: str
        """
        return self._bind_user

    @bind_user.setter
    def bind_user(self, bind_user):
        """Sets the bind_user of this DirectoryService.

        Username used to query the directory.  # noqa: E501

        :param bind_user: The bind_user of this DirectoryService.  # noqa: E501
        :type: str
        """

        self._bind_user = bind_user

    @property
    def enabled(self):
        """Gets the enabled of this DirectoryService.  # noqa: E501

        Is the directory service enabled or not?  # noqa: E501

        :return: The enabled of this DirectoryService.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DirectoryService.

        Is the directory service enabled or not?  # noqa: E501

        :param enabled: The enabled of this DirectoryService.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def services(self):
        """Gets the services of this DirectoryService.  # noqa: E501

        Services that the directory service configuration is used for.  # noqa: E501

        :return: The services of this DirectoryService.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this DirectoryService.

        Services that the directory service configuration is used for.  # noqa: E501

        :param services: The services of this DirectoryService.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def uris(self):
        """Gets the uris of this DirectoryService.  # noqa: E501

        List of URIs for the configured directory servers.  # noqa: E501

        :return: The uris of this DirectoryService.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this DirectoryService.

        List of URIs for the configured directory servers.  # noqa: E501

        :param uris: The uris of this DirectoryService.  # noqa: E501
        :type: list[str]
        """

        self._uris = uris

    @property
    def smb(self):
        """Gets the smb of this DirectoryService.  # noqa: E501


        :return: The smb of this DirectoryService.  # noqa: E501
        :rtype: DirectoryserviceSmb
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """Sets the smb of this DirectoryService.


        :param smb: The smb of this DirectoryService.  # noqa: E501
        :type: DirectoryserviceSmb
        """

        self._smb = smb

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
        if issubclass(DirectoryService, dict):
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
        if not isinstance(other, DirectoryService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
