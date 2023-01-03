import sys
input = sys.stdin.readline

w, n = map(int, input().split())
# 보석의 무게와 무게 당 가치를 담은 리스트
jewel = [list(map(int, input().split())) for i in range (n)]
# 무게 당 가치를 우선순위로 두고 정렬
jewel.sort(key=lambda x:x[1], reverse = True)

ans = 0
for weight, price in jewel:
    # 더 담을 수 있다면
    if w > weight:
        ans += weight * price
        w -= weight

    # 보석을 잘라야 한다면
    else:
        ans += w * price
        break

print(ans)