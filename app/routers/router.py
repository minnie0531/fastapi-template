from fastapi import APIRouter

"""
This Module is for query endpoints.

Client can access this application through GET/POST/PUT/DELETE /queries

"""

router = APIRouter()


@router.get("/routers", tags=["router"], description="Test endpoint")
def test_endpoint():
    return {"Test endpoint"}
