from fastapi import FastAPI
from .routers import router
import yaml
import logging.config

# Set logging configuration
with open("./app/config/logging_config.yaml", "r") as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
#logging.config.dictConfig(config)

# Set logger name to project
logger = logging.getLogger("garage")
logger.info("START Application")

# Tags for representative endpoints
tags = [
    {
        "name": "routers",
        "description": "Operations with xxx",
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
app.include_router(router.router)

# This path is for health check or test
@app.get("/")
async def root():
    return {"Hello World :D"}
