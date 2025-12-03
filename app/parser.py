import requests
import pandas as pd


class PopulationParser:
    URL = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_%28United_Nations%29&oldid=1215058959"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }

    def fetch(self) -> pd.DataFrame:
        response = requests.get(self.URL, headers=self.HEADERS)
        response.raise_for_status()

        tables = pd.read_html(response.text)
        df = tables[0]
        return df

    def normalize(self, df: pd.DataFrame) -> list[dict]:
        data = []

        for _, row in df.iloc[1:].iterrows():
            raw_population = row["Population (1 July 2023)"]

            if pd.isna(raw_population):
                continue

            population = int(float(raw_population))

            data.append(
                {
                    "location": row["Location"],
                    "population": population,
                    "region": row["UN Continental Region[1]"],
                    "subregion": row["UN Statistical Subregion[1]"],
                }
            )
        print(f"Collected items: {len(data)}")
        return data
