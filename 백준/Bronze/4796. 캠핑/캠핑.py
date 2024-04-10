i = 0
while True:
    L, P, V = map(int, input().split())
    i += 1
    date = 0
    if L == 0:
        break    
    date = V // P * L + min(V % P,L)
    print(f"Case {i}: {date}")
