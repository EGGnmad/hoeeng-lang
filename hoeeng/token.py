token = {
    'init': ['흐'],
    'print': ['호'],
    'var': ['에'],
    'ascii': ['엥'],
    'input': ['헤'],
    # 'next': [' '],
    # 'EOL': ['\n'],

    # operations
    '+': ['ㅇ'],
    '*': ['엣'],
    '/': ['엫'],
}

class Token:
    @staticmethod
    def tokenizer(text: str):
        stack: list = []
        num_stack = 0

        for i in text:
            if i in token['init']:
                add_token(stack, Token('init', i))
                num_stack = 0  # 초기화

            elif i in token['print']:
                add_token(stack, Token('print', i))
                num_stack = 0  # 초기화

            elif i in token['var']:
                add_token(stack, Token('var', num_stack))
                num_stack = 0  # 초기화

            elif i in token['input']:
                add_token(stack, Token('cnt', num_stack))
                add_token(stack, Token('input', i))
                num_stack = 0  # 초기화

            elif i in token['ascii']:
                if num_stack != 0:
                    add_token(stack, Token('cnt', num_stack))
                add_token(stack, Token('ascii', i))
                num_stack = 0  # 초기화

            elif i in token['+']:
                add_token(stack, Token('cnt', num_stack))
                num_stack = 0  # 초기화

            elif i in token['*']:
                if num_stack != 0:
                    add_token(stack, Token('cnt', num_stack))
                add_token(stack, Token('*', '*'))
                num_stack = 0  # 초기화

            elif i in token['/']:
                if num_stack != 0:
                    add_token(stack, Token('cnt', num_stack))
                add_token(stack, Token('/', '/'))
                num_stack = 0  # 초기화

            # elif i in token['next']:
            #     add_token(stack, Token('cnt', num_stack))
            #     add_token(stack, Token('next', i))
            #     num_stack = 0  # 초기화
            #
            # elif i in token['EOL']:
            #     add_token(stack, Token('cnt', num_stack))
            #     add_token(stack, Token('EOL', i))
            #     num_stack = 0  # 초기화

            elif i == '.':
                num_stack += 1

            elif i == '~':
                num_stack -= 1

        if not (stack[len(stack) - 1].type in ['ascii', 'EOL']) and num_stack != 0:
            add_token(stack, Token('cnt', num_stack))

        return stack

    def __init__(self, type: str, value):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'<token.{self.type} {self.value}>'

def add_token(list: list, token: Token):
    if token.type == 'cnt':
        list.append(Token('+', '+'))
    list.append(token)