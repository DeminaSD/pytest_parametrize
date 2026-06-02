def square_square(a):
    return a*a

def rectangle_square(a,b):
    return a*b

def storage(salary,percent_mortgage,percent_life):
    salary_year = salary * 12
    mortgage = salary_year * percent_mortgage/100
    life = salary_year * percent_life/100
    result = salary_year - mortgage - life    
    return result

print(5)