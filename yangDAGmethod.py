import randomDAG
import copy

def refinefaV(task):
    anceV= randomDAG.findpcoDAG().findpa(task.V, task.E)
    preV = []
    lenV = len(task.V)
    for i in range(0, lenV):
        temp = []
        for j in range(0, i):
            if (j, i) in task.E:
                temp.append(j)
        preV.append(temp)
    # print('preV=',preV)
    faV=copy.deepcopy(preV)
    for i in range(0,lenV):
        for u in preV[i]:
            for v in preV[i]:
                if v !=u:
                    if u in anceV[v]:
                        faV[i].remove(u)
                        break
    # print ("faV=",faV)
    return faV

def cal_wcets(task,s):
    lenV = len(task.V)
    type=task.P
    WT=0
    maxv=0
    for i in range(lenV):
        if task.P[i]==s:
            WT=WT+task.V[i]
            if maxv<task.V[i]:
                maxv=task.V[i]
    return WT,maxv





def findRT(task,Ms):
    lenV = len(task.V)
    E = task.E
    # release offset
    rt= [0 * lenV for i in range(lenV)]
    R = [0 * lenV for i in range(lenV)]
    # RT = [0] * lenV
    preV = refinefaV(task)
    for i in range(lenV):
        # print ("calculating vertex ",i)
        corty = task.P[i]
        mk =Ms[corty-1]
        wcets = cal_wcets(task, corty)
        if i == 0:
            # if it is a source node
            rt[0]=0

            Rt=(1/mk)*wcets[0]+wcets[1]+task.V[i]/2
            R[i]=Rt
        else:
            maxrt=0
            for j in preV[i]:
                curt=rt[j]+R[j]
                if maxrt<curt:
                    maxrt=curt
            rt[i]=maxrt
            if task.V[i]==0:
                Rt=0
            else:
                Rt = (1 / mk) * wcets[0] + wcets[1] + task.V[i] / 2
            R[i] = Rt
    # print("rt=",rt)
    # print("R=", R)
    return R[lenV-1]+rt[lenV-1]
if __name__ == '__main__':
    v = [133,16,83,197,78,0]
    e = [(0, 1), (1, 2), (1, 4),(2,3),(3,5),(4,5)]
    type = [1,2,2,1,1,1]
    MS = [2, 2]
    T = randomDAG.DAGtask(v, e, 500, 500, 0, type)
    rt = findRT(T, MS)
    print("rt=", rt)

