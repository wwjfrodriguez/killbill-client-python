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

    OpenAPI spec version: 0.19.17-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class InvoiceEmail(object):
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
        'is_notified_for_invoices': 'Bool',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'is_notified_for_invoices': 'isNotifiedForInvoices',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, is_notified_for_invoices=False, audit_logs=None):  # noqa: E501
        """InvoiceEmail - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._is_notified_for_invoices = None
        self._audit_logs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if is_notified_for_invoices is not None:
            self.is_notified_for_invoices = is_notified_for_invoices
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this InvoiceEmail.  # noqa: E501


        :return: The account_id of this InvoiceEmail.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvoiceEmail.


        :param account_id: The account_id of this InvoiceEmail.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def is_notified_for_invoices(self):
        """Gets the is_notified_for_invoices of this InvoiceEmail.  # noqa: E501


        :return: The is_notified_for_invoices of this InvoiceEmail.  # noqa: E501
        :rtype: Bool
        """
        return self._is_notified_for_invoices

    @is_notified_for_invoices.setter
    def is_notified_for_invoices(self, is_notified_for_invoices):
        """Sets the is_notified_for_invoices of this InvoiceEmail.


        :param is_notified_for_invoices: The is_notified_for_invoices of this InvoiceEmail.  # noqa: E501
        :type: Bool
        """


        self._is_notified_for_invoices = is_notified_for_invoices

    @property
    def audit_logs(self):
        """Gets the audit_logs of this InvoiceEmail.  # noqa: E501


        :return: The audit_logs of this InvoiceEmail.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this InvoiceEmail.


        :param audit_logs: The audit_logs of this InvoiceEmail.  # noqa: E501
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
        if not isinstance(other, InvoiceEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
