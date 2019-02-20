import os, sys
import pickle as pk
from scheduler import Schedule, INT_TO_DOW

MAX_SHIFT_COUNT = 50 # student can only work 20 hours a week...


# class Shift:
#     def __init__(self, day, prev=None):
#         self.empl = [None, None, None]
#         self.score = 0
#         self.next = None
#         self.prev = None
#         if prev:
#             self.prev = prev
#             prev.next = self
#
#     def __str__(self):
#         ret = ""
#         for per in self.empl:
#             if not per:
#                 ret += "<empty>, "
#                 continue
#             ret += per + ", "
#         return ret[:-2]
#
#     def isEmpty(self):
#         return len([1 for i in self.empl if i==None]) == 3
#
#     def getScore(self):
#         return self.score
#
#     def getEmplNames(self):
#         return self.empl
#
#     def insert(self, slot, pers):
#         if slot > 2:
#             return 1
#         else:
#             if not self.empl[slot] and self.isAssigned(pers):
#                 self.empl[slot] = pers[1]
#                 self.score += pers[0]
#                 return 0
#             else:
#                 return 1
#
#     def isAssigned(self, pers):
#         return pers in self.empl
#
#     def hasShiftBefore(self, pers):
#         if self.prev:
#            return self.prev.isAssigned(pers)
#     #
#     # def remove(self,slot):
#     #     if slot > 2:
#     #         return -1
#     #     else:
#     #         self.empl[slot] = None
#     #         return 0
#
#
# class MasterSchedule:
#     def __init__(self):
#         self.shifts = [[],[],[]]
#         self.masterSched = [[[],[],[]] for _ in range(5)] + [[[],[]] for _ in range(2)]
#         self.scheds = {}
#         self.point = 0
#         self.retSched = [[Shift(i) for i in range(3)] for _ in range(5)] + [[Shift(j) for j in range(2)] for _ in range(2)]
#     def __copysched(self, origin):
#         return [[j for j in i] for i in origin]
#
#     def __gensched(self, curSched, day, shift, nameCnt):
#         ret = []
#         for choice in self.masterSched[day][shift]:
#             if nameCnt[choice[1]] >= MAX_SHIFT_COUNT:
#                 continue
#             for i in range(3):
#                 nextSched = self.__copysched(curSched)
#                 if not nextSched[0][0].isEmpty():
#                     if shift > 0:
#                         if choice[1] in nextSched[day][shift-1].getEmplNames() :
#                             continue
#                     else:
#                         if choice[1] in nextSched[day-1][-1].getEmplNames():
#                             continue
#                 if nextSched[day][shift].insert(i, choice):
#                     continue
#                 nameCnt[choice[1]] += 1
#                 if (shift < 2 and day <= 4) or (shift < 1 and day > 4):
#                     ret += (self.__gensched(nextSched, day, shift + 1, nameCnt))
#                 elif day < 6:
#                     ret += (self.__gensched(nextSched, day + 1, 0, nameCnt))
#                 else:
#                     # print("appended")
#                     ret.append((1, nextSched))
#                 nameCnt[choice[1]] -= 1
#         return ret
#
#
#     def loadSched(self):
#         for _, _, files in os.walk("."):
#             for file in files:
#                 # print(file)
#                 if file.endswith(".sched"):
#                     with open(file, "rb") as f:
#                         s = pk.load(f)
#                         self.scheds[s.getName()] = s
#         # print(self.scheds)
#
#
#         for name, sched in self.scheds.items():
#             curday = 0
#             for shiftsPerDay in sched:
#                 curshift = 0
#                 for shift in shiftsPerDay:
#                     if shift:
#                         self.masterSched[curday][curshift].append((shift,sched.getName()))
#                     curshift +=1
#                 curday+=1
#
#     def getMasterSched(self):
#         # Check if we have at least 3 options per shift
#         for day in range(len(self.masterSched)):
#             for options in self.masterSched[day]:
#                 # print("options: ", options)
#                 if len(options) < 1:
#                     print("FATAL: not enough option per shift")
#                     return -1
#         res = self.__gensched(self.retSched, 0, 0, {name:0 for name in self.scheds.keys()})
#         print("hello")
#         for sched in res:
#             for day in sched[1]:
#                 for shift in day:
#                     print(shift)
#         # if res:
#         #     maxScore = max(res)[0]
#         #     nSched = 1
#         #     for score, sched in res:
#         #         if score == maxScore:
#         #             print("Schedule #"+str(nSched)+"  Score:"+str(score))
#         #             for i in range(7):
#         #                 print(INT_TO_DOW[i] + ' ' + str(name for name in sched[i]))
#         #             nSched+=1
#         # else:
#         #     print("FATAL: Not enough people; hire more!")
#
#
#
#
#
#
#
#
#
#
#
# ms = MasterSchedule()
# ms.loadSched()
# ms.getMasterSched()

class Employee:
    def __init__(self, schedObj):
        self.name = schedObj.name
        self.sched = schedObj.schedule
        self.prefShifts = [(i,j) for i in range(len(self.sched))for j in range(len(self.sched[i])) if self.sched[i][j] == 2]
        # self.prefNumSftCnt = schedObj.prefNumOfSft TODO: Implement preferred number of shifts in scheduler.py
        self.assignedShift = []
        # self.xp = schedObj.xp TODO: Implement xp input in scheduler.py

    def _getPoint(self):
        pass
        # experience = self.xp - 1 TODO: Implement self.xp





class ShiftOfDay:
    def __init__(self, day, sftCnt, perCnt=(3,3,3)):
        self.day = day
        self.shifts = [[None for _ in range(perCnt[i])] for i in range(sftCnt)]
        self.sftCnt = sftCnt
        self.perCnt = perCnt
    def getShifts(self, name):
        ret = []
        print(self.shifts)
        for shiftIdx in range(self.sftCnt):
            for nameIdx in range(self.perCnt[shiftIdx]):
                if self.shifts[shiftIdx][nameIdx] == name:
                    ret.append((self.day, shiftIdx))



class MasterSchedule:
    def __init__(self, sftPerDay=(3,3,3,3,3,2,2)):
        self.shifts = [ShiftOfDay(i, sftPerDay[i]) for i in range(7)]
        self.rawSched = []

    def loadScheds(self):
        for _, _, files in os.walk("."):
            for file in files:
                # print(file)
                if file.endswith(".sched"):
                    with open(file, "rb") as f:
                        s = pk.load(f)
                        self.rawSched.append(Employee(s))


ms = MasterSchedule()
ms.loadScheds()
pass