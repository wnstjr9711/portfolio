def solution(info, query):
    ans = [0] * len(query)
    data = [i.split() for i in info]
    query = [i.split() for i in query]
    data = [[set(i[:4]), eval(i[4])] for i in data]
    score = [eval(i[7]) for i in query]
    query = [set(i[:7]).difference({'and', '-'}) for i in query]
    print(data)
    print(query)
    for i in range(len(query)):
        temp = list(map(lambda x: x[0].issuperset(query[i]), data))
        for j in range(len(temp)):
            if temp[j] and data[j][1] >= score[i]:
                ans[i] += 1
    return ans







inf = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
que = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(inf, que))