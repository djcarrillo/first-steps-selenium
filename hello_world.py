import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    def test_hello_word(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='report', report_name='hello-word-report'))
