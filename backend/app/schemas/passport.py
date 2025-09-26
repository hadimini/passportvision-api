from datetime import datetime
from typing import Optional

from app.schemas.base import BaseSchema


class PassportBaseSchema(BaseSchema):
    # MRZ Data (Available)
    document_type: str
    issuing_country: str
    surname: str
    given_names: str
    passport_number: str
    nationality: str
    date_of_birth: datetime
    sex: str
    expiration_date: datetime
    personal_number: Optional[str] = None

    # Visual Zone Data (Not available from MRZ)
    issue_date: Optional[datetime] = None
    place_of_birth: Optional[str] = None
    issuing_authority: Optional[str] = None


class PassportPublicSchema(PassportBaseSchema):
    mrz_raw_text: str
    is_valid: bool
    has_visual_zone_data: bool
    data_source: str = "MRZ"
    limitations: list[str] = []
