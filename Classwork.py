def main():
    # exer1()
    # exer2()
    exer3()

def exer1():
    i = 0
    while i <= 6:
        if i == 3:
            i += 1
            continue

        elif i == 6:
            i +=1
            continue

        else:
            print(i)
            i += 1
def exer2():
    even = 0
    odd = 0
    for x in range(1, 9, 1):
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Number of even numbers is", even)
    print("Number of odd numbers is", odd)
def exer3():
    while 1==1:
        user = input("Enter a sentence.")
        if user == "":
            break
        else:
            print(user)




if __name__ == '__main__':
    main()