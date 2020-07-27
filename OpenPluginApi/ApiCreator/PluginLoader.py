import os
def help():
    message = """
Loads Plugins
"""
    print(message)
    return message

def load(FileName: str, globals, locals):
    with open(FileName) as f:
        exec(f.read(),globals, locals)

def loadFolder(FolderName: str, globals, locals, recursive = False, parent = ""):
    files = os.listdir(parent+FolderName)
    print(parent)
    for file in files:
        print(file)
        if ".py" in file:
            with open(parent+FolderName+'/'+file) as f:
                exec(f.read(),globals, locals)
        elif recursive == True:
            loadFolder(file, globals, locals, recursive = False, parent = parent+FolderName+'/')
