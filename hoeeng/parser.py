from hoeeng.token import Token
from hoeeng.error import (Error, CantFoundVariableError, AsciiExpressionError, WrongInputError, ExpressionError)

#TODO: next 토큰,
class Parser:
    def __init__(self):
        self.stack = [0 for x in range(10000)]

    def run(self, text:str):
        token = Token.tokenizer(text)
        # print(token)
        self.parse(token)

    def parse(self, list):
        start = 0

        # 변수 대입
        if list[start].type == 'init':
            if list[start + 1].type == 'var':
                self.stack[ list[start + 1].value ] = self.expression(list[start + 2:])
            else:
                self.raise_error(CantFoundVariableError())
                exit()

        elif list[start].type == 'print':
            output = self.expression(list[start + 1:])
            if list[len(list) -1].type == 'ascii':
                output = chr(output)
            print(output)


    def expression(self, list) -> int:
        num_stack = []

        for i in list:
            # print(num_stack[len(num_stack) -1])
            if i.type != 'ascii':
                if i.type == 'var':
                    num_stack += str(self.stack[i.value])

                elif i.type == 'input':
                    get = input()
                    try:
                        num_stack += str(int(get))
                    except ValueError:
                        self.raise_error(WrongInputError(wrong=get))
                        exit()

                else:
                    num_stack += str(i.value)

        try:
            return eval("".join(num_stack))

        except SyntaxError:
            self.raise_error(ExpressionError(wrong="".join(num_stack)))
            exit()

    def raise_error(self, error:Error):
        print(error)

