from pydantic import BaseModel, ConfigDict

class ConversionResponse(BaseModel):
    from_unit: str
    to_unit: str
    value: float
    result: float
    model_config = ConfigDict(from_attributes=True)