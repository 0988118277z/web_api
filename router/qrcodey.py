import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask, HorizontalGradiantColorMask, ImageColorMask
from fastapi import APIRouter, status, Response, FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter(
    prefix="/api/v1/qrcode",
    tags=["Qrcode Generate"],
)

class QRCodeItem(BaseModel):
    version: int = Field(3, ge=1, le=40)
    # error_correction: str = 'L'  #LMHQ
    box_size: int = 10
    border: int = 4
    text: str = Field('web api', example="your text")
    

@router.post("/")
async def qrcode_generate(item:QRCodeItem):
    qr = qrcode.QRCode(
        version = item.version,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = item.box_size,
        border = item.border
    )
    qr.add_data(item.text)
    qr.make(fit=True)
    img = qr.make_image()
    
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d-%H%M%S.%f")
    file_path = f"images/qrcode_{formatted_time}.jpg"

    img.save(file_path)
    return FileResponse(file_path, media_type=f"image/jpg", filename=f"qrcode.jpg")