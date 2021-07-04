from fastapi import FastAPI, Depends
from starlette.requests import Request
from api.config import PROJECT_NAME
from api.routers.company_manager import companies_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn




app = FastAPI(
    title=PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(
    companies_router,
    prefix="/company",
    tags=["company"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)