from random import shuffle


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

    """
    Add answer to quiz.
    
    :param marker: '+' if answer is correct, '-' if answer is incorrect
    :param text: text of the answer 
    """
    def add_answer(self, marker, text):
        self.__answers.append({'marker': marker, 'text': text})

    """
    Quiz validation function: when there is more than one correct answer or no correct answers, or 
    there is no incorrect answers, than some error will be raised.
    
    :return: None.
    """
    def __validate_quiz(self):
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

    """
    Quiz generation.
    
    :return: Ren'Py code for quiz.
    """
    def generate_quiz(self):
        # Checking answers and shuffling them randomly
        self.__validate_quiz()
        shuffle(self.__answers)

        result = ''
        result += f"menu quiz_{self.__counter}:\n"          # Ren'Py menu statement
        result += f"{Quiz.TAB}\"{self.__question}\"\n\n"    # question is placed right after
        for answer in self.__answers:
            result += f"{Quiz.TAB}\"{answer['text']}\":\n"
            if answer['marker'] == '+':
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_CORRECT}\"\n"
            else:
                result += f"{Quiz.TAB2}\"{Quiz.DEFAULT_INCORRECT}\"\n"

        return result
