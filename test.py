import unittest
from app import Assets

class TestAssets(unittest.TestCase):
    def setUp(self):
        self.assets = Assets()
        self.user = "test_user"

    def test_add_asset(self):
        self.assets.add_asset(self.user, 1, "Laptop", 1000)
        self.assertIn(1, self.assets.assets)
        self.assertEqual(self.assets.assets[1]['name'], "Laptop")
        self.assertEqual(self.assets.assets[1]['value'], 1000)

    def test_remove_asset(self):
        self.assets.add_asset(self.user, 1, "Laptop", 1000)
        self.assets.remove_asset(self.user, 1)
        self.assertNotIn(1, self.assets.assets)

    def test_total_assets_value(self):
        self.assets.add_asset(self.user, 1, "Laptop", 1000)
        self.assets.add_asset(self.user, 2, "Projector", 500)
        total_value = self.assets.total_assets_value()
        self.assertEqual(total_value, 1500)

    def test_remove_nonexistent_asset(self):
        self.assets.add_asset(self.user, 1, "Laptop", 1000)
        self.assets.remove_asset(self.user, 2)  # Attempt to remove an asset that doesn't exist
        self.assertIn(1, self.assets.assets)  # Original asset should still be there

if __name__ == '__main__':
    unittest.main()
