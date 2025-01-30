from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")




@router.get("/success")
async def success_page(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": "Сообщение успешно отправлено!"
    })


@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/python")
async def python_page(request: Request):
    return templates.TemplateResponse("python.html", {"request": request})

@router.get("/datascience")
async def datascience_page(request: Request):
    return templates.TemplateResponse("datascience.html", {"request": request})

@router.get("/machinelearning")
async def machinelearning_page(request: Request):
    return templates.TemplateResponse("machinelearning.html", {"request": request})