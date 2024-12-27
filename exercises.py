s1 = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
of negation) they are a complete set of basic logical operations — all other logical 
operations, no matter how complex, can be obtained by suitable combinations of these.” 
― John von Neumann, The Computer and the Brain
"""

# # ```
# {
#     'A': 2, 
#     'a': 2, 
#     'B': 2, 
#     'b': 1, 
#     'C': 1
# }
# ```

empty_string={}

s="""“The Computer and the Brain"""

s="abaaade"

for x in s1:
    if(x.isalpha()):
            # empty_string[x]=0
            # for keys,values in empty_string.items():
            #   empty_string[keys]=empty_string[keys]+1
            if x in empty_string:
                 empty_string[x]+=1
            else:
                 empty_string[x]=1
        
print(empty_string)

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

d1.update(d2)
d1.update(d3)

for keys,values in d1.items():
    print(f"keys:{keys},values:{values}")
        

grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam = {
    'Eric': 99,
    'John': 100
}

for key,val in grades.items():
    # print(val,exam[key])
    if(key in exam):
       val.insert(0,exam[key])
    else:
       val.insert(0,None)
       
print(grades)

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