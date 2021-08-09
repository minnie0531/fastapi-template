from fastapi import FastAPI

from .routers import query

# Tags for representative endpoints
tags = [
    {
        "name": "queries",
        "description": "Operations with queries",
    }
]

# Define Fast api and description
app = FastAPI(
    title="Garage MVP FastAPI MAS template",
    description="This is a template of python MSA used in Garage project.",
    version="0.0.1",
    openapi_tags=tags,
)

# Add routers to main
app.include_router(query.router)

# This path is for health check or test
@app.get("/")
async def root():
    return {"Hello World :D"}
