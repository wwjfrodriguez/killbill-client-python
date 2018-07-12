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

    OpenAPI spec version: 0.20.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class AuditLog(object):
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
        'change_type': 'Str',
        'change_date': 'Datetime',
        'object_type': 'Str',
        'object_id': 'Str',
        'changed_by': 'Str',
        'reason_code': 'Str',
        'comments': 'Str',
        'user_token': 'Str',
        'history': 'Entity'
    }

    attribute_map = {
        'change_type': 'changeType',
        'change_date': 'changeDate',
        'object_type': 'objectType',
        'object_id': 'objectId',
        'changed_by': 'changedBy',
        'reason_code': 'reasonCode',
        'comments': 'comments',
        'user_token': 'userToken',
        'history': 'history'
    }

    def __init__(self, change_type=None, change_date=None, object_type=None, object_id=None, changed_by=None, reason_code=None, comments=None, user_token=None, history=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501

        self._change_type = None
        self._change_date = None
        self._object_type = None
        self._object_id = None
        self._changed_by = None
        self._reason_code = None
        self._comments = None
        self._user_token = None
        self._history = None
        self.discriminator = None

        if change_type is not None:
            self.change_type = change_type
        if change_date is not None:
            self.change_date = change_date
        if object_type is not None:
            self.object_type = object_type
        if object_id is not None:
            self.object_id = object_id
        if changed_by is not None:
            self.changed_by = changed_by
        if reason_code is not None:
            self.reason_code = reason_code
        if comments is not None:
            self.comments = comments
        if user_token is not None:
            self.user_token = user_token
        if history is not None:
            self.history = history

    @property
    def change_type(self):
        """Gets the change_type of this AuditLog.  # noqa: E501


        :return: The change_type of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this AuditLog.


        :param change_type: The change_type of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._change_type = change_type

    @property
    def change_date(self):
        """Gets the change_date of this AuditLog.  # noqa: E501


        :return: The change_date of this AuditLog.  # noqa: E501
        :rtype: Datetime
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """Sets the change_date of this AuditLog.


        :param change_date: The change_date of this AuditLog.  # noqa: E501
        :type: Datetime
        """


        self._change_date = change_date

    @property
    def object_type(self):
        """Gets the object_type of this AuditLog.  # noqa: E501


        :return: The object_type of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this AuditLog.


        :param object_type: The object_type of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this AuditLog.  # noqa: E501


        :return: The object_id of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AuditLog.


        :param object_id: The object_id of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._object_id = object_id

    @property
    def changed_by(self):
        """Gets the changed_by of this AuditLog.  # noqa: E501


        :return: The changed_by of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this AuditLog.


        :param changed_by: The changed_by of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._changed_by = changed_by

    @property
    def reason_code(self):
        """Gets the reason_code of this AuditLog.  # noqa: E501


        :return: The reason_code of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this AuditLog.


        :param reason_code: The reason_code of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._reason_code = reason_code

    @property
    def comments(self):
        """Gets the comments of this AuditLog.  # noqa: E501


        :return: The comments of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AuditLog.


        :param comments: The comments of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._comments = comments

    @property
    def user_token(self):
        """Gets the user_token of this AuditLog.  # noqa: E501


        :return: The user_token of this AuditLog.  # noqa: E501
        :rtype: Str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        """Sets the user_token of this AuditLog.


        :param user_token: The user_token of this AuditLog.  # noqa: E501
        :type: Str
        """


        self._user_token = user_token

    @property
    def history(self):
        """Gets the history of this AuditLog.  # noqa: E501


        :return: The history of this AuditLog.  # noqa: E501
        :rtype: Entity
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this AuditLog.


        :param history: The history of this AuditLog.  # noqa: E501
        :type: Entity
        """


        self._history = history

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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
