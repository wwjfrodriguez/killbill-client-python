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
from api.tag_api import TagApi  # noqa: E501
from killbill.rest import ApiException


class TestTagApi(unittest.TestCase):
    """TagApi unit test stubs"""

    def setUp(self):
        self.api = api.tag_api.TagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_tags(self):
        """Test case for get_tags

        List tags  # noqa: E501
        """
        pass

    def test_search_tags(self):
        """Test case for search_tags

        Search tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
