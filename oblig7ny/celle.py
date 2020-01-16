class Celle:

    def __init__(self):
        self._levende = False

    # Endre status
    def settDoed(self):
        self._levende = False

    def settLevende(self):
        self._levende = True
    # Hente status
    def erLevende(self):
        return self._levende


    def hentStatusTegn(self):
        if self._levende:
            return "O"
        return "."
