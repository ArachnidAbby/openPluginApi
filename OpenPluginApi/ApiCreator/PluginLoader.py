def load(FileName: str, globals, locals):
    with open(FileName) as f:
        exec(f.read(),globals, locals)