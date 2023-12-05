from fastapi import FastAPI
from fastapi.responses import UJSONResponse

app = FastAPI(default_response_class=UJSONResponse)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(v1_router)
