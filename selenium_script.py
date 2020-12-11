from selenium import webdriver
import unittest


class Test_Home_Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    # User Story: Eddy goes to site.com and expects to see Home in the title
    def test_home_page_being_rendered(self):
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn("Home", self.driver.title)
    
    # User Story: Eddy expects to be able to add a new user
    def test_add_user_page_being_rendered(self):
        self.driver.get("http://127.0.0.1:5000/add_user")
        self.assertIn("Add New User", self.driver.title)

if __name__ == "__main__":
    unittest.main()
    