#  py -m pip install fastapi uvicorn
#  py -m uvicorn main:app --reload --port 8080
from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Optional
from router import accounty, helloy, imgconverty

app = FastAPI()
app.include_router(accounty.router)
app.include_router(helloy.router)
app.include_router(imgconverty.router)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs", status_code=301)


    

