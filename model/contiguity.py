from dataclasses import dataclass


@dataclass
class Contiguity:
    dyad: int
    state1no: int
    state1ab:str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float


    def __eq__(self, other):
        return self.state1no == other.state1no and self.state2no == other.state2no

    def __hash__(self):
        return hash((self.state1no, self.state1ab, self.state2no, self.state2ab))