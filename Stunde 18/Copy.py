class CopyFile:
    sourceName: ""
    sourcePath: ""
    targetName: ""
    targetPath: ""

    def __init__(self, sourceName, sourcePath, targetName, targetPath):
        self.sourceName = sourceName
        self.sourcePath = sourcePath
        self.targetName = targetName
        self.targetPath = targetPath

    def set_sourceName(self, sourceName):
        self.sourceName = sourceName

    def set_sourcePath(self, sourcePath):
        self.sourcePath = sourcePath

    def set_targetName(self, targetName):
        self.targetName = targetName

    def set_targetPath(self, targetPath):
        self.targetPath = targetPath

    def get_sourceName(self):
        return self.sourceName

    def get_sourcePath(self):
        return self.sourcePath

    def get_targetName(self):
        return self.targetName

    def get_targetPath(self):
        return self.targetPath

    def doCopy(self):

        sourceFilePath = self.sourcePath + self.sourceName
        targetFilePath = self.targetPath + self.targetName

        if sourceFilePath == targetFilePath:
            return "Source und Target sind identisch! Ich kopiere mal lieber nicht."

        with open(sourceFilePath, 'r') as reader, open(targetFilePath, "w") as writer:

            inhalt = reader.readlines()
            writer.writelines(reversed(inhalt))

        return "File: " + self.sourceName + " from directory: " + self.sourcePath + " copied to file: " + self.targetName + " in directory: " + self.targetPath

