def solution(s):
    answer = 0
    stack = []
    
    for item in s.split():
        if item != 'Z':
            num = int(item)
            answer += num
            stack.append(num)
        else:
            if stack:
                answer -= stack.pop()
    
    return answer
