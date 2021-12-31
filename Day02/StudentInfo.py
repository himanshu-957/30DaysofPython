student_name = []
math_marks = []
science_marks = []
hindi_marks = []
english_marks = []
computer_marks = []
final = []
for i in range(1,11):
    name = input("Enter name of {}th student: ".format(i))
    student_name.append(name)
    math = int(input("Enter math marks: "))
    math_marks.append(math)
    science = int(input("Enter Science Marks: "))
    science_marks.append(science)
    hindi = int(input("Enter Hindi Marks: "))
    hindi_marks.append(hindi)
    english = int(input("Enter English Marks: "))
    english_marks.append(english)
    computer = int(input("Enter Computer Marks: "))
    computer_marks.append(computer)
    final.append(name)
    final.append(math)
    final.append(science)
    final.append(hindi)
    final.append(english)
    final.append(computer)
choice = int(input("Which student's marks you want to see?(1 to 10): "))
j = 6*(choice-1)
print("{} has {} marks in Maths, {} marks in Science, {} marks in Hindi, {} marks in English, {} marks in Computer".format(final[j],final[j+1],final[j+2],final[j+3],final[j+4],final[j+5]))