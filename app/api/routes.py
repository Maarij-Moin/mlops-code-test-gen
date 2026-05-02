from fastapi import APIRouter
from app.services.test_service import run_test_pipeline

router = APIRouter()

@router.post("/generate-tests")
def generate_tests(repo_url: str, commit_id: str):
    result = run_test_pipeline(repo_url, commit_id)
    return {"status": "success", "data": result}