class Celle:
    # Constructor
    def __init__(self):
        self.settDoed()

    # Endre status
    def settDoed(self):
        self._status = False

    def settLevende(self):
        self._status = True

    # Hente status
    def erLevende(self):
        if self._status:
            return True
        else:
            return False


    def hentStatusTegn(self):
        if self.erLevende:
            return "O"
        else:
            return "."
