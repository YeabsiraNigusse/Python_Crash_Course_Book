import unittest
from City_function import City

class TestCityName(unittest.TestCase):
    def test_city_country(self):
        formatted_name = City('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
    def test_city_country_population(self):
        formatted_name = City('santiago', 'chile','5000000')
        self.assertEqual(formatted_name,'Santiago, Chile - Population 5000000')
    print(__name__)
if __name__ == '__main__':
 unittest.main()
 