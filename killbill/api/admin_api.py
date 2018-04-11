# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class AdminApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def invalidates_cache(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates the given Cache if specified, otherwise invalidates all caches  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param str cache_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.invalidates_cache_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def invalidates_cache_with_http_info(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates the given Cache if specified, otherwise invalidates all caches  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache_with_http_info(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param str cache_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_killbill_api_key', 'x_killbill_api_secret', 'cache_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `invalidates_cache`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `invalidates_cache`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cache_name' in params:
            query_params.append(('cacheName', params['cache_name']))  # noqa: E501

        header_params = {}
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidates_cache_by_account(self, account_id, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates Caches per account level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache_by_account(account_id, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.invalidates_cache_by_account_with_http_info(account_id, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_by_account_with_http_info(account_id, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def invalidates_cache_by_account_with_http_info(self, account_id, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates Caches per account level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache_by_account_with_http_info(account_id, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'x_killbill_api_key', 'x_killbill_api_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache_by_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `invalidates_cache_by_account`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `invalidates_cache_by_account`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `invalidates_cache_by_account`")  # noqa: E501

        if 'account_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['account_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `account_id` when calling `invalidates_cache_by_account`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache/accounts/{accountId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidates_cache_by_tenant(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates Caches per tenant level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache_by_tenant(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.invalidates_cache_by_tenant_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_by_tenant_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def invalidates_cache_by_tenant_with_http_info(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Invalidates Caches per tenant level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.invalidates_cache_by_tenant_with_http_info(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_killbill_api_key', 'x_killbill_api_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache_by_tenant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `invalidates_cache_by_tenant`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `invalidates_cache_by_tenant`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache/tenants', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_in_rotation(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Put the host back into rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_in_rotation(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_in_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.put_in_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def put_in_rotation_with_http_info(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Put the host back into rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_in_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_killbill_api_key', 'x_killbill_api_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_in_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `put_in_rotation`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `put_in_rotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/healthcheck', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_out_of_rotation(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Put the host out of rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_out_of_rotation(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_out_of_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.put_out_of_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def put_out_of_rotation_with_http_info(self, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Put the host out of rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_out_of_rotation_with_http_info(x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_killbill_api_key', 'x_killbill_api_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_out_of_rotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `put_out_of_rotation`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `put_out_of_rotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/healthcheck', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trigger_invoice_generation_for_parked_accounts(self, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Trigger an invoice generation for all parked accounts  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_invoice_generation_for_parked_accounts(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_created_by: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param int offset:
        :param int limit:
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trigger_invoice_generation_for_parked_accounts_with_http_info(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_invoice_generation_for_parked_accounts_with_http_info(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def trigger_invoice_generation_for_parked_accounts_with_http_info(self, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Trigger an invoice generation for all parked accounts  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_invoice_generation_for_parked_accounts_with_http_info(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_killbill_created_by: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param int offset:
        :param int limit:
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_killbill_created_by', 'x_killbill_api_key', 'x_killbill_api_secret', 'offset', 'limit', 'x_killbill_reason', 'x_killbill_comment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_invoice_generation_for_parked_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_killbill_created_by' is set
        if ('x_killbill_created_by' not in params or
                params['x_killbill_created_by'] is None):
            raise ValueError("Missing the required parameter `x_killbill_created_by` when calling `trigger_invoice_generation_for_parked_accounts`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `trigger_invoice_generation_for_parked_accounts`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `trigger_invoice_generation_for_parked_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'x_killbill_created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['x_killbill_created_by']  # noqa: E501
        if 'x_killbill_reason' in params:
            header_params['X-Killbill-Reason'] = params['x_killbill_reason']  # noqa: E501
        if 'x_killbill_comment' in params:
            header_params['X-Killbill-Comment'] = params['x_killbill_comment']  # noqa: E501
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/invoices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_transaction_state(self, payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Update existing paymentTransaction and associated payment state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_payment_transaction_state(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_id: (required)
        :param str payment_transaction_id: (required)
        :param AdminPayment body: (required)
        :param str x_killbill_created_by: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs)  # noqa: E501
            return data

    def update_payment_transaction_state_with_http_info(self, payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, **kwargs):  # noqa: E501
        """Update existing paymentTransaction and associated payment state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_id: (required)
        :param str payment_transaction_id: (required)
        :param AdminPayment body: (required)
        :param str x_killbill_created_by: (required)
        :param str x_killbill_api_key: (required)
        :param str x_killbill_api_secret: (required)
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'payment_transaction_id', 'body', 'x_killbill_created_by', 'x_killbill_api_key', 'x_killbill_api_secret', 'x_killbill_reason', 'x_killbill_comment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_transaction_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'payment_transaction_id' is set
        if ('payment_transaction_id' not in params or
                params['payment_transaction_id'] is None):
            raise ValueError("Missing the required parameter `payment_transaction_id` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'x_killbill_created_by' is set
        if ('x_killbill_created_by' not in params or
                params['x_killbill_created_by'] is None):
            raise ValueError("Missing the required parameter `x_killbill_created_by` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_key' is set
        if ('x_killbill_api_key' not in params or
                params['x_killbill_api_key'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_key` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'x_killbill_api_secret' is set
        if ('x_killbill_api_secret' not in params or
                params['x_killbill_api_secret'] is None):
            raise ValueError("Missing the required parameter `x_killbill_api_secret` when calling `update_payment_transaction_state`")  # noqa: E501

        if 'payment_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['payment_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `payment_id` when calling `update_payment_transaction_state`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        if 'payment_transaction_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['payment_transaction_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `payment_transaction_id` when calling `update_payment_transaction_state`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501
        if 'payment_transaction_id' in params:
            path_params['paymentTransactionId'] = params['payment_transaction_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_killbill_created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['x_killbill_created_by']  # noqa: E501
        if 'x_killbill_reason' in params:
            header_params['X-Killbill-Reason'] = params['x_killbill_reason']  # noqa: E501
        if 'x_killbill_comment' in params:
            header_params['X-Killbill-Comment'] = params['x_killbill_comment']  # noqa: E501
        if 'x_killbill_api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['x_killbill_api_key']  # noqa: E501
        if 'x_killbill_api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['x_killbill_api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/payments/{paymentId}/transactions/{paymentTransactionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
