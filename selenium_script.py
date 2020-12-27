from selenium import webdriver
import unittest
from app import Users as Users


class Test_Home_Page(unittest.TestCase):

    def setUp(self):        
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    # User Story: billy_testcase goes to the site address and expects to see Home in the title
    def test_home_page_should_render(self):
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn("Home", self.driver.title)
    
    # User Story: billy_testcase expects to be able to navigate to the "add new user" page
    def test_add_user_page_should_render(self):
        self.driver.get("http://127.0.0.1:5000")
        btn_add_user = self.driver.find_element_by_id("btn-add-user")
        btn_add_user.click()
        self.assertIn("Add New User", self.driver.title)
    
    # User Story: billy_testcase should be able to add himself as a new user
    def test_adding_new_user_should_contain_new_user_in_list(self):
        self.driver.get("http://127.0.0.1:5000/add_user")
        self.assertIn("Add New User", self.driver.title)
        first_name_field = self.driver.find_element_by_id("first-name")
        first_name_field.send_keys("billy_testcase")
        second_name_field = self.driver.find_element_by_id("second-name")
        second_name_field.send_keys("bob_testcase")
        country_field = self.driver.find_element_by_id("country")
        country_field.send_keys("america_testcase")
        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()
        self.assertIn("Home", self.driver.title)

        user_actual = Users.query.filter_by(firstname = "billy_testcase").first()
        print(user_actual)
        self.assertIsInstance(user_actual, Users)
    
    
    # User Story: Eddy should be able to add a new user
    def test_deleting_user_should_remove_user_from_list(self):
        self.driver.get("http://127.0.0.1:5000/delete_user")
        self.assertIn("Delete User", self.driver.title)
        user_id = self.driver.find_element_by_id("id")
        user_id.send_keys("4")
        btn_submit = self.driver.find_element_by_id("submit")
        btn_submit.click()
        self.assertIn("Home", self.driver.title)
        
        try:
            testcase_user_id = self.driver.find_element_by_id("4")
            element_not_found = False
        except:
            element_not_found = True
        
        self.assertTrue(element_not_found)


if __name__ == "__main__":
    unittest.main()
    