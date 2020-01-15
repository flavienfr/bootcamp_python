class OpenFile():
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        # ici on retourne l'objet fichier, il sera accessible avec "as"
        return self.file
    def __exit__(self, type, value, traceback):
        self.file.close()

with OpenFile('good.csv') as f:
    for line in f:
        print(line, end = '')