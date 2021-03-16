class ScorerError(Exception):
    pass

class Scorer:
    """
    Class responsible for generating scoring Ren'Py code.
    """
    SCORE_PREFIX = "score_"
    TAB = " " * 4

    __n_quizzes_in_test = {}
    __test_index = {}
    __counter = 0

    def add_quiz(self, test_name):
        """
        Marking quiz as part of some test.

        :param test_name: name of test
        :return: None.
        """
        if test_name in self.__n_quizzes_in_test.keys():
            self.__n_quizzes_in_test[test_name] += 1
        else:
            self.__n_quizzes_in_test[test_name] = 1
            self.__counter += 1
            self.__test_index[test_name] = self.__counter

    def init_rpy_variables(self):
        """
        Initializing Ren'Py scoring variables for all tests.

        :return: None.
        """
        if len(self.__test_index) == 0:
            return ""
        vars = ""
        for n in self.__test_index.values():
            vars += f"{Scorer.TAB}$ {self.SCORE_PREFIX}{n} = 0\n"
        return vars

    def __var(self, test_name):
        """
        Auxiliary function to generate Ren'Py variable name.

        :param test_name: name of test
        :return: string of Ren'Py variable name.
        """
        return f"{self.SCORE_PREFIX}{self.__test_index[test_name]}"

    def update_score(self, test_name):
        """
        Generate Ren'Py code for updating test score.

        :param test_name: name of test
        :return: string of Ren'Py code.
        """
        return f"$ {self.__var(test_name)} += 1\n"

    def print_score(self, test_name):
        """
        Generate Ren'Py code for printing score.

        :param test_name: name of test
        :return: string of Ren'Py code.
        """
        if test_name not in self.__test_index.keys():
            raise ScorerError(f"There is no such test {test_name}")
        return f"\"{test_name} test: you have obtained [{self.__var(test_name)}] out of {self.__n_quizzes_in_test[test_name]} points.\""


Tescha = Scorer()
