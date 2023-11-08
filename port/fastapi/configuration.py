import os
from fastapi import FastAPI
from port.fastapi.router import post as post_router
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv

load_dotenv()

def configure_routers(application: FastAPI):
    application.include_router(post_router.router)

def configure_tortoise(application: FastAPI):
    register_tortoise(
        application,
        generate_schemas=True,
        db_url=os.environ.get("DATABASE_URL"),
        modules={
            "models": [
                "adapter.schemas.post"
            ],
        }
    )