import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def home():
    return {
        "msg": "Hello world",
    }


uvicorn.run(api)
