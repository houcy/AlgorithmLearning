class Solutionold:
    def findItinerary(self, tickets: list) -> list:
        map = {}
        for i in tickets:
            if not i[0] in map.keys():
                map[i[0]] = []
                map[i[0]].append(i[1])
            else:
                j = 0
                while j < len(map[i[0]]) and map[i[0]][j] < i[1]:
                    j += 1
                map[i[0]].insert(j, i[1])
        res = []
        tmp = 'JFK'
        while tmp in map.keys():
            res.append(tmp)
            if map[tmp]:
                tmp = map[tmp].pop(0)
            else:
                break
        if not tmp in map.keys():
            res.append(tmp)
        return res
import collections
'''1.比较容易理解的方式：'''
# 类似大部分基本深搜，每次对当前出发点的“剩余可用目的地”循环，优先去名字值小的
# 但无论以递归入参还是全局变量的方式，每次进递归需层数+1，选择的ticket要暂时标为已用，即当前form-to的剩余可用次数-1
# 结束条件是层数达到完全遍历，若未达到又无可用目的地，说明这条路走不通了，回溯时需还原层数、可用次数

'''2.更烧脑但更简洁的方式：'''
# 因题目强调了“假定所有机票至少存在一种合理的行程”，所以可利用深搜一定会有结果这一点，无需任何标记、判定，仅单纯对每层进行循环及扣除
# 也就是每次进递归，还是对当前“剩余可用目的地”循环，但选择名字值小的进入下层时直接扣除这张机票
# 这样任意循环若还能进行，说明还有机票没用；反之一定是“基于已经出现的终点，自身成为更早部分的终点”
# 这里有点绕，举例来说第一个结束循环的一定是唯一一个这样的机场：他作为机票的终点的总次数，比作为起点的总次数多1
# 也就是说JFK恰好是唯一相反的机场，而其它机场作为起点和终点的总次数一定相同
# 所以最早结束循环的递归，一定是入参为终点时，将其加入行程数组；第二个出现的，则是之前行程中，唯一可作为终点的
# 以此类推……最后行程数组反向，即为答案

class Solution:
    def findItinerary(self, tickets: list) -> list:
        paths = collections.defaultdict(list)
        for start, tar in tickets:
            paths[start].append(tar)
        for start in paths:
            paths[start].sort(reverse=True)
        s = []

        def search(start):
            while paths[start]:
                search(paths[start].pop())
            s.append(start)

        search("JFK")
        return s[::-1]
        
s = Solution()
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))