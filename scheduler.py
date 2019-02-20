from PyQt5 import QtWidgets as QTW,\
                  QtGui as QTG, \
                  QtCore as QTC
import os, sys
import pickle as pk
import nosel, part0, part1, part2, success


DOW_TO_INT = {"mon": 0, # Day of the week to integer index
              "tue": 1,
              "wed": 2,
              "thu": 3,
              "fri": 4,
              "sat": 5,
              "sun": 6}

INT_TO_DOW = {0:"Monday", # Day of the week to integer index
              1: "Tuesday",
              2: "Wednesday",
              3: "Thursday",
              4: "Friday",
              5: "Saturday",
              6: "Sunday"}

TOD_TO_INT = {"Mor":0, # TIme of the day to integer index
              "Aft":1,
              "Eve":2}

INT_TO_TOD = {0: "9:00am - 1:00pm",
              1: "1:00pm - 5:00pm",
              2: "5:00pm - 9:00pm"}

# """
# With A, B and C as day of the week
#      L, M and N as time of the day
#
# X can (not) work on A, B and C at L, M, and N
# X prefers (not) to work on A, B and C (at L, M, and N)
# X can (not) work 2 shifts concurrently
# X can only have maximum Y shifts
# """

class NoSel(QTW.QDialog, nosel.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.buttonBox.button(QTW.QDialogButtonBox.Close).clicked.connect(self.close)

class Part0(QTW.QMainWindow, part0.Ui_MainWindow):
    def __init__(self, schedule, nosel):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sched = schedule
        self.nosel = nosel
        self.btnNext.clicked.connect(self.next)
        self.btnExit.clicked.connect(self.close)



    def next(self,i):
        if not self.userName.text() or not self.userSem.text():
            self.nosel.show()
        else:
            self.sched.setName(self.userName.text())
            self.sched.setSem(self.userSem.text())
            self.part1 = Part1(self.sched,self.nosel)
            self.part1.show()
            self.close()


class Part1(QTW.QMainWindow, part1.Ui_MainWindow):
    def __init__(self, schedule, nosel):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sched = schedule
        self.part2 = None
        self.nosel = nosel


        self.monMor.stateChanged.connect(lambda: schedule.checked(self, self.monMor))
        self.monAft.stateChanged.connect(lambda: schedule.checked(self, self.monAft))
        self.monEve.stateChanged.connect(lambda: schedule.checked(self, self.monEve))
        self.tueMor.stateChanged.connect(lambda: schedule.checked(self, self.tueMor))
        self.tueAft.stateChanged.connect(lambda: schedule.checked(self, self.tueAft))
        self.tueEve.stateChanged.connect(lambda: schedule.checked(self, self.tueEve))
        self.wedMor.stateChanged.connect(lambda: schedule.checked(self, self.wedMor))
        self.wedAft.stateChanged.connect(lambda: schedule.checked(self, self.wedAft))
        self.wedEve.stateChanged.connect(lambda: schedule.checked(self, self.wedEve))
        self.thuMor.stateChanged.connect(lambda: schedule.checked(self, self.thuMor))
        self.thuAft.stateChanged.connect(lambda: schedule.checked(self, self.thuAft))
        self.thuEve.stateChanged.connect(lambda: schedule.checked(self, self.thuEve))
        self.friMor.stateChanged.connect(lambda: schedule.checked(self, self.friMor))
        self.friAft.stateChanged.connect(lambda: schedule.checked(self, self.friAft))
        self.friEve.stateChanged.connect(lambda: schedule.checked(self, self.friEve))
        self.satMor.stateChanged.connect(lambda: schedule.checked(self, self.satMor))
        self.satAft.stateChanged.connect(lambda: schedule.checked(self, self.satAft))
        self.sunMor.stateChanged.connect(lambda: schedule.checked(self, self.sunMor))
        self.sunAft.stateChanged.connect(lambda: schedule.checked(self, self.sunAft))
        self.btnNext.clicked.connect(self.next)
    def next(self,i):
        if not self.sched.getCount():
            self.nosel.show()
        else:
            self.part2 = Part2(self.sched,self,self.nosel)
            self.part2.show()
            self.close()

class Part2(QTW.QMainWindow, part2.Ui_MainWindow):
    def __init__(self,sched,part1,nosel):

        super(self.__class__, self).__init__()
        self.part1 = part1
        self.setupUi(self)
        self.sched = sched
        self.nosel = nosel

        for idx in range(len(self.sched.schedule)):
            for i in range(3):
                if self.sched.schedule[idx][i]:
                    self.listShift.addItem(QTW.QListWidgetItem(INT_TO_DOW[idx] + " - " + INT_TO_TOD[i]))
        self.btnNext.clicked.connect(self.next)
        self.btnBack.clicked.connect(self.back)
    def next(self,i):
        if not self.listShift.selectedItems() or len(self.listShift.selectedItems()) > 5:
            self.nosel.show()
        else:
            todFullToInt = {v:k for k,v in INT_TO_TOD.items()}
            for item in self.listShift.selectedItems():
                day = DOW_TO_INT[item.text()[:3].lower()]
                time = todFullToInt[item.text()[-15:]]
                self.sched.schedule[day][time] += 1
            self.part3 = Success(self.sched)
            self.part3.show()
            self.close()
    def back(self):
        self.part1.show()
        self.close()

class Success(QTW.QDialog, success.Ui_Dialog):
    def __init__(self,sched):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sched = sched
        self.buttonBox.button(QTW.QDialogButtonBox.Close)
        self.filename = self.sched.getName().lower().replace(" ","")+self.sched.getSem().lower().replace(" ", "") + ".sched"
        self.fileName.setText(self.filename) # label object

        with open(self.filename, "wb+") as f:
            pk.dump(self.sched,f)

class Schedule():
    def __init__(self):
        self.name = None
        self.sem = None
        self.countShift = 0
        self.schedule = [[0,0,0] for _ in range(7)] # from 9:00am to 9:00pm, 1hr increment
    def __getitem__(self, item):
        try:
            return self.schedule[item]
        except KeyError:
            raise StopIteration
    def __len__(self):
        return len(self.schedule)
    def checked(self, i, button):
        day = DOW_TO_INT[button.objectName()[:3]]
        time = TOD_TO_INT[button.objectName()[3:]]
        if button.isChecked():
            # print("Checked", button.objectName())
            self.countShift += 1
            self.schedule[day][time] = 1
        else:
            # print("Unchecked", button.objectName())
            self.countShift -= 1
            self.schedule[day][time] = 0
        # print(self.schedule)
    def getCount(self):
        return self.countShift

    def getName(self):
        return self.name

    def getSem(self):
        return self.sem

    def setName(self,name):
        self.name = name

    def setSem(self,sem):
        self.sem = sem



if __name__ == "__main__":
    app = QTW.QApplication(sys.argv)  # A new instance of QApplication
    sched = Schedule()
    nosel = NoSel()
    part0 = Part0(sched,nosel)  # We set the form to be our ExampleApp (design)
    part0.show()  # Show the form

    app.exec_()



