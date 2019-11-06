import time
import numpy as np
import random as rd
import statistics as stat
DEBUG = 1
TIMESTAMP = time.time()
DAY_PER_WEEK = 6
SHIFT_PER_DAY = 3
EMP_PER_SHIFT = 3
SHIFT_SLOTS = [3,3,2,3,3,2,3,3,2,3,3,2,3,3,2,2,2]
NUM_OF_EMPL = 10


class Shift:
    def __init__(self, dt, score, name=""):
        self.dt = dt
        self.score = score
        self.name = name
    def __repr__(self):
        return self.name + ":" + str(self.dt) + ":" + str(self.score)
    def __str__(self):
        return repr(self)
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.dt, self.name) == (other.dt, other.name)
        return NotImplemented
    def __hash__(self):
        return (hash(self.dt) ^ hash(self.name))
    def getDT(self):
        return self.dt
    def getScore(self):
        return self.score
    def getName(self):
        return self.name

def cmp_shift(s1, s2):
    return s1.getDT() < s2.getDT()

def checkValidity(table, idx, ):
    pass



def binarySearch(shifts, start_index):
    lo = 0
    hi = start_index - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if cmp_shift(shifts[mid], shifts[start_index]):
            if cmp_shift(shifts[mid+1], shifts[start_index]):
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

def schedule(shifts, maxRecursion=120):
    if not maxRecursion:
        print("FATAL: No possible schedule. Exiting")
        return
    shifts = rd.sample(shifts, len(shifts))
    shifts = sorted(shifts, key=lambda j: j.getDT())
    n = len(shifts)
    table = [[0, []] for _ in range(n)]
    table[0] = [shifts[0].getScore(), [shifts[0]]]
    for i in range(1, n):

        inclProf = [shifts[i].getScore(), [shifts[i]]]
        l = binarySearch(shifts, i)
        if (l != -1):
            inclProf[0] += table[l][0]
            inclProf[1] += table[l][1]
        table[i][0] = inclProf[0] if inclProf[0] >= table[i - 1][0] else table[i - 1][0]
        table[i][1] = [i for i in inclProf[1]] if inclProf[0] >= table[i - 1][0] else [i for i in table[i - 1][1]]

    emp_cnt = getEmpCountPerShift(shifts)

    for entry in table:
        shf_cnt = getShiftCountPerEmp(entry[1])
        entry[0] += (- sum([100 for i in shf_cnt if i==0]) # Penalize fatally for invalid schedule. TODO: replace this with a function to check invalid schedule (no emp on a shift, no shift for an emp, one emp has illegal num of shifts,...)
                     - 9*stat.stdev(shf_cnt) # Penalize if deviation of num of shifts per employee is large because one person may have lots of shifts while others don't.
                     + 2*stat.stdev(emp_cnt)) # Reward if deviation of employee per shift is large because that is out of control and can affect the space of possible schedules

    table = sorted(table, key=lambda s: s[0])
    # print(table)
    if table[n - 1][0] < 0:
        return schedule(shifts, maxRecursion-1)
    return table[n - 1]

def shf_dt_to_idx(dt):
    return dt[0]*(SHIFT_PER_DAY) + dt[1]

def getEmpCountPerShift(shifts, specific_shift=None):
    if specific_shift:
        return len(list(filter(lambda s: s.getDT() == specific_shift, shifts)))
    emp_cnt = [0 for _ in range(SHIFT_PER_DAY * DAY_PER_WEEK)]
    for x in range(DAY_PER_WEEK):
        for y in range(SHIFT_PER_DAY):
            emp_cnt[shf_dt_to_idx((x, y))] = len(list(filter(lambda s: s.getDT() == (x, y), shifts)))
    return emp_cnt

def getShiftCountPerEmp(sched, specific_emp=None):
    if specific_emp:
        return len(list(filter(lambda s: s.getName() == specific_emp, sched)))
    shf_cnt = [0 for _ in range(NUM_OF_EMPL)]
    for i in range(NUM_OF_EMPL):
        shf_cnt[i] = len(list(filter(lambda s: s.getName() == str(i), sched)))
    return shf_cnt

def genShift():
    dt = (rd.randint(0,DAY_PER_WEEK-1), rd.randint(0,SHIFT_PER_DAY-1))
    # while dt[0] == 2:
    #     dt = (rd.randint(0,DAY_PER_WEEK-1), rd.randint(0,SHIFT_PER_DAY-1))
    prof = rd.randint(1,5)
    name = str(rd.randint(0,NUM_OF_EMPL-1))
    return Shift(dt,prof, name)
shifts = set()
while len(shifts) < 10*NUM_OF_EMPL:
    shifts.add(genShift())



# print(shifts)
# print(sorted(shifts, key=lambda j: j.getDT()))

print("Input:")
for i in range(NUM_OF_EMPL):
    print(list(filter(lambda s: s.getName()==str(i), shifts)))
print("Employee per shift")
for x in range(DAY_PER_WEEK):
    for y in range(SHIFT_PER_DAY):
        print(list(filter(lambda s: s.getDT() == (x, y), shifts)))
print(getEmpCountPerShift(shifts))
output1 = []
for _ in range(50):
    output1.append(schedule(shifts))
output1 = max(output1,key=lambda s: s[0])
print("Best profit:")
print(output1)
for i in range(NUM_OF_EMPL):
    print(list(filter(lambda s: s.getName()==str(i), output1[1])))
    # if output1:
    #     print("Best profit:")
    #     print(output1)
    #     for i in range(NUM_OF_EMPL):
    #         print(list(filter(lambda s: s.getName()==str(i), output1[1])))
print("Employee per shift")
for x in range(DAY_PER_WEEK):
    for y in range(SHIFT_PER_DAY):
        print(list(filter(lambda s: s.getDT() == (x, y), output1[1])))

