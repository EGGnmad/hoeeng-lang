from hoeeng.parser import Parser

def main():
    parser = Parser()
    parser.run('흐...에..엣.....')  # 5번째 변수에 10 대입
    parser.run('호...에엣...ㅇ...엥')  # "!"(33) 출력

if __name__ == '__main__':
    main()