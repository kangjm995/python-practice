def find_name(num, nolist, namelist) :
    lens = len(nolist)
    result = "?"

    for i in range(lens) :
        if nolist[i] == num :
            result = namelist[i]
    return result

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
a = 0

while True :
    print(stu_no)
    a = int(input("학생번호를 입력하세요(-1은 끝내기) : "))
    
    if a != -1 :
        print(find_name(a, stu_no, stu_name))
    else :
        break