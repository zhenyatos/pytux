from enum import Enum


class VarType(Enum):
    STRING = 1


class VarSystem:
    """
    Class responsible for handling variables in pytux program
    """

    __variables = {}

    """
    Initializes variable or assigns value to existing variable.

    :param name: variable identifier 
    :param value: variable value
    :param type: variable type
    :return: None.
    """

    def init_or_assign(self, name: str, value, type: VarType):
        if name in self.__variables:
            var_type = self.__variables[name][1]
            if var_type != type:
                raise ValueError("trying to assign value of type [{}] to the variable [{}] of type "
                                 "[{}]".format(type, name, var_type))
        self.__variables[name] = (value, type)

    """
    Gets variable value if variable with such identifier exists.
    
    :param name: variable identifier 
    :return: variable value.
    """

    def get_value(self, name: str):
        if name in self.__variables:
            return self.__variables[name][0]
        else:
            return None


Varya = VarSystem()