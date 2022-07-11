import datetime, time, os
#Very simple script just run TimeCheck with your file path.
class TimeCheck:
    def __init__(self, filePath):
        self.filePath = filePath

    def measureTime(self):
        startTime = time.time()
        exec(open(self.filePath).read())
        stopTime = time.time()
        finalTime = str(datetime.timedelta(seconds=stopTime-startTime))

        return finalTime