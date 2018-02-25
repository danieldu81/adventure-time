import unittest
import inventory

class Test_Inventory(unittest.TestCase):
    def setUp(self):
        # set up Inventory instances to test length and weight restrictions
        self.inv = inventory.Inventory()
        self.inv_len = inventory.Inventory(max_len=3)
        self.inv_wt = inventory.Inventory(max_weight=7)

        # set up Item objects for use
        self.generic1 = inventory.Item('item1')
        self.generic2 = inventory.Item('item2')
        self.generic3 = inventory.Item('item3')
        self.generic4 = inventory.Item('item4')
        self.light = inventory.Item('light', weight=1)
        self.medium = inventory.Item('medium', weight=4)
        self.heavy = inventory.Item('heavy', weight=8)

    def test_pick(self):
        # basic picking up of one item
        pick = self.inv.pick_item(self.generic1)
        self.assertEqual(pick, 1)

    def test_drop(self):
        # basic dropping of one item
        self.inv.pick_item(self.generic1)
        drop = self.inv.drop_item(0)
        self.assertEqual(drop, self.generic1)

    def test_drop_null(self):
        # dropping invalid item should return NULL
        drop = self.inv.drop_item(0)
        self.assertEqual(drop, inventory.NULL)

    def test_pick_length(self):
        # picking up items under the length restriction should be fine
        pick1 = self.inv_len.pick_item(self.generic1)
        pick2 = self.inv_len.pick_item(self.generic2)
        pick3 = self.inv_len.pick_item(self.generic3)
        self.assertEqual(pick1, 1)
        self.assertEqual(pick2, 1)
        self.assertEqual(pick3, 1)

        # picking up items once we've reached the length should fail
        pick4 = self.inv_len.pick_item(self.generic4)
        self.assertEqual(pick4, -1)

if __name__ == '__main__':
    unittest.main()
