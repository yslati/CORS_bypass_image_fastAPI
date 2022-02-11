from fastapi import FastAPI
from settings import headers
import requests
import io
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getimg/")
def read_item(src: str):
	r = requests.get(src, headers=headers)
	return StreamingResponse(io.BytesIO(r.content), media_type="image/png")
