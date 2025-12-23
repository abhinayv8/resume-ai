from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.parser_service import extract_text
from app.services.preprocessing_service import preprocess_text
from app.services.extractor_service import extract_resume_entities

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    raw_text = extract_text(file)
    clean_text = preprocess_text(raw_text)

    entities = extract_resume_entities(clean_text)

    return {
        "filename": file.filename,
        "entities": entities,
        "preview": clean_text[:500]
    }

