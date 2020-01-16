class Bud:
    def __init__(self, budgiver, budStr):
        self._budgiver = budgiver
        self._budStr = int(budStr)


    def hentBudgiver(self):
        return self._budgiver


    def hentBudStr(self):
        if self._budStr <= 0:
            self._budStr = 1
        return self._budStr
