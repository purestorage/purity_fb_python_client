# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.12 Python SDK

    Pure Storage FlashBlade REST 1.12 Python SDK. Compatible with REST API versions 1.0 - 1.12. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.12
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PolicyMemberWithRemote(object):
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
        'policy': 'PolicyReferenceWithId',
        'member': 'PolicyReferenceWithId',
        'link': 'MemberLink'
    }

    attribute_map = {
        'policy': 'policy',
        'member': 'member',
        'link': 'link'
    }

    def __init__(self, policy=None, member=None, link=None):  # noqa: E501
        """PolicyMemberWithRemote - a model defined in Swagger"""  # noqa: E501

        self._policy = None
        self._member = None
        self._link = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy
        if member is not None:
            self.member = member
        if link is not None:
            self.link = link

    @property
    def policy(self):
        """Gets the policy of this PolicyMemberWithRemote.  # noqa: E501


        :return: The policy of this PolicyMemberWithRemote.  # noqa: E501
        :rtype: PolicyReferenceWithId
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyMemberWithRemote.


        :param policy: The policy of this PolicyMemberWithRemote.  # noqa: E501
        :type: PolicyReferenceWithId
        """

        self._policy = policy

    @property
    def member(self):
        """Gets the member of this PolicyMemberWithRemote.  # noqa: E501


        :return: The member of this PolicyMemberWithRemote.  # noqa: E501
        :rtype: PolicyReferenceWithId
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this PolicyMemberWithRemote.


        :param member: The member of this PolicyMemberWithRemote.  # noqa: E501
        :type: PolicyReferenceWithId
        """

        self._member = member

    @property
    def link(self):
        """Gets the link of this PolicyMemberWithRemote.  # noqa: E501


        :return: The link of this PolicyMemberWithRemote.  # noqa: E501
        :rtype: MemberLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this PolicyMemberWithRemote.


        :param link: The link of this PolicyMemberWithRemote.  # noqa: E501
        :type: MemberLink
        """

        self._link = link

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
        if issubclass(PolicyMemberWithRemote, dict):
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
        if not isinstance(other, PolicyMemberWithRemote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other