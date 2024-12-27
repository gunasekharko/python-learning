# m=[[1 if row==col else 0 for col in range(3)]for row in range(3)]

# print(m)


data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']

frequency={}

for element in set(data):
   count=len([char for char in data if char == element])
   frequency[element]=count

# print(frequency)


data = [
    {'open': 100, 'high': 120, 'low': 90, 'close': 110},
    {'open': 110, 'high': 130, 'low': 80, 'close': 120},
    {'open': 120, 'high': 140, 'low': 70, 'close': 130},
    {'open': 130, 'high': 150, 'low': 60, 'close': 140},
]

ranges = []
for d in data:
    ranges.append(d['high'] - d['low'])

result=[d['high'] - d['low'] for d in data]


result=[]

for i in range(1,101):
    for j in range(2,10):
        if i%j==0:
          result.append(i)
print(result)

result1=[]
for num in range(1,101):
    if num not in result:
        result1.append(num)

# print(result1)



data = [
    {'symbol': 'ABCD', 'name': 'ABCD Company', 'ranking': 2, 'risk': 0.2},
    {'symbol': 'BCDE', 'name': 'BCDE Company', 'ranking': 5, 'risk': 0.2},
    {'symbol': 'CDEF', 'name': 'CDEF Company', 'ranking': 8, 'risk': 0.5},
    {'symbol': 'DEFG', 'name': 'DEFG Company', 'ranking': 7, 'risk': 0.8},
    {'symbol': 'EFGH', 'name': 'EFGH Company', 'ranking': 9, 'risk': 0.6},
    {'symbol': 'FGHI', 'name': 'FGHI Company', 'ranking': 10, 'risk': 0.1},
    {'symbol': 'GHIJ', 'name': 'GHIJ Company', 'ranking': 3, 'risk': 0.6},
    {'symbol': 'HIJK', 'name': 'HIJK Company', 'ranking': 5, 'risk': 0.5},
    {'symbol': 'IJKL', 'name': 'IJKL Company', 'ranking': 5, 'risk': 0.7},
    {'symbol': 'JKLM', 'name': 'JKLM Company', 'ranking': 6, 'risk': 0.9},
    {'symbol': 'KLMN', 'name': 'KLMN Company', 'ranking': 6, 'risk': 0.4},
    {'symbol': 'LMNO', 'name': 'LMNO Company', 'ranking': 8, 'risk': 0.4},
    {'symbol': 'MNOP', 'name': 'MNOP Company', 'ranking': 8, 'risk': 0.2},
    {'symbol': 'NOPQ', 'name': 'NOPQ Company', 'ranking': 1, 'risk': 0.5},
    {'symbol': 'OPQR', 'name': 'OPQR Company', 'ranking': 9, 'risk': 0.2},
    {'symbol': 'PQRS', 'name': 'PQRS Company', 'ranking': 10, 'risk': 0.9},
    {'symbol': 'QRST', 'name': 'QRST Company', 'ranking': 3, 'risk': 0.4},
    {'symbol': 'RSTU', 'name': 'RSTU Company', 'ranking': 7, 'risk': 0.3},
    {'symbol': 'STUV', 'name': 'STUV Company', 'ranking': 8, 'risk': 0.1},
    {'symbol': 'TUVW', 'name': 'TUVW Company', 'ranking': 7, 'risk': 0.9}
]

data_result=[]

# Write code that does these two things:
# - creates a new list of of dictionaries where the ranking is at least `5`, and the risk is less than `0.6`
# - these dictionaries should contain the `symbol` and a calculated key, named `weighted`, 
# which is the result of dividing `ranking` by `risk`. (You should round this value two decimal places). 
# Do **not** mutate the original `data` list or dictionaries in any way.

for d in data:
    if (d['ranking']>=5 and d['risk']<0.6):
        new_entry={
            'symbol':d['symbol'],
            'weighted':round(d['ranking']/d['risk'],2)
        }
        data_result.append(new_entry)
print(data_result)



students = {
    'Alice': {'Math': 85, 'Science': 92, 'English': 88},
    'Bob': {'Math': 78, 'Science': 81, 'English': 74},
    'Charlie': {'Math': 95, 'Science': 89, 'English': 93},
    'David': {'Math': 62, 'Science': 70, 'English': 65},
    'Eva': {'Math': 88, 'Science': 90, 'English': 85}
}

# Calculate the average grade for each student and add it to the dictionary
for student, grades in students.items():
    average = sum(grades.values()) / len(grades)
    students[student]['Average'] = round(average, 2)

# Find the student with the highest average grade using a for loop
highest_avg_student = None
highest_avg = 0

for student, grades in students.items():
    if grades['Average'] > highest_avg:
        highest_avg = grades['Average']
        highest_avg_student = student

print(f"\nStudent with the highest average grade: {highest_avg_student}")