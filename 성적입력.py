scorelist = []

def high_score():
    temp = 0
    for i in range(5):
        if temp<scorelist[i]:
            temp=scorelist[i]
    return temp
def low_score():
    temp = 101
    for i in range(5):
        if temp>scorelist[i]:
            temp=scorelist[i]
    return temp

    
for i in range(5):
    score = int(input('5명의 성적을 입력하세요:'))
    scorelist.append(score)
s_max = high_score()
s_min = low_score()
print('최고 점수는',s_max,' 점 입니다.')
print('최저 점수는',s_min,' 점 입니다.') 
