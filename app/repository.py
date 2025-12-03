from sqlalchemy import func, select
from app.models import Country
from app.database import SessionLocal


class CountryRepository:
    def __init__(self):
        self.session = SessionLocal()

    def save_many(self, countries: list[dict]):
        for item in countries:
            self.session.add(Country(**item))
        self.session.commit()

    def get_region_stats(self):
        total_sub = (
            self.session.query(
                Country.region.label("region"),
                func.sum(Country.population).label("total_population"),
            )
            .group_by(Country.region)
            .subquery()
        )

        max_sub = (
            self.session.query(
                Country.region.label("region"),
                func.max(Country.population).label("max_population"),
            )
            .group_by(Country.region)
            .subquery()
        )

        min_sub = (
            self.session.query(
                Country.region.label("region"),
                func.min(Country.population).label("min_population"),
            )
            .group_by(Country.region)
            .subquery()
        )

        return (
            self.session.query(
                Country.region,
                total_sub.c.total_population,
                Country.location.label("max_country"),
                max_sub.c.max_population,
                Country.location.label("min_country"),
                min_sub.c.min_population,
            )
            .join(total_sub, Country.region == total_sub.c.region)
            .join(max_sub, Country.region == max_sub.c.region)
            .join(min_sub, Country.region == min_sub.c.region)
            .filter(
                (Country.population == max_sub.c.max_population)
                | (Country.population == min_sub.c.min_population)
            )
            .group_by(
                Country.region,
                total_sub.c.total_population,
                max_sub.c.max_population,
                min_sub.c.min_population,
                Country.location,
            )
            .all()
        )
