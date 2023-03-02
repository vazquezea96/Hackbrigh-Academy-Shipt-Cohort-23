import unittest
import further_study


class FurtherStudyTests(unittest.TestCase):
    """Tests for list slicing further study."""


    def test_concatenate_new_value(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        result = further_study.concatenate_new_value(months, 'Jul')
        self.assertEqual(result, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'])
    

    def test_pig_latin(self):
        self.assertEqual(further_study.pig_latin('porcupines'), 'orcupinespay')
        self.assertEqual(further_study.pig_latin('apple'), 'appleyay')


    def test_replace_middle(self):
        multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        further_study.replace_middle(multiples)
        self.assertEqual(multiples, [0, 3, 42, 37, 24, 27])


    def test_delete_middle(self):
        notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        further_study.delete_middle(notes)
        self.assertEqual(notes, ['Do', 'Re', 'Ti', 'Do'])
    

    def test_double_with_list_comprehension(self):
        result = further_study.double_with_list_comprehension([1, 2, 3, 4, 5])
        self.assertEqual(result, [2, 4, 6, 8, 10])
    

    def test_multiplication_table(self):
        result = further_study.multiplication_table(3)
        self.assertEqual(result, [[1, 2, 3], [2, 4, 6], [3, 6, 9]])


if __name__ == "__main__":
    unittest.main()