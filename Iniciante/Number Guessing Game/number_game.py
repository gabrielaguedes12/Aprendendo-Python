import random

lowest_num = 1
highest_num = 100
#radint é uma função que sorteia um numero inteiro aleatorio de um intervalo
answer = random.randint(lowest_num, highest_num)

guesses=0
is_running = True

print("Python Number Guessing Game")
print(f"Selecione um número entre {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Insira seu palpite: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("Número fora do intervalo")
            print(f"Por favor selecione um número entre {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Muito Baixo! Tente novamente")
        elif guess > answer:
            print("Muito Alto! Tente novamente")
        else: 
            print(f"Correto! A resposta é {answer}")    
            print(f"Numero de palpites: {guesses}")
            #is_running = False
    else:
        print("Palpite inválido")
        print(f"Por favor selecione um número entre {lowest_num} and {highest_num}")
        
        