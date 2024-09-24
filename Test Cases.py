import unittest
from unittest.mock import patch
import numpy as np


class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_first_option_left(self, mock_print, mock_input):
        directions = np.array(["Left", "Right", "Straight", "Back"])
        expected_print_calls = [
            "Which path do you choose?",
            "1. Left",
            "2. Right",
            "3. Straight",
            "4. Back",
            "Infront of you there is a pond."
        ]

        first_decision, second_decision = first_option()
        self.assertEqual(first_decision, "Left")
        self.assertIn("Do you swim across or walk alongside?", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=['2', 'Swim across'])
    @patch('builtins.print')
    def test_first_option_right(self, mock_print, mock_input):
        directions = np.array(["Left", "Right", "Straight", "Back"])
        expected_print_calls = [
            "Which path do you choose?",
            "1. Left",
            "2. Right",
            "3. Straight",
            "4. Back",
            "You get into a fruit yard."
        ]

        first_decision, second_decision = first_option()


        self.assertEqual(first_decision, "Right")
        self.assertIn("Do you pick a fruit or keep exploring?", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_second_option_hide(self, mock_print, mock_input):
        decision = second_option()
        self.assertEqual(decision, "Hide")

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_final_option_leave(self, mock_print, mock_input):
        decision = final_option()
        self.assertEqual(decision, "Leave it there")
        self.assertIn("You leave it there and keep exploring.", [call[0][0] for call in mock_print.call_args_list])

    @patch('builtins.input', side_effect=['no'])
    @patch('builtins.print')
    def test_game_loop_replay_no(self, mock_print, mock_input):
        with patch('game.game_loop', return_value=None):
            main()
            mock_print.assert_called_with("Thank you for participating")


if __name__ == '__main__':
    unittest.main()
