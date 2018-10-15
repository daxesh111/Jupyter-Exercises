leng= input().split()
sets = set(map(int, input().split()))
liked = set(map(int, input().split()))
disliked = set(map(int, input().split()))
h_lik = 0
h_dis = 0
total = 0
for i in liked:
    if i in sets:
        h_lik = h_lik+1

for i in disliked:
    if i in sets:
        h_dis = h_dis-1
total = h_lik+h_dis
print(total)
