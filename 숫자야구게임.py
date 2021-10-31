import random
secretLen = 3

#비밀 숫자 생성
secretList = random.sample(range(10), secretLen)    #0~9 중 33개 추출
secret = ''

for i in range(secretLen) :
    secret += str(secretList[i])    #문자열로 변환

print(secret)       #테스트용


for chance in range(10, 0, -1) :    #10번의 기회
    #추론 숫자 입력
    while True :
        guess = input(("You have %d chance(s). " % chance) + "Guess my three-digit number: ")
        if len(guess) == secretLen and guess.isdigit(): #올바른 입력 시 중단
            break

    print(guess)        #테스트용

    #추론 숫자 분석
    strike = 0      #strike 초기화
    ball = 0        #ball 초기화

    for i in range(secretLen) :
        if secret[i] == guess[i] :
            strike += 1                     #strike 증가
        elif secret[i] in guess :
            ball += 1                       #ball 증가

    print(secret, strike, ball)     #테스트용

    #분석 결과 출력
    if strike == secretLen :
        print("You guessed my number!!")
        break
    if strike > 0 :
        if ball > 0 :
            print("%d strike(s) and %d ball(s)\n" % (strike, ball))
        else :
            print("%d strike(s)\n" % strike)
    else :
        if ball >0 :
            print("%d ball(s)\n" % ball)
        else :
            print("Out\n")
else :
    print("You failed to guess my number..")