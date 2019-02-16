# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.6), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
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


class QuotasGroupsApi(object):
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

    def create_group_quotas(self, **kwargs):
        """
        Create a new group quota
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_group_quotas(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :param QuotasGroup quota:
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_group_quotas_with_http_info(**kwargs)
        else:
            (data) = self.create_group_quotas_with_http_info(**kwargs)
            return data

    def create_group_quotas_with_http_info(self, **kwargs):
        """
        Create a new group quota
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_group_quotas_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :param QuotasGroup quota:
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_system_names', 'gids', 'group_names', 'quota']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group_quotas" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'gids' in params:
            query_params.append(('gids', params['gids']))
            collection_formats['gids'] = 'csv'
        if 'group_names' in params:
            query_params.append(('group_names', params['group_names']))
            collection_formats['group_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota' in params:
            body_params = params['quota']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/quotas/groups', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='QuotasGroupResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_group_quotas(self, **kwargs):
        """
        Delete
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_group_quotas(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_group_quotas_with_http_info(**kwargs)
        else:
            (data) = self.delete_group_quotas_with_http_info(**kwargs)
            return data

    def delete_group_quotas_with_http_info(self, **kwargs):
        """
        Delete
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_group_quotas_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'file_system_names', 'gids', 'group_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group_quotas" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'gids' in params:
            query_params.append(('gids', params['gids']))
            collection_formats['gids'] = 'csv'
        if 'group_names' in params:
            query_params.append(('group_names', params['group_names']))
            collection_formats['group_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/quotas/groups', 'DELETE',
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

    def list_group_quotas(self, **kwargs):
        """
        A list of quota group entries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_group_quotas(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_group_quotas_with_http_info(**kwargs)
        else:
            (data) = self.list_group_quotas_with_http_info(**kwargs)
            return data

    def list_group_quotas_with_http_info(self, **kwargs):
        """
        A list of quota group entries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_group_quotas_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'filter', 'limit', 'sort', 'start', 'token', 'file_system_names', 'gids', 'group_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_group_quotas" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'gids' in params:
            query_params.append(('gids', params['gids']))
            collection_formats['gids'] = 'csv'
        if 'group_names' in params:
            query_params.append(('group_names', params['group_names']))
            collection_formats['group_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/quotas/groups', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='QuotasGroupResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_group_quotas(self, **kwargs):
        """
        Update existing group quotas
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_group_quotas(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :param QuotasGroup quota:
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_group_quotas_with_http_info(**kwargs)
        else:
            (data) = self.update_group_quotas_with_http_info(**kwargs)
            return data

    def update_group_quotas_with_http_info(self, **kwargs):
        """
        Update existing group quotas
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_group_quotas_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param list[str] file_system_names: A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned.
        :param list[str] gids: A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter.
        :param list[str] group_names: A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter.
        :param QuotasGroup quota:
        :return: QuotasGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'file_system_names', 'gids', 'group_names', 'quota']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group_quotas" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'gids' in params:
            query_params.append(('gids', params['gids']))
            collection_formats['gids'] = 'csv'
        if 'group_names' in params:
            query_params.append(('group_names', params['group_names']))
            collection_formats['group_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota' in params:
            body_params = params['quota']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/quotas/groups', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='QuotasGroupResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
