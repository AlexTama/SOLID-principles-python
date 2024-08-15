from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename) -> None:
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    def write(self, data, encoding="utf-8"):
        return self.path.write_text(data, encoding)
    
class ZipFileManager:
    def __init__(self, filename) -> None:
        self.path = Path(filename)
    
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)
    
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip")) as archive:
            archive.extractall(self.path)