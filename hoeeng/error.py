class Error:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'

class CantFoundVariableError(Error):
    def __init__(self):
        super().__init__('변수를 찾을 수 없습니다.')

class ExpressionError(Error):
    def __init__(self, **kwargs):
        super().__init__(f'잘못된 식입니다. ( "{kwargs["wrong"]}" )' )

class AsciiExpressionError(Error):
    def __init__(self, **kwargs):
        super().__init__(f'"엥"은 식 뒤에 와야 합니다.' )

class WrongInputError(Error):
    def __init__(self, **kwargs):
        super().__init__(f'잘못된 식입니다. ( "{kwargs["wrong"]}" )')