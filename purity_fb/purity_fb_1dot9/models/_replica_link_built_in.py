# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReplicaLinkBuiltIn(object):
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
        'direction': 'Direction',
        'id': 'str',
        'lag': 'int',
        'remote': 'FixedReferenceWithId',
        'status_details': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'id': 'id',
        'lag': 'lag',
        'remote': 'remote',
        'status_details': 'status_details'
    }

    def __init__(self, direction=None, id=None, lag=None, remote=None, status_details=None):  # noqa: E501
        """ReplicaLinkBuiltIn - a model defined in Swagger"""  # noqa: E501

        self._direction = None
        self._id = None
        self._lag = None
        self._remote = None
        self._status_details = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if id is not None:
            self.id = id
        if lag is not None:
            self.lag = lag
        if remote is not None:
            self.remote = remote
        if status_details is not None:
            self.status_details = status_details

    @property
    def direction(self):
        """Gets the direction of this ReplicaLinkBuiltIn.  # noqa: E501


        :return: The direction of this ReplicaLinkBuiltIn.  # noqa: E501
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ReplicaLinkBuiltIn.


        :param direction: The direction of this ReplicaLinkBuiltIn.  # noqa: E501
        :type: Direction
        """

        self._direction = direction

    @property
    def id(self):
        """Gets the id of this ReplicaLinkBuiltIn.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this ReplicaLinkBuiltIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReplicaLinkBuiltIn.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this ReplicaLinkBuiltIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lag(self):
        """Gets the lag of this ReplicaLinkBuiltIn.  # noqa: E501

        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.  # noqa: E501

        :return: The lag of this ReplicaLinkBuiltIn.  # noqa: E501
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this ReplicaLinkBuiltIn.

        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.  # noqa: E501

        :param lag: The lag of this ReplicaLinkBuiltIn.  # noqa: E501
        :type: int
        """

        self._lag = lag

    @property
    def remote(self):
        """Gets the remote of this ReplicaLinkBuiltIn.  # noqa: E501

        Reference to a remote target.  # noqa: E501

        :return: The remote of this ReplicaLinkBuiltIn.  # noqa: E501
        :rtype: FixedReferenceWithId
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this ReplicaLinkBuiltIn.

        Reference to a remote target.  # noqa: E501

        :param remote: The remote of this ReplicaLinkBuiltIn.  # noqa: E501
        :type: FixedReferenceWithId
        """

        self._remote = remote

    @property
    def status_details(self):
        """Gets the status_details of this ReplicaLinkBuiltIn.  # noqa: E501

        Detailed information about the status of the replica link.  # noqa: E501

        :return: The status_details of this ReplicaLinkBuiltIn.  # noqa: E501
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this ReplicaLinkBuiltIn.

        Detailed information about the status of the replica link.  # noqa: E501

        :param status_details: The status_details of this ReplicaLinkBuiltIn.  # noqa: E501
        :type: str
        """

        self._status_details = status_details

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
        if issubclass(ReplicaLinkBuiltIn, dict):
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
        if not isinstance(other, ReplicaLinkBuiltIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
