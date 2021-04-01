

def hanoi(num, start, end):
    if num==1:
        print(f'from: {start} to: {end}')
    else:
        hanoi(num-1, start, 6-start-end)
        hanoi(1, start, end)
        hanoi(num-1, 6-start-end, end)





if __name__=="__main__":
    user_input = int(input("원판의 개수를 입력해주세요!"))
    
    print(user_input, '개의 원판을 1번 에서 3번으로 이동시키는 순서입니다')

    hanoi(user_input, 1, 3)



