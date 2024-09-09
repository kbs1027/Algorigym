def solution(genres, plays):
    answer = []
    gp = list(zip(genres, plays))
    gpl = [(g,p) for g,p in enumerate(plays)]
    gpd = dict()
    
    for i in range(len(genres)):
        if genres[i] in gpd:
            gpd[genres[i]].append(list(gpl[i]))
        else:
            gpd[genres[i]] = []
            gpd[genres[i]].append(list(gpl[i]))
    
    sq = sequence(gp)
    
    lt = []
    for i in range(len(sq)):
        lt = gpd[sq[i]]
        lt = sorted(lt, key=lambda x:x[1], reverse = True)
        if len(lt) < 2:
            answer.append(lt[0][0])
        else:
            for j in range(2):
                answer.append(lt[j][0])

    return answer

def sequence(gp):
    d = dict()
    lt = []
    for g, p in gp:
        if g in d:
            d[g] += p
        else:
            d[g] = p
    d = sorted(d.items(), key=lambda x:x[1], reverse =True)
    for i in d:
        lt.append(i[0])
    return lt
    