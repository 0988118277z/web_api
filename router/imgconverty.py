from fastapi import APIRouter, File, UploadFile, HTTPException
from enum import Enum
from fastapi.responses import FileResponse
from PIL import Image
import os
from io import BytesIO
from datetime import datetime

router = APIRouter(
    prefix="/api/v1/img-convert",
    tags=["Image convert"],
)

class ImageItem(str, Enum):
    # cpc = "CPC"
    gif = "GIF"
    # ilbm = "ILBM"
    jpeg = "JPEG"
    # pict = "PICT"
    png = "PNG"
    # psd = "PSD"
    # psp = "PSP"
    # svg = "SVG"
    tga = "TGA"
    tiff = "TIFF"
    bmp = "BMP"
    webp = "WebP"

@router.post("/jpeg/to/{img_format}")
async def jpg_image_convert(img_format:ImageItem, file: UploadFile = File(...)):
    if file.content_type != 'image/jpeg':
        raise HTTPException(status_code=400, detail="File must be a JPG image")
        
    image = Image.open(BytesIO(await file.read()))
    cnv_image = image.convert("RGB")
    
    img_format = str(img_format).split('.')[1]
    current_time = datetime.now()  #取得當前時間
    formatted_time = current_time.strftime("%Y%m%d-%H%M%S.%f")  #格式化時間
    file_path = f"images/{formatted_time}.{img_format}"

    cnv_image.save(file_path, img_format)
    return FileResponse(file_path, media_type=f"image/{img_format}", filename=f"converted_image.{img_format}")

@router.post("/png/to/{img_format}")   
async def png_image_convert(img_format:ImageItem, file: UploadFile = File(...)):
    if file.content_type != 'image/png':
        raise HTTPException(status_code=400, detail="File must be a PNG image")
        
    image = Image.open(BytesIO(await file.read()))
    cnv_image = image.convert("RGB")
    
    img_format = str(img_format).split('.')[1]
    current_time = datetime.now()  #取得當前時間
    formatted_time = current_time.strftime("%Y%m%d-%H%M%S.%f")  #格式化時間
    file_path = f"images/{formatted_time}.{img_format}"
    
    cnv_image.save(file_path, img_format)
    return FileResponse(file_path, media_type=f"image/{img_format}", filename=f"converted_image.{img_format}")
    





