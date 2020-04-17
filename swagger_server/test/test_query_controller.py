# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.test_query import TestQuery  # noqa: E501
from swagger_server.models.user_query import UserQuery  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQueryController(BaseTestCase):
    """QueryController integration test stubs"""

    def test_execute_query(self):
        """Test case for execute_query

        Queries for executing code
        """
        body = UserQuery()
        response = self.client.open(
            '/query',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_test_query(self):
        """Test case for test_query

        Queries for executing code
        """
        body = TestQuery()
        response = self.client.open(
            '/testquery',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
