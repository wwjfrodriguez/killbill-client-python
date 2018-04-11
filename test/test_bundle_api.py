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
from api.bundle_api import BundleApi  # noqa: E501
from killbill.rest import ApiException


class TestBundleApi(unittest.TestCase):
    """BundleApi unit test stubs"""

    def setUp(self):
        self.api = api.bundle_api.BundleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_bundle_blocking_state(self):
        """Test case for add_bundle_blocking_state

        Block a bundle  # noqa: E501
        """
        pass

    def test_create_bundle_custom_fields(self):
        """Test case for create_bundle_custom_fields

        Add custom fields to bundle  # noqa: E501
        """
        pass

    def test_create_bundle_tags(self):
        """Test case for create_bundle_tags

        Add tags to bundle  # noqa: E501
        """
        pass

    def test_delete_bundle_custom_fields(self):
        """Test case for delete_bundle_custom_fields

        Remove custom fields from bundle  # noqa: E501
        """
        pass

    def test_delete_bundle_tags(self):
        """Test case for delete_bundle_tags

        Remove tags from bundle  # noqa: E501
        """
        pass

    def test_get_bundle(self):
        """Test case for get_bundle

        Retrieve a bundle by id  # noqa: E501
        """
        pass

    def test_get_bundle_by_key(self):
        """Test case for get_bundle_by_key

        Retrieve a bundle by external key  # noqa: E501
        """
        pass

    def test_get_bundle_custom_fields(self):
        """Test case for get_bundle_custom_fields

        Retrieve bundle custom fields  # noqa: E501
        """
        pass

    def test_get_bundle_tags(self):
        """Test case for get_bundle_tags

        Retrieve bundle tags  # noqa: E501
        """
        pass

    def test_get_bundles(self):
        """Test case for get_bundles

        List bundles  # noqa: E501
        """
        pass

    def test_modify_bundle_custom_fields(self):
        """Test case for modify_bundle_custom_fields

        Modify custom fields to bundle  # noqa: E501
        """
        pass

    def test_pause_bundle(self):
        """Test case for pause_bundle

        Pause a bundle  # noqa: E501
        """
        pass

    def test_rename_external_key(self):
        """Test case for rename_external_key

        Update a bundle externalKey  # noqa: E501
        """
        pass

    def test_resume_bundle(self):
        """Test case for resume_bundle

        Resume a bundle  # noqa: E501
        """
        pass

    def test_search_bundles(self):
        """Test case for search_bundles

        Search bundles  # noqa: E501
        """
        pass

    def test_transfer_bundle(self):
        """Test case for transfer_bundle

        Transfer a bundle to another account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
