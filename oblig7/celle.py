"""Har valgt å bruke True og False som levende og doed."""

class Celle:
    def __init__(self):
        self.settDoed()

    def settDoed(self):
        self._status = False

    def settLevende(self):
        self._status = True

    def erLevende(self):
        if self._status == True:
            return True
        elif self._status == False:
            return False

    def hentStatusTegn(self):
        if self._status == True:
            return "O"
        elif self._status == False:
            return "."
