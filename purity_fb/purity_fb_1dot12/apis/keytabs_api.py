# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.12 Python SDK

    Pure Storage FlashBlade REST 1.12 Python SDK. Compatible with REST API versions 1.0 - 1.12. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.12
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class KeytabsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_keytabs(self, keytab, **kwargs):
        """
        Create new keytabs by non-disruptively rotating the current set of keytabs for the configured Active Directory account that has been specified.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_keytabs(keytab, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KeytabPost keytab: (required)
        :param list[str] name_prefixes: The prefix to use for the names of all kerberos keytab entry objects that are being created.
        :return: KeytabResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_keytabs_with_http_info(keytab, **kwargs)
        else:
            (data) = self.create_keytabs_with_http_info(keytab, **kwargs)
            return data

    def create_keytabs_with_http_info(self, keytab, **kwargs):
        """
        Create new keytabs by non-disruptively rotating the current set of keytabs for the configured Active Directory account that has been specified.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_keytabs_with_http_info(keytab, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KeytabPost keytab: (required)
        :param list[str] name_prefixes: The prefix to use for the names of all kerberos keytab entry objects that are being created.
        :return: KeytabResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keytab', 'name_prefixes']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_keytabs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keytab' is set
        if ('keytab' not in params) or (params['keytab'] is None):
            raise ValueError("Missing the required parameter `keytab` when calling `create_keytabs`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name_prefixes' in params:
            query_params.append(('name_prefixes', params['name_prefixes']))
            collection_formats['name_prefixes'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'keytab' in params:
            body_params = params['keytab']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/1.12/keytabs', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KeytabResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_keytabs(self, **kwargs):
        """
        Delete a keytab.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_keytabs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_keytabs_with_http_info(**kwargs)
        else:
            (data) = self.delete_keytabs_with_http_info(**kwargs)
            return data

    def delete_keytabs_with_http_info(self, **kwargs):
        """
        Delete a keytab.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_keytabs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_keytabs" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.12/keytabs', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def download_keytab_file(self, **kwargs):
        """
        Download a keytab file.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_keytab_file(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] keytab_ids: A comma-separated list of keytab ids. This cannot be provided together with the keytab names query parameters.
        :param list[str] keytab_names: A comma-separated list of keytab names. This cannot be provided together with the keytab ids query parameters.
        :return: KeytabDownloadUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.download_keytab_file_with_http_info(**kwargs)
        else:
            (data) = self.download_keytab_file_with_http_info(**kwargs)
            return data

    def download_keytab_file_with_http_info(self, **kwargs):
        """
        Download a keytab file.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_keytab_file_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] keytab_ids: A comma-separated list of keytab ids. This cannot be provided together with the keytab names query parameters.
        :param list[str] keytab_names: A comma-separated list of keytab names. This cannot be provided together with the keytab ids query parameters.
        :return: KeytabDownloadUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keytab_ids', 'keytab_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_keytab_file" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keytab_ids' in params:
            query_params.append(('keytab_ids', params['keytab_ids']))
            collection_formats['keytab_ids'] = 'csv'
        if 'keytab_names' in params:
            query_params.append(('keytab_names', params['keytab_names']))
            collection_formats['keytab_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream', 'text/plain', 'application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.12/keytabs/download', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KeytabDownloadUploadResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_keytabs(self, **kwargs):
        """
        List keytabs.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_keytabs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param str sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name).
        :param int start: The offset of the first resource to return from a collection.
        :param str token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :return: KeytabResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_keytabs_with_http_info(**kwargs)
        else:
            (data) = self.list_keytabs_with_http_info(**kwargs)
            return data

    def list_keytabs_with_http_info(self, **kwargs):
        """
        List keytabs.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_keytabs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param int limit: limit, should be >= 0
        :param list[str] names: A comma-separated list of resource names. This cannot be provided together with the ids query parameters.
        :param str sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name).
        :param int start: The offset of the first resource to return from a collection.
        :param str token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :return: KeytabResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'ids', 'limit', 'names', 'sort', 'start', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_keytabs" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.12/keytabs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KeytabResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def upload_keytab_file(self, keytab_file, **kwargs):
        """
        Upload a keytab file.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_keytab_file(keytab_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str keytab_file: The attribute map containing the data of the file of keytabs being imported. (required)
        :param list[str] name_prefixes: The prefix to use for the names of all kerberos keytab entry objects that are being created.
        :return: KeytabDownloadUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_keytab_file_with_http_info(keytab_file, **kwargs)
        else:
            (data) = self.upload_keytab_file_with_http_info(keytab_file, **kwargs)
            return data

    def upload_keytab_file_with_http_info(self, keytab_file, **kwargs):
        """
        Upload a keytab file.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_keytab_file_with_http_info(keytab_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str keytab_file: The attribute map containing the data of the file of keytabs being imported. (required)
        :param list[str] name_prefixes: The prefix to use for the names of all kerberos keytab entry objects that are being created.
        :return: KeytabDownloadUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keytab_file', 'name_prefixes']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_keytab_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keytab_file' is set
        if ('keytab_file' not in params) or (params['keytab_file'] is None):
            raise ValueError("Missing the required parameter `keytab_file` when calling `upload_keytab_file`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name_prefixes' in params:
            query_params.append(('name_prefixes', params['name_prefixes']))
            collection_formats['name_prefixes'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'keytab_file' in params:
            form_params.append(('keytab_file', params['keytab_file']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream', 'text/plain', 'application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.12/keytabs/upload', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KeytabDownloadUploadResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
