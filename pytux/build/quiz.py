from random import shuffle
from .tescha import Tescha


class QuizError(Exception):
    pass


class Quiz:
    """
    Class responsible for Ren'Py quiz generation
    """
    DEFAULT_CORRECT = "Yes, you are right!"
    DEFAULT_INCORRECT = "Nope, wrong answer..."
    TAB = " " * 4
    TAB2 = TAB * 2

    __counter = 0

    def __init__(self, question, lineno):
        self.__question = question
        self.__answers = []
        self.__lineno = lineno
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
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_CORRECT}\"\n"
            else:
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_INCORRECT}\"\n"

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
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_CORRECT}\"\n"
            else:
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_INCORRECT}\"\n"

        return result
