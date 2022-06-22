import unittest
from LinkedListFile import *
from InventoryItemFile import *

class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertual(True, False)
    def setUp(self):
        self.genericItem:InventoryItem  = InventoryItem()
        self.swordItem:InventoryItem    = InventoryItem(item_name="sword", item_type=InventoryType.MEELEE, item_power=5)
        self.wandItem:InventoryItem     = InventoryItem(item_name="wand", item_type=InventoryType.MAGIC, item_power=3)
        self.poulticeItem:InventoryItem = InventoryItem(item_name="poultice", item_type=InventoryType.HEALING, item_power=2)
        self.clubItem:InventoryItem     = InventoryItem(item_name="club", item_type=InventoryType.MEELEE, item_power=2)
        self.daggerItem:InventoryItem   = InventoryItem(item_name="dagger", item_type=InventoryType.MEELEE, item_power=3)
        self.potionItem:InventoryItem   = InventoryItem(item_name="potion", item_type=InventoryType.MAGIC, item_power=2)


    def test_a_is_empty(self):
        print("\nStart TEST A -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        self.assertTrue(l_list.is_empty())
        l_list.add_to_end(self.genericItem)
        print(f"\t{l_list}")
        self.assertFalse(l_list.is_empty())
        print("End TEST A   -----------------------------------------------------------")

    #@unittest.skip("Skipping test b. Get test a working first.")
    def test_b_add_to_end(self):
        print("\nStart TEST B -----------------------------------------------------------")

        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        self.assertEqual([],l_list.toList())
        l_list.add_to_end(self.genericItem)
        l_list.add_to_end(self.swordItem)
        print(f"\t{l_list}")
        self.assertEqual([self.genericItem, self.swordItem], l_list.toList())
        print("End TEST B   -----------------------------------------------------------")

    #@unittest.skip("Skipping test c. Get test b working first.")
    def test_c_add_to_start(self):
        print("\nStart TEST C -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_to_end(InventoryItem())
        l_list.add_to_end(InventoryItem(item_name="sword", item_type=InventoryType.MEELEE, item_power=5))
        l_list.add_to_start(InventoryItem(item_name="wand", item_type=InventoryType.MAGIC, item_power=3))
        print(f"\t{l_list}")
        self.assertEqual([self.wandItem, self.genericItem, self.swordItem],l_list.toList())
        print("End TEST C   -----------------------------------------------------------")

    #@unittest.skip("Skipping test d. Get test c working first.")
    def test_d_add_items(self):
        print("\nStart TEST D -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_to_start(self.wandItem)
        l_list.add_all_to_end([self.clubItem, self.potionItem, self.swordItem])
        print(f"\t{l_list}")
        self.assertEqual([self.wandItem, self.clubItem, self.potionItem, self.swordItem], l_list.toList())
        print("End TEST D   -----------------------------------------------------------")

    #@unittest.skip("Skipping test e. Get test d working first.")
    def test_e_len(self):
        print("\nStart TEST E -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()
        print(f"\t{l_list}")
        self.assertEqual(0, len(l_list))
        l_list.add_all_to_end([self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem])
        print(f"\t{l_list}")
        self.assertEqual(5, len(l_list))
        l_list.add_to_end([self.clubItem])
        print(f"\t{l_list}")
        self.assertEqual(6, len(l_list))
        print("End TEST E   -----------------------------------------------------------")


    #@unittest.skip("Skipping test f. Get test e working first.")
    def test_f_contains(self):
        print("\nStart TEST F -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.poulticeItem, self.clubItem, self.genericItem, self.wandItem])
        print(f"\t{l_list}")
        self.assertTrue(self.clubItem in l_list)
        self.assertTrue(self.wandItem in l_list)
        self.assertFalse(self.daggerItem in l_list)
        print("End TEST F   -----------------------------------------------------------")


    #@unittest.skip("Skipping test g. Get test f working first.")
    def test_g_index(self):
        print("\nStart TEST G -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.poulticeItem, self.clubItem, self.genericItem, self.wandItem])
        print(f"\t{l_list}")
        self.assertEqual(0, l_list.index(self.wandItem))
        self.assertEqual(2, l_list.index(self.clubItem))
        print("End TEST G   -----------------------------------------------------------")


    #@unittest.skip("Skipping test h. Get test g working first.")
    def test_h_item_at_index(self):
        print("\nStart TEST H -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        print(f"\t{l_list}")
        self.assertEqual(self.genericItem, l_list.item_at_index(0))
        self.assertEqual(self.poulticeItem, l_list.item_at_index(2))
        self.assertRaises(IndexError, l_list.item_at_index, 20)
        print("End TEST H   -----------------------------------------------------------")


    #@unittest.skip("Skipping test i. Get test h working first.")
    def test_i_item_at_start_and_end(self):
        print("\nStart TEST I -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        print(f"\t{l_list}")
        self.assertEqual(self.genericItem, l_list.item_at_start())
        self.assertEqual(self.swordItem, l_list.item_at_end())
        print("End TEST I   -----------------------------------------------------------")


    #@unittest.skip("Skipping test j. Get test i working first.")
    def test_j_insert_item_at_start(self):
        print("\nStart TEST J -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        l_list.insert_value_at_start(self.clubItem)
        print(f"\t{l_list}")
        self.assertEqual(self.clubItem, l_list.item_at_start())
        self.assertEqual(self.genericItem, l_list.item_at_index(1))
        self.assertEqual(self.wandItem, l_list.item_at_index(2))
        self.assertEqual(7, len(l_list))
        l_list = LinkedList()
        l_list.insert_value_at_start(self.clubItem)
        print(f"\t{l_list}")
        self.assertEqual(self.clubItem, l_list.item_at_start())
        self.assertEqual(1, len(l_list))
        print("End TEST J   -----------------------------------------------------------")


    #@unittest.skip("Skipping test k. Get test j working first.")
    def test_k_insert_value_at_index(self):
        print("\nStart TEST K -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        l_list.insert_value_at_index(self.clubItem, 3)
        print(f"\t{l_list}")
        self.assertEqual(7, len(l_list))
        self.assertEqual(self.clubItem, l_list.item_at_index(3))
        self.assertEqual(self.potionItem, l_list.item_at_index(4))
        print("End TEST K   -----------------------------------------------------------")


    #@unittest.skip("Skipping test l. Get test k working first.")
    def test_l_insert_all(self):
        print("\nStart TEST L -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.clubItem, self.potionItem])
        l_list.insert_all_at_index([self.swordItem, self.poulticeItem, self.genericItem], 1)
        print(f"\t{l_list}")
        self.assertEqual([self.wandItem, self.swordItem, self.poulticeItem, self.genericItem, \
                                         self.clubItem, self.potionItem], l_list.toList())

        l_list.insert_all_at_index([self.wandItem, self.potionItem], 0)
        self.assertEqual([self.wandItem, self.potionItem, self.wandItem, self.swordItem, \
                                         self.poulticeItem, self.genericItem, self.clubItem, self.potionItem], l_list.toList() )

        l_list.insert_all_at_index([self.wandItem], 8)
        self.assertEqual([self.wandItem, self.potionItem, self.wandItem, self.swordItem, \
                                         self.poulticeItem, self.genericItem, self.clubItem, self.potionItem, \
                                         self.wandItem], l_list.toList())

        self.assertRaises(IndexError, l_list.insert_all_at_index, [self.genericItem, self.genericItem], 12)
        print("End TEST L   -----------------------------------------------------------")


    #@unittest.skip("Skipping test m. Get test l working first.")
    def test_m_remove_first_and_last(self):
        print("\nStart TEST M -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.genericItem, self.wandItem, self.potionItem, self.daggerItem])
        l_list.remove_first_item()
        print(f"\t{l_list}")
        self.assertEqual(3, len(l_list))
        self.assertEqual([self.wandItem, self.potionItem, self.daggerItem], l_list.toList())
        l_list.remove_last_item()
        print(f"\t{l_list}")
        self.assertEqual(2, len(l_list))
        self.assertEqual([self.wandItem, self.potionItem], l_list.toList())
        print("End TEST M   -----------------------------------------------------------")


    #@unittest.skip("Skipping test n. Get test m working first.")
    def test_n_remove_from_middle(self):
        print("\nStart TEST N -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.potionItem, self.swordItem, self.clubItem, self.potionItem, self.poulticeItem])
        print(f"\t{l_list}")
        l_list.remove_item_at_index(2)
        print(f"\t{l_list}")
        self.assertEqual(4, len(l_list))
        self.assertEqual([self.potionItem, self.swordItem, self.potionItem, self.poulticeItem], l_list.toList())

        l_list.remove_item_at_index(0)
        print(f"\t{l_list}")
        self.assertEqual(3, len(l_list))
        self.assertEqual([self.swordItem, self.potionItem, self.poulticeItem], l_list.toList())

        l_list.remove_item_at_index(2)
        print(f"\t{l_list}")
        self.assertEqual(2, len(l_list))
        self.assertEqual([self.swordItem, self.potionItem], l_list.toList())
        print("End TEST N   -----------------------------------------------------------")


    #@unittest.skip("Skipping test o. Get test n working first.")
    def test_o_contains(self):
        print("\nStart TEST O -----------------------------------------------------------")
        # Note the syntax "a in b" automatically calls "b.__contains__(a)"
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.clubItem, self.swordItem, self.genericItem])
        print(f"\t{l_list}")
        self.assertTrue(self.swordItem in l_list)
        self.assertTrue(self.clubItem in l_list)
        self.assertTrue(self.genericItem in l_list)
        self.assertFalse(self.poulticeItem in l_list)
        print("End TEST O   -----------------------------------------------------------")


    #@unittest.skip("Skipping test p. Get test o working first.")
    def test_p_remove_item(self):
        print("\nStart TEST P -----------------------------------------------------------")
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.swordItem, self.clubItem, self.wandItem, self.clubItem, self.poulticeItem, \
                             self.swordItem, self.daggerItem, self.wandItem, self.clubItem])
        print(f"\t{l_list}")
        l_list.remove(self.clubItem)
        print(f"\t{l_list}")
        self.assertEqual(6, len(l_list))
        self.assertEqual([self.swordItem, self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem,
                          self.wandItem], l_list.toList())

        l_list.remove(self.swordItem, first_only=True)
        print(f"\t{l_list}")
        self.assertEqual(5, len(l_list))
        self.assertEqual([self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem, self.wandItem],
                         l_list.toList())

        l_list.remove(self.genericItem)
        print(f"\t{l_list}")
        self.assertEqual(5, len(l_list))
        self.assertEqual([self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem, self.wandItem],
                         l_list.toList())
        print("End TEST P   -----------------------------------------------------------")



    #@unittest.skip("Skipping test q. Get test p working first.")
    def test_q_other_list_types(self):
        print("\nStart TEST Q -----------------------------------------------------------")
        l_list:LinkedList[int] = LinkedList[int]()

        l_list.add_to_end(12)
        l_list.add_to_end(18)
        l_list.add_to_start(6)
        print(f"\t{l_list}")
        self.assertEqual([6, 12, 18],l_list.toList())

        l_list2:LinkedList[str] = LinkedList[str]()

        l_list2.add_to_start("first")
        items = ("second","third","fourth")
        l_list2.add_all_to_end(items)
        l_list2.add_to_end("fifth")
        print(l_list2)
        self.assertEqual(["first", "second", "third", "fourth", "fifth"], l_list2.toList() )
        print("End TEST Q   -----------------------------------------------------------")

if __name__ == '__main__':
    unittest.main()
