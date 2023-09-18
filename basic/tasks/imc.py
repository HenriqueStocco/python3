# DDigite seu nome, sua altura (metros) e peso (kilos) e calcule o imc (body mass index -> bmi).

name = 'Henrique Stocco'
height = 1.70
weight = 65
bmi = weight / (height**2)

# Underweight < 18,5
# Normal 18,5 - 24,9
# Overweight 25 - 29,9
# Obese 30 - 34,9
# Extremely Obese > 35 

print(f'Your name is {name} , you are {height:.2f} meters tall, weight {weight} kg and your BMI is {bmi:.2f}')
# imc = weight / (height * height)