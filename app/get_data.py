from app.parser import PopulationParser
from app.repository import CountryRepository


class GetDataCommand:
    def __init__(self):
        self.parser = PopulationParser()
        self.repo = CountryRepository()

    def run(self):
        df = self.parser.fetch()
        data = self.parser.normalize(df)
        self.repo.save_many(data)
