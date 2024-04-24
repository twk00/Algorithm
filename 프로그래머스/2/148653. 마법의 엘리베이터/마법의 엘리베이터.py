def solution(storey):
    answer = 0
    place = 1
    
    while storey > 0:
        current_digit = storey % 10
        
        # 올림이나 내림 결정
        if current_digit == 5:
            # 다음 자릿수를 확인하여 올림/내림 결정
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                # 5 이상인 경우 올림
                answer += (10 - current_digit)
                storey += 10
            else:
                # 5 미만인 경우 내림
                answer += current_digit
        elif current_digit > 5:
            # 5 초과인 경우 올림
            answer += (10 - current_digit)
            storey += 10
        else:
            # 5 미만인 경우 내림
            answer += current_digit
        
        # 다음 자릿수로 이동
        storey //= 10
        place *= 10
    
    return answer
