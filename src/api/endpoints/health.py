from fastapi import APIRouter
from typing import Dict

router = APIRouter()

@router.get("/health", response_model=Dict)
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }
