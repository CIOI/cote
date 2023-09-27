from collections import defaultdict 
'''
BFS 방법이라고 생각하면된다.
1. cases 는 온도를 key, 그 온도에 도달하기위한 최소 소비전력을 value로 갖는다.
2. nextstep 은 cases 에 존재하는 모든 온도를 +1 0 -1 변화시켰을때 얻을 수 있는 모든 [온도:소비전력] 쌍이다.
   가능한 소비전력이 하나 이상이기 때문에 소비전력은 list로 저장한다.
3. nextstep 의 온도를 key, 소비전력 list 중 최소 값을 value 로 하도록 cases 를 업데이트 한다.
4. 만약 onboard[t] 가 1 이라면 t1~t2 사이에 있지 않는 모든 cases key:value 쌍을 삭제한다.
5. iteration 이 끝났을 때 cases.values 의 최소값을 return 하면 그것이 정답!
    ex) Q: temperatrue:28	t1=18	t2=26	a=10	b=8	onboard=[0, 0, 1, 1, 1, 1, 1]
        t가 1일 때 업데이트 하는 과정:
        - 먼저 첫번째 step(t=0 -> t=1) 에서 cases 는 {28:[0]} -> {27: [10], 28: [0]} 가 되었다.
        - cases 에 존재하는 온도는 27, 28 이므로
        - 먼저 27의 경우에 모든 가능한 key value 쌍은 {26: [20] 27: [18], 28: [10]}
        - 28의 경우에 {27: [10], 28: [0]}
        - 이처럼 각 온도에 대해 중복된 값이 존재함으로 nextstep 은 defaultdict(list) 로 만들었다.
        - nextstep = {26: [20], 27: [18, 10], 28: [10, 0]}
        - cases(t=1) = {26: 20, 27: 10, 28: 10}
        
이렇게 하면 최종 cases 는 각 온도에서 가능한 최소의 소비전력을 나타내는 dict 이고
그 key 는 가능한 온도만 남게된다.
'''
def upper(temperature,t1,t2,a,b,onboard):
    cases=dict() #첫번째에만 cases dict 생성 -----(1)
    cases[temperature]=0
    for t in range(len(onboard)):
        pre_tems=list(cases.keys())
        nextstep=defaultdict(list) #매스텝 nextstep을 초기화 ------(2)
        for pre_tem in pre_tems:
            if pre_tem==temperature:
                nextstep[pre_tem-1].append(cases[pre_tem]+a)
                nextstep[pre_tem].append(cases[pre_tem])
            else:
                nextstep[pre_tem-1].append(cases[pre_tem]+a)
                nextstep[pre_tem].append(cases[pre_tem]+b)
                nextstep[pre_tem+1].append(cases[pre_tem])
        cases=dict() #cases 초기화
        for temp in nextstep.keys():
            cases[temp]=min(nextstep[temp])
        if onboard[t]==1:
            keylist=list(cases.keys())
            for key in keylist:
                if key<t1 or key>t2:
                    del cases[key]
    return min(cases.values())

def lower(temperature,t1,t2,a,b,onboard):
    cases=dict() #첫번째에만 cases dict 생성
    cases[temperature]=0
    for t in range(len(onboard)):
        pre_tems=list(cases.keys())
        nextstep=defaultdict(list)
        for pre_tem in pre_tems:
            if pre_tem==temperature:
                nextstep[pre_tem+1].append(cases[pre_tem]+a)
                nextstep[pre_tem].append(cases[pre_tem])
            else:
                nextstep[pre_tem+1].append(cases[pre_tem]+a)
                nextstep[pre_tem].append(cases[pre_tem]+b)
                nextstep[pre_tem-1].append(cases[pre_tem])
        cases=dict() #cases 초기화
        for temp in nextstep.keys():
            cases[temp]=min(nextstep[temp])
        if onboard[t]==1:
            keylist=list(cases.keys())
            for key in keylist:
                if key<t1 or key>t2:
                    del cases[key]
    return min(cases.values())

def solution(temperature, t1, t2, a, b, onboard):
    answer=2
    if temperature > t2:
        answer=upper(temperature,t1,t2,a,b,onboard)
    else:
        answer=lower(temperature,t1,t2,a,b,onboard)
    return answer

print(solution(11,	8,	10,	10,	1,	[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))