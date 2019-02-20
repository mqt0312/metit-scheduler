import os, sys
import pickle as pk
from scheduler import Schedule, INT_TO_DOW

MAX_SHIFT_COUNT = 50 # student can only work 20 hours a week...


class MasterSchedule:
    def __init__(self):
        self.shifts = [[],[],[]]
        self.masterSched = [[[],[],[]] for _ in range(5)] + [[[],[]] for _ in range(2)]
        self.scheds = {}
        self.point = 0
        self.retSched = [[None,None,None] for _ in range(5)] + [[None,None] for _ in range(2)]
    def __copysched(self, origin):
        return [[j for j in i] for i in origin]

    def __genemptysched(self):
        return [[None,None,None] for _ in range(5)] + [[None,None] for _ in range(2)]


    def __getScoreDup(self, sched):
        score = 0
        for person, _ in self.scheds.items():
            perCount = 0
            for day in sched:
                for shift in day:
                    if shift[0] == person:
                        perCount +=1
            if perCount in [MAX_SHIFT_COUNT-1,MAX_SHIFT_COUNT]:
                score += 6
            elif perCount in [MAX_SHIFT_COUNT-2]:
                score += 2
            else:
                score -= 10
        return score
    def __getSum(self, sched):
        score = 0
        for day in sched:
            for shift in day:
                score += shift[0]
        return score + self.__getScoreDup(sched)
    def __gensched(self, currentSched, curDay, curShift, nameCount):
        ret = []
        for choice in self.masterSched[curDay][curShift]:

            if nameCount[choice[1]] >= MAX_SHIFT_COUNT:
                continue

            nextSched = self.__copysched(currentSched)
            if nextSched[0][0]:
                if curShift > 0:
                    if nextSched[curDay][curShift-1][1] == choice[1]:
                        continue
                else:
                    if nextSched[curDay-1][-1][1] == choice[1]:
                        continue
            nextSched[curDay][curShift]=choice
            nameCount[choice[1]]+=1
            # print(nextSched)
            if (curShift < 2 and curDay <= 4) or (curShift < 1 and curDay > 4) :
                ret+=(self.__gensched(nextSched, curDay, curShift+1, nameCount))
            elif curDay < 6:
                ret+=(self.__gensched(nextSched, curDay+1, 0, nameCount))
            else:
                # print("appended")
                ret.append((self.__getSum(nextSched), nextSched))
            nameCount[choice[1]] -= 1
        return ret

    def loadSched(self):
        for _, _, files in os.walk("."):
            for file in files:
                # print(file)
                if file.endswith(".sched"):
                    with open(file, "rb") as f:
                        s = pk.load(f)
                        self.scheds[s.getName()] = s
        # print(self.scheds)


        for name, sched in self.scheds.items():
            curday = 0
            for shiftsPerDay in sched:
                curshift = 0
                for shift in shiftsPerDay:
                    if shift:
                        self.masterSched[curday][curshift].append((shift,sched.getName()))
                    curshift +=1
                curday+=1
        # print(self.masterSched)


    def getMasterSched(self):
        # Check if we have at least 3 options per shift
        for day in range(len(self.masterSched)):
            for options in self.masterSched[day]:
                # print("options: ", options)
                if len(options) < 1:
                    print("FATAL: not enough option per shift")
                    return -1
        res = self.__gensched(self.retSched, 0, 0, {name:0 for name in self.scheds.keys()})
        # print(max(res)[0])
        if res:
            maxScore = max(res)[0]
            nSched = 1
            for score, sched in res:
                if score == maxScore:
                    print("Schedule #"+str(nSched)+"  Score:"+str(score))
                    for i in range(7):
                        print(INT_TO_DOW[i] + ' ' + str([name[1] for name in sched[i]]))
                    nSched+=1
        else:
            print("FATAL: Not enough people; hire more!")











ms = MasterSchedule()
ms.loadSched()
ms.getMasterSched()
