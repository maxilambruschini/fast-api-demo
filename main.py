from fastapi import FastAPI

from services import cases, users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(cases.router, prefix="/cases", tags=["cases"])
