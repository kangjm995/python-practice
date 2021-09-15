jumsu = int(input("점수를 입력해주세요 :"))

if jumsu >= 90 :
    if jumsu >= 97 :
        print("A+")
    elif jumsu >= 94 :
        print("A")
    else :
        print("A-")
elif jumsu >= 80 :
    if jumsu >= 87 :
        print("B+")
    elif jumsu >= 84 :
        print("B")
    else :
        print("B-")
elif jumsu >= 70 :
    if jumsu >= 77 :
        print("C+")
    elif jumsu >= 74 :
        print("C")
    else :
        print("C-")
elif jumsu >= 60 :
    if jumsu >= 67 :
        print("D+")
    elif jumsu >= 64 :
        print("D")
    else :
        print("D-")
else :
    print("F")