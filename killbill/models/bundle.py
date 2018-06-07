# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.19.16-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Bundle(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'account_id': 'Str',
        'bundle_id': 'Str',
        'external_key': 'Str',
        'subscriptions': 'List[Subscription]',
        'timeline': 'BundleTimeline',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bundle_id': 'bundleId',
        'external_key': 'externalKey',
        'subscriptions': 'subscriptions',
        'timeline': 'timeline',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, bundle_id=None, external_key=None, subscriptions=None, timeline=None, audit_logs=None):  # noqa: E501
        """Bundle - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._bundle_id = None
        self._external_key = None
        self._subscriptions = None
        self._timeline = None
        self._audit_logs = None
        self.discriminator = None

        self.account_id = account_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if external_key is not None:
            self.external_key = external_key
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if timeline is not None:
            self.timeline = timeline
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this Bundle.  # noqa: E501


        :return: The account_id of this Bundle.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Bundle.


        :param account_id: The account_id of this Bundle.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this Bundle.  # noqa: E501


        :return: The bundle_id of this Bundle.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this Bundle.


        :param bundle_id: The bundle_id of this Bundle.  # noqa: E501
        :type: Str
        """


        self._bundle_id = bundle_id

    @property
    def external_key(self):
        """Gets the external_key of this Bundle.  # noqa: E501


        :return: The external_key of this Bundle.  # noqa: E501
        :rtype: Str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this Bundle.


        :param external_key: The external_key of this Bundle.  # noqa: E501
        :type: Str
        """


        self._external_key = external_key

    @property
    def subscriptions(self):
        """Gets the subscriptions of this Bundle.  # noqa: E501


        :return: The subscriptions of this Bundle.  # noqa: E501
        :rtype: List[Subscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this Bundle.


        :param subscriptions: The subscriptions of this Bundle.  # noqa: E501
        :type: List[Subscription]
        """


        self._subscriptions = subscriptions

    @property
    def timeline(self):
        """Gets the timeline of this Bundle.  # noqa: E501


        :return: The timeline of this Bundle.  # noqa: E501
        :rtype: BundleTimeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this Bundle.


        :param timeline: The timeline of this Bundle.  # noqa: E501
        :type: BundleTimeline
        """


        self._timeline = timeline

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Bundle.  # noqa: E501


        :return: The audit_logs of this Bundle.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Bundle.


        :param audit_logs: The audit_logs of this Bundle.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
