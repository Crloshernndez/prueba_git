# Archivo principal

print("cambio el print")

def run():
    a, b = 0, 1
    while b <= 1597:
        print(a, b, end=' ')
        a = a + b
        b = a + b

run()
