import unittest
from server import app


class BasicTests(unittest.TestCase):
    """Test features that don't require login or database."""

    def setUp(self):
        app.config['TESTING'] = True
        app.secret_key = "ABC"
        self.client = app.test_client()

    def test_homepage(self):
        """Any user should be able to see the homepage."""

        r = self.client.get("/")
        self.assertIn("Vacation Run", r.data)


if __name__ == "__main__":
    unittest.main()
