import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

home_templates = Jinja2Templates("templates")

router = fastapi.APIRouter()


@router.get("/home")
def home(request: Request):
    return home_templates.TemplateResponse("home.html", {
        "request": request,
        "welcome": "welcome to learning FastAPI",
    })
