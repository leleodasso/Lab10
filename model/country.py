from dataclasses import dataclass


@dataclass
class County:
    StateAbb: str
    CCode: int
    StateNme: str

    def __eq__(self, other):
        return self.CCode == other.CCode

    def __hash__(self):
        return hash(self.CCode)

