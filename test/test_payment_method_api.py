# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import killbill
from api.payment_method_api import PaymentMethodApi  # noqa: E501
from killbill.rest import ApiException


class TestPaymentMethodApi(unittest.TestCase):
    """PaymentMethodApi unit test stubs"""

    def setUp(self):
        self.api = api.payment_method_api.PaymentMethodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_method_custom_fields(self):
        """Test case for create_payment_method_custom_fields

        Add custom fields to payment method  # noqa: E501
        """
        pass

    def test_delete_payment_method(self):
        """Test case for delete_payment_method

        Delete a payment method  # noqa: E501
        """
        pass

    def test_delete_payment_method_custom_fields(self):
        """Test case for delete_payment_method_custom_fields

        Remove custom fields from payment method  # noqa: E501
        """
        pass

    def test_get_payment_method(self):
        """Test case for get_payment_method

        Retrieve a payment method by id  # noqa: E501
        """
        pass

    def test_get_payment_method_by_key(self):
        """Test case for get_payment_method_by_key

        Retrieve a payment method by external key  # noqa: E501
        """
        pass

    def test_get_payment_method_custom_fields(self):
        """Test case for get_payment_method_custom_fields

        Retrieve payment method custom fields  # noqa: E501
        """
        pass

    def test_get_payment_methods(self):
        """Test case for get_payment_methods

        List payment methods  # noqa: E501
        """
        pass

    def test_modify_payment_method_custom_fields(self):
        """Test case for modify_payment_method_custom_fields

        Modify custom fields to payment method  # noqa: E501
        """
        pass

    def test_search_payment_methods(self):
        """Test case for search_payment_methods

        Search payment methods  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
