from dataclasses import dataclass
from datetime import date

@dataclass
class TurmaDTO():

    nome: str
    desc: str
    data_inic: date
    data_fim: date