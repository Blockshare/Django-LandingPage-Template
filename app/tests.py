from django.test import TestCase
from django.test import Client


class ViewTests(TestCase):
    def testAppView(self):
        resp = self.client.get('/app/')
        self.assertEqual(resp.status_code, 200)

    def testAddressView(self):
        resp = self.client.get('/app/address/')
        self.assertEqual(resp.status_code, 200)

    def testAddress(self):
        resp = self.client.post('/app/address/', {'address': '12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX'})
        self.assertEqual(resp.status_code, 200)

    def testAddressContent(self):
        resp = self.client.post('/app/address/', {'address': '12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX'})
        self.assertNotEqual(resp.content, '')

