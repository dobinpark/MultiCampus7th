def solution(price):
    answer = price
    if price >= 500000:
        answer = price * (1-0.2)
    elif price >= 300000:
        answer = price * (1-0.1)
    elif price >= 100000:
        answer = price * (1-0.05)
    return int(answer)