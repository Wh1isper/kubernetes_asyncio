# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.27.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.well_known_api import WellKnownApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestWellKnownApi(unittest.TestCase):
    """WellKnownApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.well_known_api.WellKnownApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_service_account_issuer_open_id_configuration(self):
        """Test case for get_service_account_issuer_open_id_configuration

        """
        pass


if __name__ == '__main__':
    unittest.main()
