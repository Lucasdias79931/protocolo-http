import aiofiles, logging, os
from uuid import uuid4
from fastapi import UploadFile
from backend.settings import settings
from ..dto import File_dto


class _File:

    @staticmethod
    async def save(file: UploadFile) -> File_dto:
        try:
            os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

            file_id = str(uuid4())
            filename = f"{file_id}_{file.filename}"
            filepath = os.path.join(settings.UPLOAD_DIR, filename)

            async with aiofiles.open(filepath, "wb") as f:
                content = await file.read()
                await f.write(content)

            logging.info(f"Arquivo salvo em: {filepath}")

            return File_dto(
                filename=filename,
                id=file_id,
                url=filepath  
            )

        except Exception as e:
            logging.error(f"Erro ao salvar arquivo: {e}")
            raise