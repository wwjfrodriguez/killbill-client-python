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

from killbill.models.audit_log import AuditLog  # noqa: F401,E501
from killbill.models.event_subscription import EventSubscription  # noqa: F401,E501
from killbill.models.phase_price_override import PhasePriceOverride  # noqa: F401,E501


class Subscription(object):
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
        'account_id': 'str',
        'bundle_id': 'str',
        'subscription_id': 'str',
        'external_key': 'str',
        'start_date': 'date',
        'product_name': 'str',
        'product_category': 'str',
        'billing_period': 'str',
        'phase_type': 'str',
        'price_list': 'str',
        'plan_name': 'str',
        'state': 'str',
        'source_type': 'str',
        'cancelled_date': 'date',
        'charged_through_date': 'date',
        'billing_start_date': 'date',
        'billing_end_date': 'date',
        'bill_cycle_day_local': 'int',
        'events': 'list[EventSubscription]',
        'price_overrides': 'list[PhasePriceOverride]',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bundle_id': 'bundleId',
        'subscription_id': 'subscriptionId',
        'external_key': 'externalKey',
        'start_date': 'startDate',
        'product_name': 'productName',
        'product_category': 'productCategory',
        'billing_period': 'billingPeriod',
        'phase_type': 'phaseType',
        'price_list': 'priceList',
        'plan_name': 'planName',
        'state': 'state',
        'source_type': 'sourceType',
        'cancelled_date': 'cancelledDate',
        'charged_through_date': 'chargedThroughDate',
        'billing_start_date': 'billingStartDate',
        'billing_end_date': 'billingEndDate',
        'bill_cycle_day_local': 'billCycleDayLocal',
        'events': 'events',
        'price_overrides': 'priceOverrides',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, bundle_id=None, subscription_id=None, external_key=None, start_date=None, product_name=None, product_category=None, billing_period=None, phase_type=None, price_list=None, plan_name=None, state=None, source_type=None, cancelled_date=None, charged_through_date=None, billing_start_date=None, billing_end_date=None, bill_cycle_day_local=None, events=None, price_overrides=None, audit_logs=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._bundle_id = None
        self._subscription_id = None
        self._external_key = None
        self._start_date = None
        self._product_name = None
        self._product_category = None
        self._billing_period = None
        self._phase_type = None
        self._price_list = None
        self._plan_name = None
        self._state = None
        self._source_type = None
        self._cancelled_date = None
        self._charged_through_date = None
        self._billing_start_date = None
        self._billing_end_date = None
        self._bill_cycle_day_local = None
        self._events = None
        self._price_overrides = None
        self._audit_logs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if external_key is not None:
            self.external_key = external_key
        if start_date is not None:
            self.start_date = start_date
        self.product_name = product_name
        if product_category is not None:
            self.product_category = product_category
        self.billing_period = billing_period
        if phase_type is not None:
            self.phase_type = phase_type
        self.price_list = price_list
        self.plan_name = plan_name
        if state is not None:
            self.state = state
        if source_type is not None:
            self.source_type = source_type
        if cancelled_date is not None:
            self.cancelled_date = cancelled_date
        if charged_through_date is not None:
            self.charged_through_date = charged_through_date
        if billing_start_date is not None:
            self.billing_start_date = billing_start_date
        if billing_end_date is not None:
            self.billing_end_date = billing_end_date
        if bill_cycle_day_local is not None:
            self.bill_cycle_day_local = bill_cycle_day_local
        if events is not None:
            self.events = events
        if price_overrides is not None:
            self.price_overrides = price_overrides
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this Subscription.  # noqa: E501


        :return: The account_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Subscription.


        :param account_id: The account_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this Subscription.  # noqa: E501


        :return: The bundle_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this Subscription.


        :param bundle_id: The bundle_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Subscription.  # noqa: E501


        :return: The subscription_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Subscription.


        :param subscription_id: The subscription_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def external_key(self):
        """Gets the external_key of this Subscription.  # noqa: E501


        :return: The external_key of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this Subscription.


        :param external_key: The external_key of this Subscription.  # noqa: E501
        :type: str
        """

        self._external_key = external_key

    @property
    def start_date(self):
        """Gets the start_date of this Subscription.  # noqa: E501


        :return: The start_date of this Subscription.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Subscription.


        :param start_date: The start_date of this Subscription.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def product_name(self):
        """Gets the product_name of this Subscription.  # noqa: E501


        :return: The product_name of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Subscription.


        :param product_name: The product_name of this Subscription.  # noqa: E501
        :type: str
        """
        if product_name is None:
            raise ValueError("Invalid value for `product_name`, must not be `None`")  # noqa: E501

        self._product_name = product_name

    @property
    def product_category(self):
        """Gets the product_category of this Subscription.  # noqa: E501


        :return: The product_category of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this Subscription.


        :param product_category: The product_category of this Subscription.  # noqa: E501
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
    def billing_period(self):
        """Gets the billing_period of this Subscription.  # noqa: E501


        :return: The billing_period of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Subscription.


        :param billing_period: The billing_period of this Subscription.  # noqa: E501
        :type: str
        """
        if billing_period is None:
            raise ValueError("Invalid value for `billing_period`, must not be `None`")  # noqa: E501
        allowed_values = ["DAILY", "WEEKLY", "BIWEEKLY", "THIRTY_DAYS", "SIXTY_DAYS", "NINETY_DAYS", "MONTHLY", "BIMESTRIAL", "QUARTERLY", "TRIANNUAL", "BIANNUAL", "ANNUAL", "BIENNIAL", "NO_BILLING_PERIOD"]  # noqa: E501
        if billing_period not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

    @property
    def phase_type(self):
        """Gets the phase_type of this Subscription.  # noqa: E501


        :return: The phase_type of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._phase_type

    @phase_type.setter
    def phase_type(self, phase_type):
        """Sets the phase_type of this Subscription.


        :param phase_type: The phase_type of this Subscription.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRIAL", "DISCOUNT", "FIXEDTERM", "EVERGREEN"]  # noqa: E501
        if phase_type not in allowed_values:
            raise ValueError(
                "Invalid value for `phase_type` ({0}), must be one of {1}"  # noqa: E501
                .format(phase_type, allowed_values)
            )

        self._phase_type = phase_type

    @property
    def price_list(self):
        """Gets the price_list of this Subscription.  # noqa: E501


        :return: The price_list of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this Subscription.


        :param price_list: The price_list of this Subscription.  # noqa: E501
        :type: str
        """
        if price_list is None:
            raise ValueError("Invalid value for `price_list`, must not be `None`")  # noqa: E501

        self._price_list = price_list

    @property
    def plan_name(self):
        """Gets the plan_name of this Subscription.  # noqa: E501


        :return: The plan_name of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this Subscription.


        :param plan_name: The plan_name of this Subscription.  # noqa: E501
        :type: str
        """
        if plan_name is None:
            raise ValueError("Invalid value for `plan_name`, must not be `None`")  # noqa: E501

        self._plan_name = plan_name

    @property
    def state(self):
        """Gets the state of this Subscription.  # noqa: E501


        :return: The state of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Subscription.


        :param state: The state of this Subscription.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "ACTIVE", "BLOCKED", "CANCELLED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def source_type(self):
        """Gets the source_type of this Subscription.  # noqa: E501


        :return: The source_type of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this Subscription.


        :param source_type: The source_type of this Subscription.  # noqa: E501
        :type: str
        """
        allowed_values = ["NATIVE", "MIGRATED", "TRANSFERRED"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def cancelled_date(self):
        """Gets the cancelled_date of this Subscription.  # noqa: E501


        :return: The cancelled_date of this Subscription.  # noqa: E501
        :rtype: date
        """
        return self._cancelled_date

    @cancelled_date.setter
    def cancelled_date(self, cancelled_date):
        """Sets the cancelled_date of this Subscription.


        :param cancelled_date: The cancelled_date of this Subscription.  # noqa: E501
        :type: date
        """

        self._cancelled_date = cancelled_date

    @property
    def charged_through_date(self):
        """Gets the charged_through_date of this Subscription.  # noqa: E501


        :return: The charged_through_date of this Subscription.  # noqa: E501
        :rtype: date
        """
        return self._charged_through_date

    @charged_through_date.setter
    def charged_through_date(self, charged_through_date):
        """Sets the charged_through_date of this Subscription.


        :param charged_through_date: The charged_through_date of this Subscription.  # noqa: E501
        :type: date
        """

        self._charged_through_date = charged_through_date

    @property
    def billing_start_date(self):
        """Gets the billing_start_date of this Subscription.  # noqa: E501


        :return: The billing_start_date of this Subscription.  # noqa: E501
        :rtype: date
        """
        return self._billing_start_date

    @billing_start_date.setter
    def billing_start_date(self, billing_start_date):
        """Sets the billing_start_date of this Subscription.


        :param billing_start_date: The billing_start_date of this Subscription.  # noqa: E501
        :type: date
        """

        self._billing_start_date = billing_start_date

    @property
    def billing_end_date(self):
        """Gets the billing_end_date of this Subscription.  # noqa: E501


        :return: The billing_end_date of this Subscription.  # noqa: E501
        :rtype: date
        """
        return self._billing_end_date

    @billing_end_date.setter
    def billing_end_date(self, billing_end_date):
        """Sets the billing_end_date of this Subscription.


        :param billing_end_date: The billing_end_date of this Subscription.  # noqa: E501
        :type: date
        """

        self._billing_end_date = billing_end_date

    @property
    def bill_cycle_day_local(self):
        """Gets the bill_cycle_day_local of this Subscription.  # noqa: E501


        :return: The bill_cycle_day_local of this Subscription.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day_local

    @bill_cycle_day_local.setter
    def bill_cycle_day_local(self, bill_cycle_day_local):
        """Sets the bill_cycle_day_local of this Subscription.


        :param bill_cycle_day_local: The bill_cycle_day_local of this Subscription.  # noqa: E501
        :type: int
        """

        self._bill_cycle_day_local = bill_cycle_day_local

    @property
    def events(self):
        """Gets the events of this Subscription.  # noqa: E501


        :return: The events of this Subscription.  # noqa: E501
        :rtype: list[EventSubscription]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Subscription.


        :param events: The events of this Subscription.  # noqa: E501
        :type: list[EventSubscription]
        """

        self._events = events

    @property
    def price_overrides(self):
        """Gets the price_overrides of this Subscription.  # noqa: E501


        :return: The price_overrides of this Subscription.  # noqa: E501
        :rtype: list[PhasePriceOverride]
        """
        return self._price_overrides

    @price_overrides.setter
    def price_overrides(self, price_overrides):
        """Sets the price_overrides of this Subscription.


        :param price_overrides: The price_overrides of this Subscription.  # noqa: E501
        :type: list[PhasePriceOverride]
        """

        self._price_overrides = price_overrides

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Subscription.  # noqa: E501


        :return: The audit_logs of this Subscription.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Subscription.


        :param audit_logs: The audit_logs of this Subscription.  # noqa: E501
        :type: list[AuditLog]
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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
