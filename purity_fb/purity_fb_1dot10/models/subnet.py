# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.10 Python SDK

    Pure Storage FlashBlade REST 1.10 Python SDK. Compatible with REST API versions 1.0 - 1.10. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.10
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Subnet(object):
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
        'id': 'str',
        'name': 'str',
        'enabled': 'bool',
        'gateway': 'str',
        'interfaces': 'list[Reference]',
        'link_aggregation_group': 'Reference',
        'mtu': 'int',
        'prefix': 'str',
        'services': 'list[str]',
        'vlan': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enabled': 'enabled',
        'gateway': 'gateway',
        'interfaces': 'interfaces',
        'link_aggregation_group': 'link_aggregation_group',
        'mtu': 'mtu',
        'prefix': 'prefix',
        'services': 'services',
        'vlan': 'vlan'
    }

    def __init__(self, id=None, name=None, enabled=None, gateway=None, interfaces=None, link_aggregation_group=None, mtu=None, prefix=None, services=None, vlan=None):  # noqa: E501
        """Subnet - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._enabled = None
        self._gateway = None
        self._interfaces = None
        self._link_aggregation_group = None
        self._mtu = None
        self._prefix = None
        self._services = None
        self._vlan = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if gateway is not None:
            self.gateway = gateway
        if interfaces is not None:
            self.interfaces = interfaces
        if link_aggregation_group is not None:
            self.link_aggregation_group = link_aggregation_group
        if mtu is not None:
            self.mtu = mtu
        if prefix is not None:
            self.prefix = prefix
        if services is not None:
            self.services = services
        if vlan is not None:
            self.vlan = vlan

    @property
    def id(self):
        """Gets the id of this Subnet.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subnet.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this Subnet.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Subnet.  # noqa: E501

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :return: The name of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subnet.

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :param name: The name of this Subnet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this Subnet.  # noqa: E501

        Indicates if subnet is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :return: The enabled of this Subnet.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Subnet.

        Indicates if subnet is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :param enabled: The enabled of this Subnet.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def gateway(self):
        """Gets the gateway of this Subnet.  # noqa: E501

        The IPv4 or IPv6 address of the gateway through which the specified subnet is to communicate with the network.  # noqa: E501

        :return: The gateway of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Subnet.

        The IPv4 or IPv6 address of the gateway through which the specified subnet is to communicate with the network.  # noqa: E501

        :param gateway: The gateway of this Subnet.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def interfaces(self):
        """Gets the interfaces of this Subnet.  # noqa: E501

        List of network interfaces associated with this subnet.  # noqa: E501

        :return: The interfaces of this Subnet.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this Subnet.

        List of network interfaces associated with this subnet.  # noqa: E501

        :param interfaces: The interfaces of this Subnet.  # noqa: E501
        :type: list[Reference]
        """

        self._interfaces = interfaces

    @property
    def link_aggregation_group(self):
        """Gets the link_aggregation_group of this Subnet.  # noqa: E501

        reference of the associated LAG.  # noqa: E501

        :return: The link_aggregation_group of this Subnet.  # noqa: E501
        :rtype: Reference
        """
        return self._link_aggregation_group

    @link_aggregation_group.setter
    def link_aggregation_group(self, link_aggregation_group):
        """Sets the link_aggregation_group of this Subnet.

        reference of the associated LAG.  # noqa: E501

        :param link_aggregation_group: The link_aggregation_group of this Subnet.  # noqa: E501
        :type: Reference
        """

        self._link_aggregation_group = link_aggregation_group

    @property
    def mtu(self):
        """Gets the mtu of this Subnet.  # noqa: E501

        Maximum message transfer unit (packet) size for the subnet in bytes. MTU setting cannot exceed the MTU of the corresponding physical interface. 1500 by default.  # noqa: E501

        :return: The mtu of this Subnet.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this Subnet.

        Maximum message transfer unit (packet) size for the subnet in bytes. MTU setting cannot exceed the MTU of the corresponding physical interface. 1500 by default.  # noqa: E501

        :param mtu: The mtu of this Subnet.  # noqa: E501
        :type: int
        """
        if mtu is not None and mtu > 9216:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value less than or equal to `9216`")  # noqa: E501
        if mtu is not None and mtu < 1280:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value greater than or equal to `1280`")  # noqa: E501

        self._mtu = mtu

    @property
    def prefix(self):
        """Gets the prefix of this Subnet.  # noqa: E501

        The IPv4 or IPv6 address to be associated with the specified subnet.  # noqa: E501

        :return: The prefix of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Subnet.

        The IPv4 or IPv6 address to be associated with the specified subnet.  # noqa: E501

        :param prefix: The prefix of this Subnet.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def services(self):
        """Gets the services of this Subnet.  # noqa: E501

        The services provided by this subnet, as inherited from all of its interfaces.  # noqa: E501

        :return: The services of this Subnet.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Subnet.

        The services provided by this subnet, as inherited from all of its interfaces.  # noqa: E501

        :param services: The services of this Subnet.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def vlan(self):
        """Gets the vlan of this Subnet.  # noqa: E501

        VLAN ID  # noqa: E501

        :return: The vlan of this Subnet.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this Subnet.

        VLAN ID  # noqa: E501

        :param vlan: The vlan of this Subnet.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

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
        if issubclass(Subnet, dict):
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
        if not isinstance(other, Subnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
