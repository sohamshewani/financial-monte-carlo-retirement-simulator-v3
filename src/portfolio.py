from dataclasses import dataclass
from typing import List
import pandas as pd
from src.utils import read_csv
from src.utils import round_to_two_decimal_places

@dataclass
class Asset:
    name: str
    value: float

@dataclass
class Portfolio:
    assets: List[Asset]
    total_value: float = 0.0

    def __post_init__(self):
        self.total_value = sum(asset.value for asset in self.assets)

    def add_asset(self, name: str, value: float) -> None:
        self.assets.append(Asset(name, value))
        self.total_value += value

    def remove_asset(self, name: str) -> None:
        asset = next((a for a in self.assets if a.name == name), None)
        if asset:
            self.assets.remove(asset)
            self.total_value -= asset.value

    def total_value(self) -> float:
        return self.total_value

    def __str__(self):
        return pd.DataFrame(self.assets, columns=['Name', 'Value']).to_string(index=False)

    def __repr__(self):
        return self.__str__()

    @staticmethod
def from_csv(filepath: str) -> Portfolio:
    assets = [Asset(name=row['name'], value=row['value']) for row in read_csv(filepath)]
    return Portfolio(assets)

    @staticmethod
def from_string(input: str) -> Portfolio:
    lines = input.strip().split('
')
    assets = [Asset(name=line.split()[0], value=float(line.split()[1])) for line in lines]
    return Portfolio(assets)

    @staticmethod
def read_csv(filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

    @staticmethod
def round_to_two_decimal_places(value: float) -> float:
        return round_to_two_decimal_places(value)

    @staticmethod
def write_csv(data: pd.DataFrame, filepath: str) -> None:
        data.to_csv(filepath, index=False)

    @staticmethod
def read_csv(filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

    @staticmethod
def round_to_two_decimal_places(value: float) -> float:
        return round_to_two_decimal_places(value)