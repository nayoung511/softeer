import sys
input = sys.stdin.readline

N = int(input()) # 참가자의 수
scores = [list(map(int, input().split())) for i in range (3)]

# 최종 점수
scores.append([0] * N)
for i in range (N):
    for j in range (3):
        scores[3][i] += scores[j][i]

# index 기억 
for i in range (4):
    for j in range (N):
        scores[i][j] = [scores[i][j], j]

print(scores)
# 점수대로 정렬
for i in range (4):
    scores[i].sort(key=lambda x:x[0], reverse=True)
print(scores)
# 등수
results = [[0] * N for i in range (4)]
lastRank = [1] * (N+1)

for i in range (4):
    rank = 1
    count = 1
    for j in range (N-1):
        highest_score = scores[i][j][0]
        
        if highest_score == 0:
            break
        
        idx = scores[i][j][1]
        # 등수를 기록한다
        if results[i][idx] == 0:
            results[i][idx] = rank
        # 최고점을 -1로 초기화한다 (0점이 있을 때 방지)
        scores[i][j][0] = -1

        if highest_score == scores[i][j+1][0]:
            # 동점자
            count += 1
        else:
            rank += count
            count = 1
            lastRank[i] = rank

for i in range (4):
    for j in range (N):
        if results[i][j] == 0:
            print(lastRank[i], end=' ')
        else:
            print(results[i][j],  end=' ')
    print()