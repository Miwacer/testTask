from app.repository import CountryRepository


class PrintDataCommand:
    def __init__(self):
        self.repo = CountryRepository()

    def run(self):
        rows = self.repo.get_population_by_region()

        for region, total_population in rows:
            print(f"{region}: {int(total_population):,}")
