from Copy import CopyFile

fileCopy = CopyFile("", "", "", "")

fileCopy.set_sourceName(input("Gebe SourceFile Name ein"))
fileCopy.set_sourcePath("C:/Users/Paul Kostial/PycharmProjects/Aufgabe18/")
fileCopy.set_targetName("Test_copy")
fileCopy.set_targetPath("C:/Users/Paul Kostial/PycharmProjects/Aufgabe18/")

print(fileCopy.doCopy())