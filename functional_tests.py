from selenium import webdriver
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
        self.fail('Finish the test!')

        # Johno sees the options to create an account or play a game

        # Johno chooses to play a game

        # Johno is white and starts playing. The computer responds with a counter move

        # Johno tries to do an illegal move but the program doesn't let him.
        # The computer beats Johno and Johno is informed of that fact.

        # Johno decides to create an account. 

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
        # Johno logs back in and checks his win loss record again and sees it is stil l1 win and 1 loss
if __name__ == '__main__':
    unittest.main(warnings='ignore')
