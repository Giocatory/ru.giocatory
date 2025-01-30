from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse  # <-- Добавьте импорт
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models.messages import UsersMessages

router = APIRouter()

@router.post("/feedback")
async def create_feedback(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    form_data = await request.form()
    
    message = UsersMessages(
        user_name=form_data.get("user_name"),
        user_email=form_data.get("user_email"),
        user_text=form_data.get("user_text")
    )
    
    db.add(message)
    await db.commit()
    
    return RedirectResponse(url="/?success=1", status_code=303)