def chk_number(number):
    # 3 ≤ number의 길이 ≤ 13
    if len(number) < 3 or len(number) > 13:
        return -1
    # -1,000 ≤ number의 각 원소 ≤ 1,000
    for num in number:
        if num < -1000 or num > 1000:
            return -1
    
    return 0

def solution(number):
    # 문제의 조건 확인
    chk_number(number)
    
    answer = 0
    
    for idx in range(len(number)):
        for idx2 in range(idx+1, len(number)):
            for idx3 in range(idx2+1, len(number)):
                if number[idx] + number[idx2] + number[idx3] == 0:
                    answer += 1
        
    return answer
