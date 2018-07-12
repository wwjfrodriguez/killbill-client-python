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



class Unit(object):
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
        'pretty_name': 'Str'
    }

    attribute_map = {
        'name': 'name',
        'pretty_name': 'prettyName'
    }

    def __init__(self, name=None, pretty_name=None):  # noqa: E501
        """Unit - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._pretty_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if pretty_name is not None:
            self.pretty_name = pretty_name

    @property
    def name(self):
        """Gets the name of this Unit.  # noqa: E501


        :return: The name of this Unit.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Unit.


        :param name: The name of this Unit.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def pretty_name(self):
        """Gets the pretty_name of this Unit.  # noqa: E501


        :return: The pretty_name of this Unit.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, pretty_name):
        """Sets the pretty_name of this Unit.


        :param pretty_name: The pretty_name of this Unit.  # noqa: E501
        :type: Str
        """


        self._pretty_name = pretty_name

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
        if not isinstance(other, Unit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
