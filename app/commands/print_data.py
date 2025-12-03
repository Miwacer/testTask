from app.repository import CountryRepository


class PrintDataCommand:
    def __init__(self):
        self.repo = CountryRepository()

    def run(self):

        rows = self.repo.get_region_stats()
        print("DEBUG rows:", rows)

        for (
            region,
            total_population,
            max_country,
            max_population,
            min_country,
            min_population,
        ) in rows:
            print(region)
            print(int(total_population))
            print(max_country)
            print(int(max_population))
            print(min_country)
            print(int(min_population))
            print("-" * 40)


if __name__ == "__main__":
    command = PrintDataCommand()
    command.run()
