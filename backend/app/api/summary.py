from fastapi import APIRouter

from app.services.summary_service import SummaryService

router = APIRouter()


@router.post("/summary")
def summarize(workspace_id: str):

    return SummaryService.summarize(
        workspace_id=workspace_id,
    )