import os
from fastapi import FastAPI
from port.fastapi.router import post as post_router
from port.fastapi.router import user as user_router
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv

load_dotenv()

def configure_routers(application: FastAPI):
    application.include_router(post_router.router)
    application.include_router(user_router.router)

def configure_tortoise(application: FastAPI):
    __HOST = os.getenv('DB_HOST')
    __USER = os.getenv('DB_USER')
    __PASS = os.getenv('DB_PASS')
    __DATABASE = os.getenv('DB_NAME')
    __PORT = os.getenv('DB_PORT')
    register_tortoise(
        application,
        generate_schemas=True,
        db_url=f"postgres://{__USER}:{__PASS}@{__HOST}:{__PORT}/{__DATABASE}",
        modules={
            "models": [
                "adapter.models.post",
                "adapter.models.user",
            ],
        }
    )