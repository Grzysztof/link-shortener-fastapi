from typing import Annotated
from uuid import UUID
from fastapi import FastAPI, status, Depends
from fastapi.responses import UJSONResponse, RedirectResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from link_shortener_fastapi import models
from link_shortener_fastapi.dependencies import get_repository
from link_shortener_fastapi.database.session import get_db_session
from link_shortener_fastapi.database.repository import DatabaseRepository
from link_shortener_fastapi.database import schemas

app = FastAPI(default_response_class=UJSONResponse)

LinksRepository = Annotated[
    DatabaseRepository[schemas.Links],
    Depends(get_repository(schemas.Links)),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/link/{id}")
async def link_redirect(
    links_repository: LinksRepository,
    id: UUID = None,
):
    link = await links_repository.get(id)
    if link:
        return RedirectResponse(link.redirect_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
    else:
        return Response({"error": "Link not found"}, status_code=status.HTTP_404_NOT_FOUND)


@app.post("/link")
async def create_link(
    data: models.LinkPayload,
    links_repository: LinksRepository,
):
    link = await links_repository.create(data.model_dump())
    return models.Link.model_validate(link)
