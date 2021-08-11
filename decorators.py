import math

def decorator(func):
    def decorated(input_text):
        if input_text > 0:
            func(input_text)
        else:
            raise ValueError('Input must be positive value')
    return decorated
@decorator

def make_area(input_text):
    print(f'triangle_area : { (math.sqrt(3)/4) * (input_text **2) }')
    print(f'square : {input_text ** 2}')

make_area(int(3))

def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated


@decorator

def hello_world(input_text):
    print(input_text)

hello_world('HelloWorld!')