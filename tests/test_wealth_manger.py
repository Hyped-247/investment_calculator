import unittest
from wealth_manger import Calculator

"""
In this file there are four test classes: TestingValueSmall, TestingValueMedium, and TestingValueLarge. 
Each class is going to test different features of the program to make sure that it is working correctly. 

The TestingValueSmall class is going to make sure that there are no bugs when the yearly savings is lower than
how much each apt cost. 

The TestingValueMedium class is going to make sure that there are no bugs when the yearly savings is = to
how much each apt cost. 

The TestingValueLarge class is going to make sure that there are no bugs when the yearly savings is grater than
how much each apt cost.

The code has not be tested. The numbers (that is, the values passed into the constructor) 
need to change before testing. 
"""


class TestingBasic(unittest.TestCase):

    def setUp(self):
        self._calculator_obj = Calculator(30000, 25000, 2019, 30000, 2000)

    def test_apartments_needed(self):
        self.assertEqual(self._calculator_obj.get_apartments_needed(), 17)

    def test_years_needed(self):
        self.assertEqual(self._calculator_obj.get_years_needed(), 14)

    def test_net_worth(self):
        self.assertEqual(self._calculator_obj.get_net_worth(), 510000.0)

    def tearDown(self):
        self._calculator_obj = None


class TestingValueSmall(unittest.TestCase):

    def setUp(self):
        self._calculator_obj = Calculator(150000, 70000, 2019, 80000, 6666)
        self._calculator_data = {2019: [0, 70000],
                                 2020: [1.0, 66666],
                                 2021: [2.0, 69998],
                                 2022: [3.0, 79996],
                                 2023: [4.0, 96660],
                                 2024: [6.0, 46656],
                                 2025: [7.0, 83318],
                                 2026: [8.0, 126646],
                                 2027: [10.0, 103306],
                                 2028: [12.0, 93298],
                                 2029: [14.0, 96622],
                                 2030: [16.0, 113278],
                                 2031: [18.0, 143266],
                                 2032: [20.0, 186586],
                                 2033: [23.0, 169904]}

    def test_value_small(self):
        """
        Year number: 2019, Apt number owned 0 Passive Income $70000
        Year number: 2020, Apt number owned 1.0 Passive Income $66666
        Year number: 2021, Apt number owned 2.0 Passive Income $69998
        Year number: 2022, Apt number owned 3.0 Passive Income $79996
        Year number: 2023, Apt number owned 4.0 Passive Income $96660
        Year number: 2024, Apt number owned 6.0 Passive Income $46656
        Year number: 2025, Apt number owned 7.0 Passive Income $83318
        Year number: 2026, Apt number owned 8.0 Passive Income $126646
        Year number: 2027, Apt number owned 10.0 Passive Income $103306
        Year number: 2028, Apt number owned 12.0 Passive Income $93298
        Year number: 2029, Apt number owned 14.0 Passive Income $96622
        Year number: 2030, Apt number owned 16.0 Passive Income $113278
        Year number: 2031, Apt number owned 18.0 Passive Income $143266
        Year number: 2032, Apt number owned 20.0 Passive Income $186586
        Year number: 2033, Apt number owned 23.0 Passive Income $169904
        You can reach a passive income of $150000, but it will take: 15 years
        """

        for k in self._calculator_obj.get_results().keys():
            self.assertEqual(self._calculator_obj.get_results().get(k), self._calculator_data.get(k))

    def test_apartments_needed(self):
        self.assertEqual(self._calculator_obj.get_apartments_needed(), 23)

    def test_years_needed(self):
        self.assertEqual(self._calculator_obj.get_years_needed(), 15)

    def test_net_worth(self):
        self.assertEqual(self._calculator_obj.get_net_worth(), 1840000)

    def tearDown(self):
        self._calculator_obj = None


class TestingValueSame(unittest.TestCase):

    def setUp(self):
        self._calculator_obj = Calculator(150000, 80000, 2019, 80000, 6666)
        self._calculator_data = {2019: [1.0, 6666],
                                 2020: [2.0, 19998],
                                 2021: [3.0, 39996],
                                 2022: [4.0, 66660],
                                 2023: [5.0, 99990],
                                 2024: [7.0, 66652],
                                 2025: [8.0, 119980],
                                 2026: [10.0, 106640],
                                 2027: [12.0, 106632],
                                 2028: [14.0, 119956],
                                 2029: [16.0, 146612],
                                 2030: [18.0, 186600],
                                 2031: [21.0, 166586],
                                 2032: [24.0, 166570]}

    def test_value_same(self):
        """
        Year number: 2019, Apt number owned 1.0 Passive Income $6666
        Year number: 2020, Apt number owned 2.0 Passive Income $19998
        Year number: 2021, Apt number owned 3.0 Passive Income $39996
        Year number: 2022, Apt number owned 4.0 Passive Income $66660
        Year number: 2023, Apt number owned 5.0 Passive Income $99990
        Year number: 2024, Apt number owned 7.0 Passive Income $66652
        Year number: 2025, Apt number owned 8.0 Passive Income $119980
        Year number: 2026, Apt number owned 10.0 Passive Income $106640
        Year number: 2027, Apt number owned 12.0 Passive Income $106632
        Year number: 2028, Apt number owned 14.0 Passive Income $119956
        Year number: 2029, Apt number owned 16.0 Passive Income $146612
        Year number: 2030, Apt number owned 18.0 Passive Income $186600
        Year number: 2031, Apt number owned 21.0 Passive Income $166586
        Year number: 2032, Apt number owned 24.0 Passive Income $166570
        You can reach a passive income of $150000, but it will take: 14 years
        """

        for k in self._calculator_obj.get_results().keys():
            self.assertEqual(self._calculator_obj.get_results().get(k), self._calculator_data.get(k))

    def test_apartments_needed(self):
        self.assertEqual(self._calculator_obj.get_apartments_needed(), 24)

    def test_years_needed(self):
        self.assertEqual(self._calculator_obj.get_years_needed(), 14)

    def test_net_worth(self):
        self.assertEqual(self._calculator_obj.get_net_worth(), 1920000)

    def tearDown(self):
        self._calculator_obj = None


class TestingValueLarge(unittest.TestCase):

    def setUp(self):
        self._calculator_obj = Calculator(150000, 90000, 2019, 80000, 6666)
        self._calculator_data = {2019: [1.0, 16666],
                                 2020: [2.0, 39998],
                                 2021: [3.0, 69996],
                                 2022: [4.0, 106660],
                                 2023: [6.0, 76656],
                                 2024: [8.0, 59984],
                                 2025: [9.0, 129978],
                                 2026: [11.0, 133304],
                                 2027: [13.0, 149962],
                                 2028: [15.0, 179952],
                                 2029: [18.0, 149940],
                                 2030: [20.0, 213260],
                                 2031: [23.0, 216578]}

    def test_value_large(self):
        """
        Year number: 2019, Apt number owned 1.0 Passive Income $16666
        Year number: 2020, Apt number owned 2.0 Passive Income $39998
        Year number: 2021, Apt number owned 3.0 Passive Income $69996
        Year number: 2022, Apt number owned 4.0 Passive Income $106660
        Year number: 2023, Apt number owned 6.0 Passive Income $76656
        Year number: 2024, Apt number owned 8.0 Passive Income $59984
        Year number: 2025, Apt number owned 9.0 Passive Income $129978
        Year number: 2026, Apt number owned 11.0 Passive Income $133304
        Year number: 2027, Apt number owned 13.0 Passive Income $149962
        Year number: 2028, Apt number owned 15.0 Passive Income $179952
        Year number: 2029, Apt number owned 18.0 Passive Income $149940
        Year number: 2030, Apt number owned 20.0 Passive Income $213260
        Year number: 2031, Apt number owned 23.0 Passive Income $216578
        You can reach a passive income of $150000, but it will take: 13 years
        """
        for k in self._calculator_obj.get_results().keys():
            self.assertEqual(self._calculator_obj.get_results().get(k), self._calculator_data.get(k))

    def test_apartments_needed(self):
        self.assertEqual(self._calculator_obj.get_apartments_needed(), 23)

    def test_years_needed(self):
        self.assertEqual(self._calculator_obj.get_years_needed(), 13)

    def test_net_worth(self):
        self.assertEqual(self._calculator_obj.get_net_worth(), 1840000)

    def tearDown(self):
        self._calculator_obj = None


if __name__ == '__main__':
    unittest.main()