# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import time
import unittest

from environment import HOST, API_TOKEN
from purity_fb import *
from utils import *


class TestArraysApi(unittest.TestCase):
    """ ArraysApi unit test stubs """

    def setUp(self):
        self.purity_fb = PurityFb(HOST)
        self.purity_fb.disable_verify_ssl()
        res = self.purity_fb.login(API_TOKEN)
        self.assertTrue(res == 200)
        self.arrays = self.purity_fb.arrays
        self.current = int(time.time() * 1000)

    def tearDown(self):
        self.purity_fb.logout()

    def test_list_arrays_http_specific_performance(self):
        """
        Test case for list_arrays_http_specific_performance
        """
        print('LIST HTTP specific performance\n')
        res = self.arrays.list_arrays_http_specific_performance()
        if DEBUG:
            print_list(res.items)
        check_is_list_of(res.items, ArrayHttpPerformance)
        res = self.arrays.list_arrays_http_specific_performance(
            end_time=self.current, resolution=30000
        )
        check_is_list_of(res.items, ArrayHttpPerformance)

    def test_list_arrays_performance(self):
        """
        Test case for list_arrays_performance
        """
        print('LIST array performance\n')
        res = self.arrays.list_arrays_performance()
        if DEBUG:
            print_list(res.items)
        check_is_list_of(res.items, ArrayPerformance)
        res = self.arrays.list_arrays_performance(
            end_time=self.current, resolution=30000
        )
        check_is_list_of(res.items, ArrayPerformance)

    def test_list_arrays_s3_specific_performance(self):
        """
        Test case for list_arrays_s3_specific_performance
        """
        print('LIST S3 specific performance\n')
        res = self.arrays.list_arrays_s3_specific_performance()
        if DEBUG:
            print_list(res.items)
        check_is_list_of(res.items, ArrayS3Performance)
        res = self.arrays.list_arrays_s3_specific_performance(
            end_time=self.current, resolution=30000
        )
        check_is_list_of(res.items, ArrayS3Performance)

    def test_list_arrays_space(self):
        """
        Test case for list_arrays_space
        """
        print('LIST array space\n')
        res = self.arrays.list_arrays_space()
        if DEBUG:
            print_list(res.items)
        check_is_list_of(res.items, ArraySpace)
        res = self.arrays.list_arrays_space(
            end_time=self.current, resolution=30000
        )
        check_is_list_of(res.items, ArraySpace)
        res = self.arrays.list_arrays_space(
            end_time=self.current, resolution=30000,
            type='file-system'
        )
        check_is_list_of(res.items, ArraySpace)


if __name__ == '__main__':
    unittest.main()
