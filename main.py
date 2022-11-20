# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1889667       | |      18896675
# Date: 20/11/2022
class global_variable:  # global variable can be called anywhere within the code
    def __init__(self):
        self.total = 120
        self.grades = range(0, 121, 20)  # acceptable range
        self.progress = ""
        self.trailer = ""
        self.retriver = ""
        self.excluded = ""
        self.outcome_name2 = []
        self.outcome_number2 = []
        self.student_id = ""
        self.student_id_holder = dict()


var = global_variable()


def uni_progress(pdf):  # syntax for pass, defer, and fail(p, d, f)
    sum = pdf[0] + pdf[1] + pdf[2]
    if sum == var.total:  # validates the sum of (p, d, f)
        if pdf[0] == 120:
            var.progress += "*"
            print('Progress')
            var.outcome_name2.append('Progress')
            name_credit = "Progress" + " - " + str(pdf)[1:-1]  # adds the name and the credits together
        elif pdf[0] == 100 and pdf[1] + pdf[2] == 20:
            var.trailer += "*"
            print('Progress(Module trailer)')
            var.outcome_name2.append('Module trailer')
            name_credit = "Progress(Module trailer)" + " - " + str(pdf)[1:-1]
        elif pdf[0] <= 80 and pdf[1] <= 120 and pdf[2] <= 60:
            var.retriver += "*"
            print('Do not progress - module retriver')
            var.outcome_name2.append('Do not progress - module retriver')
            name_credit = "Do not progress - module retriver" + " - " + str(pdf)[1:-1]
        elif pdf[0] <= 40 and pdf[1] <= 40 and pdf[2] >= 80:
            var.excluded += "*"
            print('Excluded')
            var.outcome_name2.append('Exclude')
            name_credit = "Exclude" + " - " + str(pdf)[1:-1]
        var.outcome_number2.append(pdf)  # list part2
        var.student_id_holder[var.student_id] = name_credit  # append method for dictionary/ student id + credit
        return continue_program()
    else:
        print("Total incorrect! Try again!\n")
        return uni_progress(main())  # returns list[p,d,f] from main and validates values again


##def id_validation(): #asks for student id and validates it
##    var.student_id = input("Enter your student ID, beginning with 'w' followed by 7 unique digits: ")
##    if len(var.student_id) == 0:
##        print("Enter a student ID")
##        return id_validation()
##    else:
##            if var.student_id[0] == 'w' and len(var.student_id) == 8:
##                if var.student_id not in var.student_id_holder:
##                    return var.student_id
##                else:
##                    print(f'- {var.student_id} - is taken! Enter again!')
##                    return id_validation()
##            else:
##                print(f'- {var.student_id} - is not valid! Enter again!')
##                return id_validation()

def main():  # acts as function manager
    var.student_id = input("Enter your student ID, beginning with 'w' followed by 7 unique digits: ")
    p = accept_p()
    d = accept_d()
    f = accept_f()
    return [p, d, f]


def accept_p():  # validates if credits are out of range
    try:
        credit = int(input("Enter your pass credits: "))
        if credit in var.grades:
            return credit
        else:
            print(f'({credit}) is not in range')
            return accept_p()
    except ValueError:
        print('Enter a number!')
        return accept_p()


def accept_d():  # validates if credits are out of range
    try:
        credit = int(input("Enter your defer credits: "))
        if credit in var.grades:
            return credit
        else:
            print(f'({credit}) is not in range')
            return accept_d()
    except ValueError:
        print('Enter a number!')
        return accept_d()


def accept_f():  # validates if credits are out of range
    try:
        credit = int(input("Enter your fail credits: "))
        if credit in var.grades:
            return credit
        else:
            print(f'({credit}) is not in range')
            return accept_f()
    except ValueError:
        print('Enter a number!')
        return accept_f()


def continue_program():  # asks the user if they want to input another set of data
    choice = input("Enter 'y' to enter another set of data, enter 'q' to quit: ")
    if choice == 'y':
        print()
        return uni_progress(main())
    elif choice == 'q':
        return histogram()
    else:
        print("Invalid input! Try 'y' or 'q' ")
        return continue_program()


def histogram():  # - if value >0 the function will print the histogram
    print("------------------------------\nHistogram:")
    if len(var.progress) > 0:
        print(f'Progress {len(var.progress)} : {var.progress}')
    if len(var.trailer) > 0:
        print(f'Module Trailer {len(var.trailer)} : {var.trailer}')
    if len(var.retriver) > 0:
        print(f'Module Retriver {len(var.retriver)} : {var.retriver}')
    if len(var.excluded) > 0:
        print(
            f'Excluded {len(var.excluded)} : {var.excluded}')  # the f sting-easier formating
    sum = len(var.progress) + len(var.trailer) + len(var.retriver) + len(var.excluded)
    print(f'\n{sum} outcomes in total')  # prints out the outcomes and their count
    print("------------------------------\nPart 2:")
    for i, value in enumerate(var.outcome_number2):
        print(f'{var.outcome_name2[i]} - {str(value)[1:-1]}')  # part 2,displays the variables and credits
    print(
        "------------------------------")  # the string removes the square brackets when printed...every variable is with curly brackets when you call it
    file_read()


def file_read():
    txt_file = open('w1889667.txt', 'w+')  # write and read file
    txt_file.write('Part 3:')
    for i, value in enumerate(var.outcome_number2):
        txt_file.write(f'\n{var.outcome_name2[i]} - {str(value)[1:-1]}')
    txt_file.close()
    read_txt_file = open('w1889667.txt', 'r')
    read_line = read_txt_file.read()
    print(read_line)
    read_txt_file.close()
    print("------------------------------\nPart 4: ")
    for i, value in enumerate(var.student_id_holder):
        print(f'{str(value)} : {str(var.student_id_holder[value])} ')


uni_progress(main())
