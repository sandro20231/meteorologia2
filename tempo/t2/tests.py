from django.test import TestCase, Client
import unittest

# Create your tests here.


class TestesT2(TestCase):

    def test_index(self):
        """Testando se index.html está abrindo"""
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
