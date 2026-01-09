from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.parser_service import extract_text
from app.services.extractor_service import extract_resume_entities

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]:
        raise HTTPException(status_code=400)

    text = extract_text(file)

    if not text.strip():
        raise HTTPException(status_code=400)

    entities = extract_resume_entities(text)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "entities": entities,
        "preview": text[:500],
    }


