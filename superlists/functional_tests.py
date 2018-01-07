from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# I have heard about a cool new online to-do app. I go
		# to checkout its home page
		self.browser.get('http://localhost:8000')

		# I notice the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual('To-Do lists', header_text)

		# I am invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# I type "Buy peacock feathers" into text box
		inputbox.send_keys('Buy peacock feathers')

		# When I hit enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertEqual('1: Buy peacock feathers', [row.text for row in rows])

		# There is still a text box inviting me to add another item. I 
		# enter "Use peacock feathers to make a fly"
		
		# The page updates again, and now shows both items in my list

		# I wonder whether site remembers my list. Then I see
		# that the site has generated a unique URL for mine -- there is 
		# some explanatory text to that effect

		# I visit that URL - my to-do list is still there

		# Satisfied, I go back to sleep

# It is done because this is not part of another script. An independent script
if __name__ == '__main__':
	unittest.main(warnings='ignore')