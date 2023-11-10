import unittest


class Account(unittest.TestCase):
    def test_deposit_money(self):
        abigailAccount = Account()
        self.assertEqual(0, abigailAccount.get_balance())
        abigailAccount.deposit(3000)
        self.assertEqual(3000, abigailAccount.get_balance())
