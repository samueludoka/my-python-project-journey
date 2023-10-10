from unittest import TestCase

from chapter_4_exercises import credit_card


class Test(TestCase):
    def test_creditcard_number_is_valid(self):
        cardNumber = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "0", "2", "6", "2", "6"];
        result = [credit_card.creditcardNumber(cardNumber)]
        answer = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "0", "2", "6", "2", "6"]
        self.assertEqual(answer, result)

    def test_card_validity(self):
        cardNumber = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "0", "2", "6", "2", "6"];
        answer = True
        result = [credit_card.cardValidate(cardNumber)]
        self.assertEqual(answer, result)


