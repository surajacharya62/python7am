age = int(input('Please provide your age: '))

if age >= 18 and age <= 40:
    print('Welcome to the party world')
elif age < 18:
    print('Sorry, you are under age')
else:
    print('Sorry, you are too old.')