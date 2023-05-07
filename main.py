import multiprocessing as mp
import os
import time
from sage.rings.real_mpfr import RRtoRR
rr = RealField(1000)

#cpuCore=os.cpu_count()
cpuCore=8

class betacalc:
    betaSum=0
    def __init__(self, betaSum,index):
        self.betaSum=betaSum
        self.index=index
    def point(self):
        return self.betaSum
    def __str__(self):
        return "{"+str(self.index)+";"+str(self.betaSum)+"}";
        
def betaCalcThread(index,cores,que,m):
    #aici este functia 
    que.append(listaBetaAlpha)

if __name__ == "__main__":
    manager=mp.Manager()
    que=manager.list()
    threadApp=[None]*cpuCore
    m=20
    #print(len(threadApp))
    timpPerformanta=time.perf_counter()
    
    for i in range(0,cpuCore):
        threadApp[i]=mp.Process(target=betaCalcThread,args=(i,cpuCore,que,m,))
    for i in range(0,cpuCore):
        threadApp[i].start()
    for i in range(0,cpuCore):
        threadApp[i].join()
    
    final_list=[]
    for i in que:
        final_list.append(i)
#     print(que)
    timpPerformanta=time.perf_counter()-timpPerformanta
    print("gata, timp :",timpPerformanta)
