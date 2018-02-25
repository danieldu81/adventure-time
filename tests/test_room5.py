import unittest
import inventory
import Room5

class Test_Room5(unittest.TestCase):
    def setUp(self):
        # set up some weights to test with
        # wt[0] => 0 kg weight, wt[1] => 1 kg weight, etc.
        self.wt = []
        for i in range(0, 10):
            name = str(i)+' kg'
            self.wt += [inventory.Item(name, weight=i)]

    def test_solve_atwood_empty(self):
        # test the atwood solving function
        # should fail when machine is partially empty
        Room5.atw_mcn.pick_item(self.wt[1])
        Room5.solve_machine()
        self.assertEqual(Room5.win, False)

    def test_solve_atwood_wrong(self):
        # when the masses are wrong, the machine should fail
        Room5.atw_mcn.drop_item(0)
        for i in range(0, 5):
            Room5.atw_mcn.pick_item(self.wt[1])
        Room5.solve_machine()
        self.assertEqual(Room5.win, False)

    def test_solve_atwood_right(self):
        # when the masses are the correct powers of two, it should work
        for i in range(0, 5):
            Room5.atw_mcn.drop_item(0)
        Room5.atw_mcn.pick_item(self.wt[8])
        Room5.atw_mcn.pick_item(self.wt[4])
        Room5.atw_mcn.pick_item(self.wt[1])
        Room5.atw_mcn.pick_item(self.wt[1])
        Room5.atw_mcn.pick_item(self.wt[2])
        Room5.solve_machine()
        self.assertEqual(Room5.win, True)
        Room5.win = False  # reset for further tests

if __name__ == '__main__':
    unittest.main()
