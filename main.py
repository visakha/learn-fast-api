import fastapi
import uvicorn
from views import home

api = fastapi.FastAPI()


def config_routers():
    api.include_router(home.router)


config_routers()

if __name__ == '__main__':
    uvicorn.run(api)
