from fastapi import APIRouter, UploadFile, File
from ..services.file_service import _File

file_router = APIRouter()

@file_router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    result = await _File.save(file)
    return result

@file_router.get('/download')
async def download():
    pass