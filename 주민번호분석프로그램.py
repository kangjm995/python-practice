#num_list에 주민번호 한 숫자씩 , 이용해서 개별적으로 저장
num_list = [x for x in input("주민번호를 한 숫자씩 ,를 사용하며 입력하세요 : ").split(",")]

#sum_proofnum 변수에 주민번호검증 공식을 이용하여 검증공식에 쓰이는 합 구함
sum_proofnum = (int(num_list[0])*2 + int(num_list[1])*3 + int(num_list[2])*4 + int(num_list[3])*5 + int(num_list[4])*6 + int(num_list[5])*7 + int(num_list[6])*8 
+ int(num_list[7])*9 +int(num_list[8])*2 + int(num_list[9])*3 + int(num_list[10])*4 + int(num_list[11])*5)

#검증공식으로 도출되는 숫자인 주민번호의 13 번째 숫자를 proofnum1에 저장.
proofnum1 = int(num_list[12])

#검증공식을 이용하여 주민번호의 13번째 숫자가 올바른 번호인지 확인
proofnum2 = 11- (int(sum_proofnum) % 11)

if proofnum2 == 11 :
    proofnum2 = 1
if proofnum2 == 10 :
    proofnum2 = 0

#존재하는 주민번호면 주민번호 분석하고, 존재하지 않는 주민번호면 존재하지 않는다고 출력.
if proofnum1 != proofnum2 :
    print("존재하지 않는 주민번호입니다.")
else :
    #생년월일 출력
    print("생년월일 : %s%s년 %s%s월 %s%s일" % (num_list[0], num_list[1], num_list[2], num_list[3], num_list[4], num_list[5]))

    #성별, 내/외국인 여부 출력
    if num_list[6] == '1' or num_list[6] == '3' :
        print("성별 : 남자\n내국인")
    elif num_list[6] == '2' or num_list[6] == '4' :
        print("성별 : 여자\n내국인")
    elif num_list[6] == '9' or num_list[6] == '0' :
        print("노인")
    else :
        print("외국인")

    #내국인일 경우
    while num_list[6] == '1' or num_list[6] == '3' or num_list[6] == '2' or num_list[6] == '4' :
        #출생등록지 출력
        if (num_list[7:9] == ['0', '0'] or num_list[7:9] == ['0', '1']
    or num_list[7:9] == ['0', '2'] or num_list[7:9] == ['0', '3'] 
    or num_list[7:9] == ['0', '4'] or num_list[7:9] == ['0', '5'] 
    or num_list[7:9] == ['0', '6'] or num_list[7:9] == ['0', '7'] 
    or num_list[7:9] == ['0', '8'])  :
            print("출생등록지 : 서울")
        elif (num_list[7:9] == ['0', '9'] or num_list[7:9] == ['1', '0']
    or num_list[7:9] == ['1', '1'] or num_list[7:9] == ['1', '2']) :
            print("출생등록지 : 부산")
        elif (num_list[7:9] == ['1', '3'] or num_list[7:9] == ['1', '4']
    or num_list[7:9] == ['1', '5']) :
            print("출생등록지 : 인천")
        elif (num_list[7:9] == ['1', '6'] or num_list[7:9] == ['1', '7']
    or num_list[7:9] == ['1', '8'] or num_list[7:9] == ['1', '9'] 
    or num_list[7:9] == ['2', '0'] or num_list[7:9] == ['2', '1'] 
    or num_list[7:9] == ['2', '2'] or num_list[7:9] == ['2', '3'] 
    or num_list[7:9] == ['2', '4'] or num_list[7:9] == ['2', '5']) :
            print("출생등록지 : 경기도")
        elif (num_list[7:9] == ['2', '6'] or num_list[7:9] == ['2', '7']
    or num_list[7:9] == ['2', '8'] or num_list[7:9] == ['2', '9'] 
    or num_list[7:9] == ['3', '0'] or num_list[7:9] == ['3', '1'] 
    or num_list[7:9] == ['3', '2'] or num_list[7:9] == ['3', '3'] 
    or num_list[7:9] == ['3', '4']) :
            print("출생등록지 : 강원도")
        elif (num_list[7:9] == ['3', '5'] or num_list[7:9] == ['3', '6']
    or num_list[7:9] == ['3', '7'] or num_list[7:9] == ['3', '8'] 
    or num_list[7:9] == ['3', '9']) :
            print("출생등록지 : 충청북도")
        elif num_list[7:9] == ['4', '0'] :
            print("출생등록지 : 대전")
        elif (num_list[7:9] == ['4', '1'] or num_list[7:9] == ['4', '2']
    or num_list[7:9] == ['4', '3'] or num_list[7:9] == ['4', '5'] 
    or num_list[7:9] == ['4', '6'] or num_list[7:9] == ['4', '7']) :
            print("출생등록지 : 충청남도")
        elif num_list[7:9] == ['4', '4'] or num_list[7:9] == ['9', '6'] :
            print("출생등록지 : 세종")
        elif (num_list[7:9] == ['4', '8'] or num_list[7:9] == ['4', '9']
    or num_list[7:9] == ['5', '0'] or num_list[7:9] == ['5', '1'] 
    or num_list[7:9] == ['5', '2'] or num_list[7:9] == ['5', '3'] 
    or num_list[7:9] == ['5', '4']) :
            print("출생등록지 : 전라북도")
        elif num_list[7:9] == ['5', '5'] or num_list == ['5', '6'] :
            print("출생등록지 : 광주")
        elif (num_list[7:9] == ['5', '7'] or num_list[7:9] == ['5', '8']
    or num_list[7:9] == ['5', '9'] or num_list[7:9] == ['6', '0'] 
    or num_list[7:9] == ['6', '1'] or num_list[7:9] == ['6', '2'] 
    or num_list[7:9] == ['6', '3'] or num_list[7:9] == ['6', '4'] 
    or num_list[7:9] == ['6', '5'] or num_list[7:9] == ['6', '6']) :
            print("출생등록지 : 전라남도")
        elif (num_list[7:9] == ['6', '7'] or num_list[7:9] == ['6', '8']
    or num_list[7:9] == ['6', '9'] or num_list[7:9] == ['7', '0']) :
            print("출생등록지 : 대구")
        elif (num_list[7:9] == ['7', '1'] or num_list[7:9] == ['7', '2']
    or num_list[7:9] == ['7', '3'] or num_list[7:9] == ['7', '5'] 
    or num_list[7:9] == ['7', '6'] or num_list[7:9] == ['7', '7']
    or num_list[7:9] == ['7', '8'] or num_list[7:9] == ['7', '9']
    or num_list[7:9] == ['8', '0'] or num_list[7:9] == ['8', '1']) :
            print("출생등록지 : 경상북도")
        elif (num_list[7:9] == ['8', '2'] or num_list[7:9] == ['8', '3']
    or num_list[7:9] == ['8', '4'] or num_list[7:9] == ['8', '6'] 
    or num_list[7:9] == ['8', '7'] or num_list[7:9] == ['8', '8'] 
    or num_list[7:9] == ['8', '9'] or num_list[7:9] == ['9', '0']) :
            print("출생등록지 : 경상남도")
        elif num_list[7:9] == ['8', '5'] :
            print("출생등록지 : 울산")
        else :
            print("출생등록지 : 제주도")

        #몇 번쨰로 접수했는지
        print("%s 번 째로 접수됨" % num_list[11])
        break
