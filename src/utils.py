def read_csv(filepath: str) -> pd.DataFrame:
    import pandas as pd
    return pd.read_csv(filepath)

    def write_csv(data: pd.DataFrame, filepath: str) -> None:
        data.to_csv(filepath, index=False)

    def round_to_two_decimal_places(value: float) -> float:
        return round(value, 2)