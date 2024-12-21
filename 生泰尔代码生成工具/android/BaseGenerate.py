class BaseGenerate:
    fileName = ''
    contentStr = ''

    def getResult(self):
        # return {'filename': self.fileName, 'content': strTemp}
        return [self.fileName, self.contentStr]
