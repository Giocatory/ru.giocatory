from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import pages, api

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем роуты
app.include_router(pages.router)
#app.include_router(api.users.router, prefix="/api/users")