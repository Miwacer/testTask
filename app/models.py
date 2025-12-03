from sqlalchemy import Column, Integer, String, BigInteger
from app.database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)

    location = Column(String, nullable=False, index=True)

    population = Column(BigInteger, nullable=False)

    region = Column(String, index=True)

    subregion = Column(String, index=True)

    def __repr__(self):
        return f"<Country {self.location} ({self.population})>"
