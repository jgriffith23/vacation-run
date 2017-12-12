import unittest
from server import app


class BasicTests(unittest.TestCase):
    """Test features that don't require login or database."""

    def setUp(self):
        app.config['TESTING'] = True
        app.secret_key = "ABC"
        self.client = app.test_client()

    def test_homepage(self):

        r = self.client.get("/")
        self.assertIn("Let's track our runs!", r.data)


if __name__ == "__main__":
    unittest.main()
