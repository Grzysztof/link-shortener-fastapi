from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI, status, Depends
from fastapi.responses import UJSONResponse, RedirectResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession
from link_shortener_fastapi import models
from link_shortener_fastapi.database.session import get_db_session, create_db
from link_shortener_fastapi.database import schemas

app = FastAPI(default_response_class=UJSONResponse)

@app.get("/")
async def root():
    return {"message": "Hello World"}

#FIXME:
@app.get("/link/")
async def empty_link():
    return Response({'error': 'No redirect'}, status_code=status.HTTP_404_NOT_FOUND)

@app.get("/link/{link_id}")
async def link_redirect(link_id: str = None):
    if link_id:
        return RedirectResponse('/', status_code=status.HTTP_301_MOVED_PERMANENTLY)
    else:
        return Response({'error': 'No redirect'}, status_code=status.HTTP_404_NOT_FOUND)
    
@app.post("/link")
async def create_link(
    data: models.LinkPayload,
    db_session: AsyncSession = Depends(get_db_session),
):
    new_link = schemas.Links(**data.model_dump())
    db_session.add(new_link)
    await db_session.commit()
    await db_session.refresh(new_link)
    return models.Link.model_validate(new_link)
