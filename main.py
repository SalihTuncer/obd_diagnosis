import obd
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application.api.api_v1.api import api_v1_router

app = FastAPI(
    title='OBD2 API',
    description='API to make analysis on OBD2 data',
    version='0.1.0',
    openapi_url='/api/v1/openapi.json',
    docs_url='/api/v1/docs'
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)

if __name__ == '__main__':
    obd.logger.info('Starting the API.')
    uvicorn.run("main:app")
