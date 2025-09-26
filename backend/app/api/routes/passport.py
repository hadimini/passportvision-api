from fastapi import UploadFile, File, HTTPException, status
from fastapi.routing import APIRouter

from app.schemas.passport import PassportPublicSchema
from app.services.passport import PassportRecognizer

router = APIRouter(prefix="/passport", tags=["passport"])


@router.post(
    path="/recognize",
    name="passport:recognize"
)
async def passport_recognize(
    file: UploadFile = File(..., description="Passport image file"),
):
    """
    Extract passport data from Machine Reading Zone (MRZ)

    Available from MRZ:
    - Passport number, expiration date, date of birth
    - Name, nationality, sex, document type

    Not available from MRZ:
    - Issue date, place of birth, issuing authority
    """
    recognizer = PassportRecognizer()

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be an image file",
        )

    content = file.read()

    try:
        # Extract MRZ data
        mrz_txt = await recognizer.extract_mrz(content)
        parsed_data = recognizer.parse_mrz(mrz_txt)

        return PassportPublicSchema(**parsed_data)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Processing failed: {str(e)}",
        )
