import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_play_games_and_see_record_later(self):
        # Johno has heard about a cool new site to learn how to play chess better
        # He gotes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header meantions Chess Teacher
        self.assertIn('Chess Teacher', self.browser.title)

        # Johno sees the options to create an account or play a game
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Create an account', header_text)
        self.assertIn('play a game', header_text)
        # Johno chooses to play a game
        play_link = self.browser.find_element_by_link_text('play')
        play_link.click()
        self.assertIn('Play a game of chess', self.browser.title)
        
        source_element = self.browser.find_element_by_name('d2')
        dest_element = self.browser.find_element_by_name('d4')
        ActionChains(self.browser).draw_and_drop(source_element, dest_element).perform()
        time.sleep(1)

        d4 = self.browser.find_element_by_name('d4')
        self.assertIn('pawn', d4)
        source_element = self.browser.find_element_by_name('e2')
        dest_element = self.browser.find_element_by_name('f4')

        # Johno is white and starts playing. The computer responds with a counter move

        # Johno tries to do an illegal move but the program doesn't let him.
        # The computer beats Johno and Johno is informed of that fact.
        ActionChains(self.browser).draw_and_drop(source_element, dest_element).perform()
        time.sleep(1)

        f4 = self.browser.find_element_by_name('d4')
        self.assertNotIn('pawn', f4)
        # Johno decides to create an account. 
        home_link = self.browser.find_element_by_name('home')
        self.assertIn('Chess Teacher', self.browser.title)
        account_link = self.browser.find_element_by_link_text('Create account')
        account_link.click()

        inputbox = self.browser.find_element_by_id('username')
        inputbox.send_keys('Johno')
        passwordbox = self.browser.find_element_by_id('password')
        inputbox.send_keys('qwerty12345@')

        user = self.browser.find_elemnt_by_name('user')
        self.assertIn('Johno', user)
        # Johno logs in and sees that he is the current user

        # He sees that his record is 0 wins and 1 loss

        # Johno decided to play again. The computer adjusts to have an easier level 
        # because of Johno's prior loss

        # Johno sees an option to get feedback about a potential move
        # Johno clicks that option and indicates what move he was thinkng of making

        # Johno drags a piece to  a spot and is told that if he moves there he may lose his piece
        # Johno tries a few more moves and they are ranked by the computer and more feedback is given

        # Johno completes the game and wins. He sees his record is now 1 win, 1 loss
        # Johno logs out
        self.fail('Finish the test!')
        # Johno logs back in and checks his win loss record again and sees it is stil l1 win and 1 loss
if __name__ == '__main__':
    unittest.main(warnings='ignore')
