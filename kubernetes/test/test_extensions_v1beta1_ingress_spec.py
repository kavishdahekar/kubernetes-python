# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.extensions_v1beta1_ingress_spec import ExtensionsV1beta1IngressSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1IngressSpec(unittest.TestCase):
    """ExtensionsV1beta1IngressSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1IngressSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_ingress_spec.ExtensionsV1beta1IngressSpec()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1IngressSpec(
                backend = kubernetes.client.models.extensions/v1beta1/ingress_backend.extensions.v1beta1.IngressBackend(
                    service_name = '0', 
                    service_port = kubernetes.client.models.service_port.servicePort(), ), 
                rules = [
                    kubernetes.client.models.extensions/v1beta1/ingress_rule.extensions.v1beta1.IngressRule(
                        host = '0', 
                        http = kubernetes.client.models.extensions/v1beta1/http_ingress_rule_value.extensions.v1beta1.HTTPIngressRuleValue(
                            paths = [
                                kubernetes.client.models.extensions/v1beta1/http_ingress_path.extensions.v1beta1.HTTPIngressPath(
                                    backend = kubernetes.client.models.extensions/v1beta1/ingress_backend.extensions.v1beta1.IngressBackend(
                                        service_name = '0', 
                                        service_port = kubernetes.client.models.service_port.servicePort(), ), 
                                    path = '0', )
                                ], ), )
                    ], 
                tls = [
                    kubernetes.client.models.extensions/v1beta1/ingress_tls.extensions.v1beta1.IngressTLS(
                        hosts = [
                            '0'
                            ], 
                        secret_name = '0', )
                    ]
            )
        else :
            return ExtensionsV1beta1IngressSpec(
        )

    def testExtensionsV1beta1IngressSpec(self):
        """Test ExtensionsV1beta1IngressSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
