# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user_modi import UserModi  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserModiController(BaseTestCase):
    """UserModiController integration test stubs"""

    def test_modify_user(self):
        """Test case for modify_user

        Modify user
        """
        body = UserModi()
        response = self.client.open(
            '/User/{UserName}'.format(UserName='UserName_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
