from fastapi import APIRouter, status, HTTPException
from app.schemas.conversion import ConversionResponse

router = APIRouter()


@router.get("/api/conversion/km-to-miles/{value}", response_model=ConversionResponse)
def convert_km_to_miles(value: float):
    if value < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Distance cannot be negative",
        )

    result = value * 0.621371
    return ConversionResponse(
        from_unit="km", to_unit="miles", value=value, result=result
    )


@router.get("/api/conversion/miles-to-km/{value}", response_model=ConversionResponse)
def convert_km_to_miles(value: float):
    if value < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Distance cannot be negative",
        )

    result = value / 0.621371
    return ConversionResponse(
        from_unit="miles", to_unit="km", value=value, result=result
    )


@router.get(
    "/api/conversion/celsius-to-fahrenheit/{value}", response_model=ConversionResponse
)
def convert_celsius_to_fahrenheit(value: float):
    result = (value * 9 / 5) + 32
    return ConversionResponse(
        from_unit="Celsius", to_unit="Fahrenheit", value=value, result=result
    )


@router.get(
    "/api/conversion/fahrenheit-to-celsius/{value}", response_model=ConversionResponse
)
def convert_fahrenheit_to_celsius(value: float):
    result = (value - 32) * 5 / 9
    return ConversionResponse(
        from_unit="Fahrenheit", to_unit="Celsius", value=value, result=result
    )
