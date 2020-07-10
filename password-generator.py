from secrets import choice
lowercase = 'abcdefghikklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%&*()/?°ºª§||=+[]{<>};:'
numbers = '1234567890'

key = lowercase + capital_letters + symbols + numbers
def generate_password(characters):
    password = ''.join(choice(key) for _ in range(characters))
    print(f'the generated password is {password}')
generate_password(int(input('password length: ')))