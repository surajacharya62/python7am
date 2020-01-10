
total_income = 150000
rate = 3.5
time_year = 3

calculated_interest = (total_income * rate * time_year) // 100
calculated_income_basedon_interest = (calculated_interest * 100) // (rate * time_year)

print(f'Your calculated interest of {time_year} year is: {calculated_interest}')
print(f'Your calculated income based on the interest {calculated_interest} of {time_year} year is: {calculated_income_basedon_interest}')



