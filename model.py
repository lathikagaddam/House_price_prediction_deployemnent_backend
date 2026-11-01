from pydantic import BaseModel


class HouseDetails(BaseModel):
    area_sqft:float
    bedrooms: int
    bathrooms: int
    property_age_years: int
    location: str
    property_type: str
    parking: str
