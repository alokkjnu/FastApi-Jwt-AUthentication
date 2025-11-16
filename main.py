from fastapi import FastAPI, Depends, HTTPException, status
from routers import api_routers
import uvicorn

app = FastAPI()

app.include_router(api_routers.router)

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8005)
