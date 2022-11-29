#Name: Omer Faruk AYDIN
#Number: 150210726

# Defining function for reading .csv file
def read_grades(filename):
    # Opening file with read mode
    fn = open(filename, "r", encoding="utf8").read()
    name, mt1, mt2, final = {},{},{},{}
    # Split the content line by line
    fn = fn.split("\n")

    for i in fn:
        fn = [i.split(",")]
        # Creating name dictionary with taking first and second elements from each line
        for line in fn:
            name[line[0]] = line[1]

        # Creating mt1 dictionary with taking first and fourth elements from each line if exam is midterm1
        for line in fn:
            if line[2] == 'midterm1':
                mt1[line[0]] = int(line[3])

        # Creating mt2 dictionary with taking first and fourth elements from each line if exam is midterm2
        for line in fn:
            if line[2] == 'midterm2':
                mt2[line[0]] = int(line[3])

        # Creating final dictionary with taking first and fourth elements from each line if exam is final
        for line in fn:
            if line[2] == 'final':
                final[line[0]] = int(line[3])

    return name, mt1, mt2, final

# Defining function for covering dictionaries to list of tuples
def convert(names, midterm1, midterm2, final):

    lst = []

    # Creating a tuple with key value pairs from dictionaries and adding to the list
    for key,value in names.items():
        value1 = midterm1[key]
        value2 = midterm2[key]
        valuel = final[key]
        temp = (key,value,value1,value2,valuel)
        lst.append(temp)

    return lst

# Defining a function for exam average
def calculate_exam_average(lst, exam):

    itemcount1 = 0
    itemcount2 = 0
    itemcountl = 0
    sum1 = 0
    sum2 = 0
    suml = 0

    # If the exam is midterm 1, then take the third element from tuples and sum them. After that take the average
    if exam == "midterm1":
        for item in lst:
            itemcount1 = itemcount1 + 1
            sum1 = sum1 + item[2]
        average1 = sum1 / itemcount1
        return average1
    # If the exam is midterm 2, then take the fourth element from tuples and sum them. After that take the average
    if exam == "midterm2":
        for item in lst:
            itemcount2 = itemcount2 + 1
            sum2 = sum2 + item[3]
        average2 = sum2 / itemcount2
        return average2
    # If the exam is final, then take the fifth element from tuples and sum them. After that take the average
    if exam == "final":
        for item in lst:
            itemcountl = itemcountl + 1
            suml = suml + item[4]
        averagel = suml / itemcountl
        return averagel

# Defining a function for detect who got the cumulative grade upper than 60
def find_passing_students(lst):

    names = {}
    mt1 = {}
    mt2 = {}
    final = {}
    student_names = []

    # Taking elements from tuples and add them to different dictionaries
    for index in lst:
        names[index[0]] = index[1]
        mt1[index[0]] = index[2]
        mt2[index[0]] = index[3]
        final[index[0]] = index[4]

    # Calculating cumulative grade with values form mt1, mt2 and final dictionaries
    for key,value in names.items():
        cumulative_grade = 0.3 * mt1[key] + 0.3 * mt2[key] + 0.4 * final[key]
        if cumulative_grade > 60:
            student_names.append(value)
    return student_names

# Defining a function upgrading grades
def manipulate(filename, lst):

    # Opening file that contains upgrade notes
    uf = open(filename, "r", encoding="utf8").read()
    names, mt1, mt2, final, mt1u, mt2u, finalu = {},{},{},{},{},{},{}
    uf = uf.split("\n")

    # Split the content line by line
    for i in uf:
        uf = [i.split(",")]

        # Creating mt1u dictionary with taking first and third elements from each line if exam is midterm1
        for line in uf:
            if line[1] == 'midterm1':
                mt1u[line[0]] = int(line[2])

        # Creating mt2u dictionary with taking first and third elements from each line if exam is midterm2
        for line in uf:
            if line[1] == 'midterm2':
                mt2u[line[0]] = int(line[2])

        # Creating finalu dictionary with taking first and third elements from each line if exam is final
        for line in uf:
            if line[1] == 'final':
                finalu[line[0]] = int(line[2])

    # Covering our list to dictionaries
    for index in lst:
        names[index[0]] = index[1]
    for index in lst:
        mt1[index[0]] = index[2]
    for index in lst:
        mt2[index[0]] = index[3]
    for index in lst:
        final[index[0]] = index[4]

    # If midterm1 grade is exist in mt1u(upgraded) then overwrite to our old mt1 dictionary
    for key,value in mt1.items():
        for keyu,valueu in mt1u.items():
            if key == keyu:
                mt1[key] = mt1u[keyu]

    # If midterm2 grade is exist in mt2u(upgraded) then overwrite to our old mt2 dictionary
    for key,value in mt2.items():
        for keyu,valueu in mt2u.items():
            if key == keyu:
                mt2[key] = mt2u[keyu]

    # If final grade is exist in finalu(upgraded) then overwrite to our old final dictionary
    for key,value in final.items():
        for keyu,valueu in finalu.items():
            if key == keyu:
                final[key] = finalu[keyu]

    result = []

    # Covering the new dictionaries to tuples and add them to list
    for key,value in names.items():
        value1 = mt1[key]
        value2 = mt2[key]
        valuel = final[key]
        temp = (key,value,value1,value2,valuel)
        result.append(temp)

    return result

# Defining a function to write grades to a .csv file
def write_grades(filename, lst):

    # Opening file with write mode
    cf = open(filename, "w")
    # Write a title for first line in .csv file
    title = "ID,Name,Midterm 1,Midterm 2,Final""\n"
    cf.write(title)

    # Writing on .csv file line by line with elements from list
    for index in lst:
        content = index[0]+","+index[1]+","+str(index[2])+","+str(index[3])+","+str(index[4])+"\n"
        cf.write(content)

    # Do not forget to close the file
    cf.close()

if __name__ == '__main__':
    names, midterm1, midterm2, final = read_grades("grades.csv")
    lst = convert(names, midterm1, midterm2, final)
    print(lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "final"))
    print(find_passing_students(lst))
    lst = manipulate("edit.csv", lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "final"))
    print(find_passing_students(lst))
    write_grades("cumulative.csv", lst)