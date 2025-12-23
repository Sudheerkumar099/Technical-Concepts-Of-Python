first_name = "Sudheer"
last_name = "Kumar"
full_name = f"({len(first_name)} {3+3})"
print(full_name)

course_name = "Python Programming"
upper = course_name.upper()
lower = course_name.lower()
tite= course_name.title()
print(upper)
print(lower)
print(course_name) 
print(tite) #to make every letter of first word capital
print(course_name.strip()) #to remove extra spaces from start and end and we also have lstrip() and rstrip() methods
print(course_name.find("Pro")) #gives the starting index of the substring
print(course_name.replace("Python", "Java")) #replaces the substring with new substring
print(course_name)
print("Programming" in course_name) #checks if the substring is present in the string or not and returns boolean value
print("programming" not in course_name) #checks if the substring is not present in the string or not and returns boolean value

def my_fun(n):
    print(n)