nepali = int(input("Please provide your Nepali Subject's mark: "))
english= int(input("Please provide your English Subject's mark: "))
math = int(input("Please provide your Math Subject's mark: "))
science = int(input("Please provide your Scienc Subject's mark: "))
population = int(input("Please provide your Population Subject's mark: "))

total_marks = 500
total_obtained_mark = nepali + english + math + science + population
percentage = (total_obtained_mark / total_marks) * 100

if nepali < 35 and english < 35 and math < 35 and science < 35 and population < 35:
    print('Sorry, your have not obtained pass marks: "Your are failed in the subjects, Please reattempt"')
    if percentage >= 35 and percentage <= 45:
        print("Division: Third")
    else:
        print("You have least marks in the subject. Please reattempt")
elif nepali > 35 and