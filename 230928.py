def combination(k:int,n:int,li:list=[])->list:
    if li==[]:
        global glo
        global total
        glo=[]
        total = n
    if k==0:
        if sum(li)==total:
            glo.append([num + 1 for num in li])
        return
    if n==0:
        a=li.copy()
        a.append(0)
        combination(k-1,n,a)
    else:
        for i in range(n+1):
            a=li.copy()
            a.append(i)
            combination(k-1,n-i,a)
    return glo        

def gettime(k:int,counselor:list,reqs:list)->int:
    '''
    counselor 배치에 따른 대기시간을 반환
    '''
    wait_time=0
    div_reqs=[]
    for i in range(k):
        div_reqs.append([])
    print(div_reqs)
    for req in reqs:
        div_reqs[req[2]-1].append(req)
    print('check',div_reqs)
    for i in range(len(counselor)):
        wait=[0 for i in range(counselor[i])] #[0,0]
        for customer in (div_reqs[i]):
            if min(wait)<=customer[0]:
                wait[wait.index(min(wait))]=customer[0]+customer[1]
            else:
                wait_time+=min(wait)-customer[0]
                wait[wait.index(min(wait))]=min(wait)+customer[1]
    return wait_time
                
                
        
    


def solution(k, n, reqs):
    #조합 만들기, 일단 무조건 하나 씩은 있어야하고
    combi = combination(k,n-k)
    print(combi)
    time_list=[]
    for i in range(len(combi)):
        time_list.append(gettime(k,combi[i],reqs))
    answer = min(time_list)
    return answer


#test
print('the result',solution(3,	5,	[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))

# solution1 모든 조합의 기다린 시간을 구해서 min 뽑기
# solution2 생각안남 ;;

