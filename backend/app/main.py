from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router as api_router
from api.journal import router as journal_router
from api.user import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(journal_router, prefix='/api/v1')
app.include_router(user_router, prefix='/api/v1')

@app.get("/")
def read_root():
    return {"message": "Welcome to the PastAI API"}