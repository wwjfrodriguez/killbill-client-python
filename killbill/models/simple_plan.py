# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SimplePlan(object):
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
        'plan_id': 'str',
        'product_name': 'str',
        'product_category': 'str',
        'currency': 'str',
        'amount': 'float',
        'billing_period': 'str',
        'trial_length': 'int',
        'trial_time_unit': 'str',
        'available_base_products': 'list[str]'
    }

    attribute_map = {
        'plan_id': 'planId',
        'product_name': 'productName',
        'product_category': 'productCategory',
        'currency': 'currency',
        'amount': 'amount',
        'billing_period': 'billingPeriod',
        'trial_length': 'trialLength',
        'trial_time_unit': 'trialTimeUnit',
        'available_base_products': 'availableBaseProducts'
    }

    def __init__(self, plan_id=None, product_name=None, product_category=None, currency=None, amount=None, billing_period=None, trial_length=None, trial_time_unit=None, available_base_products=None):  # noqa: E501
        """SimplePlan - a model defined in Swagger"""  # noqa: E501

        self._plan_id = None
        self._product_name = None
        self._product_category = None
        self._currency = None
        self._amount = None
        self._billing_period = None
        self._trial_length = None
        self._trial_time_unit = None
        self._available_base_products = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if product_name is not None:
            self.product_name = product_name
        if product_category is not None:
            self.product_category = product_category
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if billing_period is not None:
            self.billing_period = billing_period
        if trial_length is not None:
            self.trial_length = trial_length
        if trial_time_unit is not None:
            self.trial_time_unit = trial_time_unit
        if available_base_products is not None:
            self.available_base_products = available_base_products

    @property
    def plan_id(self):
        """Gets the plan_id of this SimplePlan.  # noqa: E501


        :return: The plan_id of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SimplePlan.


        :param plan_id: The plan_id of this SimplePlan.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def product_name(self):
        """Gets the product_name of this SimplePlan.  # noqa: E501


        :return: The product_name of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SimplePlan.


        :param product_name: The product_name of this SimplePlan.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_category(self):
        """Gets the product_category of this SimplePlan.  # noqa: E501


        :return: The product_category of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this SimplePlan.


        :param product_category: The product_category of this SimplePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["BASE", "ADD_ON", "STANDALONE"]  # noqa: E501
        if product_category not in allowed_values:
            raise ValueError(
                "Invalid value for `product_category` ({0}), must be one of {1}"  # noqa: E501
                .format(product_category, allowed_values)
            )

        self._product_category = product_category

    @property
    def currency(self):
        """Gets the currency of this SimplePlan.  # noqa: E501


        :return: The currency of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SimplePlan.


        :param currency: The currency of this SimplePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this SimplePlan.  # noqa: E501


        :return: The amount of this SimplePlan.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SimplePlan.


        :param amount: The amount of this SimplePlan.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def billing_period(self):
        """Gets the billing_period of this SimplePlan.  # noqa: E501


        :return: The billing_period of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this SimplePlan.


        :param billing_period: The billing_period of this SimplePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "BIWEEKLY", "THIRTY_DAYS", "SIXTY_DAYS", "NINETY_DAYS", "MONTHLY", "BIMESTRIAL", "QUARTERLY", "TRIANNUAL", "BIANNUAL", "ANNUAL", "BIENNIAL", "NO_BILLING_PERIOD"]  # noqa: E501
        if billing_period not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

    @property
    def trial_length(self):
        """Gets the trial_length of this SimplePlan.  # noqa: E501


        :return: The trial_length of this SimplePlan.  # noqa: E501
        :rtype: int
        """
        return self._trial_length

    @trial_length.setter
    def trial_length(self, trial_length):
        """Sets the trial_length of this SimplePlan.


        :param trial_length: The trial_length of this SimplePlan.  # noqa: E501
        :type: int
        """

        self._trial_length = trial_length

    @property
    def trial_time_unit(self):
        """Gets the trial_time_unit of this SimplePlan.  # noqa: E501


        :return: The trial_time_unit of this SimplePlan.  # noqa: E501
        :rtype: str
        """
        return self._trial_time_unit

    @trial_time_unit.setter
    def trial_time_unit(self, trial_time_unit):
        """Sets the trial_time_unit of this SimplePlan.


        :param trial_time_unit: The trial_time_unit of this SimplePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAYS", "WEEKS", "MONTHS", "YEARS", "UNLIMITED"]  # noqa: E501
        if trial_time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `trial_time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(trial_time_unit, allowed_values)
            )

        self._trial_time_unit = trial_time_unit

    @property
    def available_base_products(self):
        """Gets the available_base_products of this SimplePlan.  # noqa: E501


        :return: The available_base_products of this SimplePlan.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_base_products

    @available_base_products.setter
    def available_base_products(self, available_base_products):
        """Sets the available_base_products of this SimplePlan.


        :param available_base_products: The available_base_products of this SimplePlan.  # noqa: E501
        :type: list[str]
        """

        self._available_base_products = available_base_products

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
        if not isinstance(other, SimplePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
