from random import shuffle
from .tescha import Tescha
from .. import const

class QuizError(Exception):
    pass


class Quiz:
    """
    Class responsible for Ren'Py quiz generation
    """
    TAB = " " * 4
    TAB2 = TAB * 2

    __counter = 0

    def __init__(self, question, lineno):
        self.__question = question
        self.__answers = []
        self.__lineno = lineno
        self.yes = const.CONFIG_DEFAULT[const.CONFIG_KEY_QUIZ_YES]
        self.no = const.CONFIG_DEFAULT[const.CONFIG_KEY_QUIZ_NO]
        Quiz.__counter += 1

    def add_answer(self, marker, text):
        """
        Add answer to quiz.

        :param marker: '+' if answer is correct, '-' if answer is incorrect
        :param text: text of the answer
        :return: None.
        """
        self.__answers.append({'marker': marker, 'text': text})

    def __validate_quiz(self):
        """
        Quiz validation function: when there is more than one correct answer or no correct answers, or
        there is no incorrect answers, than some error will be raised.

        :return: None.
        """
        n_correct = 0
        n_incorrect = 0
        for answer in self.__answers:
            n_correct += (answer['marker'] == '+')
            n_incorrect += (answer['marker'] == '-')

        if n_correct > 1:
            raise QuizError(f"More than one answer marked with + in quiz on line {self.__lineno}")
        if n_correct == 0:
            raise QuizError(f"There must be at least one answer marked with + in quiz on line {self.__lineno}")
        if n_incorrect == 0:
            raise QuizError(f"There must be at least one answer marked with - in quiz on line {self.__lineno}")

    def generate_lonely_quiz(self):
        """
        Lonely quiz generation, without scoring.

        :return: Ren'Py code for quiz.
        """
        # Checking answers and shuffling them randomly
        self.__validate_quiz()
        shuffle(self.__answers)

        result = ''
        result += f"menu quiz_{self.__counter}:\n"  # Ren'Py menu statement
        result += f"{Quiz.TAB}\"{self.__question}\"\n\n"  # question is placed right after
        for answer in self.__answers:
            result += f"{Quiz.TAB}\"{answer['text']}\":\n"
            if answer['marker'] == '+':
                result += f"{Quiz.TAB2}\"{self.yes}\"\n"
            else:
                result += f"{Quiz.TAB2}\"{self.no}\"\n"

        return result

    def generate_test_quiz(self, test_name):
        """
        Test quiz generation, scoring added.

        :return: Ren'Py code for quiz.
        """
        # Checking answers and shuffling them randomly
        self.__validate_quiz()
        shuffle(self.__answers)

        Tescha.add_quiz(test_name) # this quiz is scored

        result = ''
        result += f"menu quiz_{self.__counter}:\n"  # Ren'Py menu statement
        result += f"{Quiz.TAB}\"{self.__question}\"\n\n"  # question is placed right after
        for answer in self.__answers:
            result += f"{Quiz.TAB}\"{answer['text']}\":\n"
            if answer['marker'] == '+':
                result += f"{Quiz.TAB2}{Tescha.update_score(test_name)}" # update score if answer is correct
                result += f"{Quiz.TAB2}\"{self.yes}\"\n"
            else:
                result += f"{Quiz.TAB2}\"{self.no}\"\n"

        return result

    def set_yes_no(self, yes, no):
        """
        Set response to correct/incorrect answer.

        :param yes: if answer is correct
        :param no: if answer is incorrect
        :return: None.
        """
        self.yes = yes
        self.no = no

