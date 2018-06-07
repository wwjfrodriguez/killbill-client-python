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



class OverdueStateConfig(object):
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
        'name': 'Str',
        'is_clear_state': 'Bool',
        'condition': 'OverdueCondition',
        'external_message': 'Str',
        'is_block_changes': 'Bool',
        'is_disable_entitlement': 'Bool',
        'subscription_cancellation_policy': 'Str',
        'auto_reevaluation_interval_days': 'Int'
    }

    attribute_map = {
        'name': 'name',
        'is_clear_state': 'isClearState',
        'condition': 'condition',
        'external_message': 'externalMessage',
        'is_block_changes': 'isBlockChanges',
        'is_disable_entitlement': 'isDisableEntitlement',
        'subscription_cancellation_policy': 'subscriptionCancellationPolicy',
        'auto_reevaluation_interval_days': 'autoReevaluationIntervalDays'
    }

    def __init__(self, name=None, is_clear_state=False, condition=None, external_message=None, is_block_changes=False, is_disable_entitlement=False, subscription_cancellation_policy=None, auto_reevaluation_interval_days=None):  # noqa: E501
        """OverdueStateConfig - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._is_clear_state = None
        self._condition = None
        self._external_message = None
        self._is_block_changes = None
        self._is_disable_entitlement = None
        self._subscription_cancellation_policy = None
        self._auto_reevaluation_interval_days = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_clear_state is not None:
            self.is_clear_state = is_clear_state
        if condition is not None:
            self.condition = condition
        if external_message is not None:
            self.external_message = external_message
        if is_block_changes is not None:
            self.is_block_changes = is_block_changes
        if is_disable_entitlement is not None:
            self.is_disable_entitlement = is_disable_entitlement
        if subscription_cancellation_policy is not None:
            self.subscription_cancellation_policy = subscription_cancellation_policy
        if auto_reevaluation_interval_days is not None:
            self.auto_reevaluation_interval_days = auto_reevaluation_interval_days

    @property
    def name(self):
        """Gets the name of this OverdueStateConfig.  # noqa: E501


        :return: The name of this OverdueStateConfig.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OverdueStateConfig.


        :param name: The name of this OverdueStateConfig.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def is_clear_state(self):
        """Gets the is_clear_state of this OverdueStateConfig.  # noqa: E501


        :return: The is_clear_state of this OverdueStateConfig.  # noqa: E501
        :rtype: Bool
        """
        return self._is_clear_state

    @is_clear_state.setter
    def is_clear_state(self, is_clear_state):
        """Sets the is_clear_state of this OverdueStateConfig.


        :param is_clear_state: The is_clear_state of this OverdueStateConfig.  # noqa: E501
        :type: Bool
        """


        self._is_clear_state = is_clear_state

    @property
    def condition(self):
        """Gets the condition of this OverdueStateConfig.  # noqa: E501


        :return: The condition of this OverdueStateConfig.  # noqa: E501
        :rtype: OverdueCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this OverdueStateConfig.


        :param condition: The condition of this OverdueStateConfig.  # noqa: E501
        :type: OverdueCondition
        """


        self._condition = condition

    @property
    def external_message(self):
        """Gets the external_message of this OverdueStateConfig.  # noqa: E501


        :return: The external_message of this OverdueStateConfig.  # noqa: E501
        :rtype: Str
        """
        return self._external_message

    @external_message.setter
    def external_message(self, external_message):
        """Sets the external_message of this OverdueStateConfig.


        :param external_message: The external_message of this OverdueStateConfig.  # noqa: E501
        :type: Str
        """


        self._external_message = external_message

    @property
    def is_block_changes(self):
        """Gets the is_block_changes of this OverdueStateConfig.  # noqa: E501


        :return: The is_block_changes of this OverdueStateConfig.  # noqa: E501
        :rtype: Bool
        """
        return self._is_block_changes

    @is_block_changes.setter
    def is_block_changes(self, is_block_changes):
        """Sets the is_block_changes of this OverdueStateConfig.


        :param is_block_changes: The is_block_changes of this OverdueStateConfig.  # noqa: E501
        :type: Bool
        """


        self._is_block_changes = is_block_changes

    @property
    def is_disable_entitlement(self):
        """Gets the is_disable_entitlement of this OverdueStateConfig.  # noqa: E501


        :return: The is_disable_entitlement of this OverdueStateConfig.  # noqa: E501
        :rtype: Bool
        """
        return self._is_disable_entitlement

    @is_disable_entitlement.setter
    def is_disable_entitlement(self, is_disable_entitlement):
        """Sets the is_disable_entitlement of this OverdueStateConfig.


        :param is_disable_entitlement: The is_disable_entitlement of this OverdueStateConfig.  # noqa: E501
        :type: Bool
        """


        self._is_disable_entitlement = is_disable_entitlement

    @property
    def subscription_cancellation_policy(self):
        """Gets the subscription_cancellation_policy of this OverdueStateConfig.  # noqa: E501


        :return: The subscription_cancellation_policy of this OverdueStateConfig.  # noqa: E501
        :rtype: Str
        """
        return self._subscription_cancellation_policy

    @subscription_cancellation_policy.setter
    def subscription_cancellation_policy(self, subscription_cancellation_policy):
        """Sets the subscription_cancellation_policy of this OverdueStateConfig.


        :param subscription_cancellation_policy: The subscription_cancellation_policy of this OverdueStateConfig.  # noqa: E501
        :type: Str
        """


        self._subscription_cancellation_policy = subscription_cancellation_policy

    @property
    def auto_reevaluation_interval_days(self):
        """Gets the auto_reevaluation_interval_days of this OverdueStateConfig.  # noqa: E501


        :return: The auto_reevaluation_interval_days of this OverdueStateConfig.  # noqa: E501
        :rtype: Int
        """
        return self._auto_reevaluation_interval_days

    @auto_reevaluation_interval_days.setter
    def auto_reevaluation_interval_days(self, auto_reevaluation_interval_days):
        """Sets the auto_reevaluation_interval_days of this OverdueStateConfig.


        :param auto_reevaluation_interval_days: The auto_reevaluation_interval_days of this OverdueStateConfig.  # noqa: E501
        :type: Int
        """


        self._auto_reevaluation_interval_days = auto_reevaluation_interval_days

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
        if not isinstance(other, OverdueStateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
