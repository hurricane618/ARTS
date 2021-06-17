# 拓扑排序的问题
# 采用优先队列实现
from queue import PriorityQueue

class Solution:
    def compileSeq(self , input ):
        # write code here
        data_list = input.split(",")
        l = len(data_list)
        pre = []
        vis = [False]*l
        queue = PriorityQueue(l)
        n = 0
        result = ""
        for data in data_list:
            pre.append(int(data))
            if data == '-1':
                queue.put(n)
            n += 1
        #print(pre)
        #print(queue.queue)
        while not queue.empty() :
            q = queue.get()
            vis[q] = True
            result += str(q)
            result += ","
            n = 0
            for p in pre:
                if not vis[n] and pre[n] == q:
                    pre[n] = -1
                    queue.put(n)
                n += 1
        return result[:-1]


s = Solution()
print(s.compileSeq("5,0,4,4,5,-1"))
