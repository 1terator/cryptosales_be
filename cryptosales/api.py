from fastapi import FastAPI

from cryptosales.user.router import router as auth_router

app = FastAPI()

# include routers
app.include_router(auth_router)
