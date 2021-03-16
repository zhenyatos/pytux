class Scorer:
    """
    Class responsible for generating scoring Ren'Py code.
    """
    SCORE_PREFIX = "score_"
    TAB = " " * 4

    __quiz_in_test = {}
    __test_keys = {}
    __counter = 0

    def add_quiz(self, test_name):
        """
        Marking quiz as part of some test.

        :param test_name: name of test
        :return: None.
        """
        if test_name in self.__quiz_in_test.keys():
            self.__quiz_in_test[test_name] += 1
        else:
            self.__quiz_in_test[test_name] = 1
            self.__counter += 1
            self.__test_keys[test_name] = self.__counter

    def init_rpy_variables(self):
        """
        Initializing Ren'Py scoring variables for all tests.

        :return: None.
        """
        if len(self.__test_keys) == 0:
            return ""
        vars = ""
        for n in self.__test_keys.values():
            vars += f"{Scorer.TAB}$ {self.SCORE_PREFIX}{n} = 0\n"
        return vars

    def update_score(self, test_name):
        """
        Generate Ren'Py update score for test sentence.

        :param test_name: name of test
        :return: Ren'Py code for scoring.
        """
        return f"$ {self.SCORE_PREFIX}{self.__test_keys[test_name]} += 1\n"


Tescha = Scorer()
