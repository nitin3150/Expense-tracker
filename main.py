from fastapi import FastAPI,Request,Form
from routes import user
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Expense Tracker")
templates = Jinja2Templates(directory="templates")

# Show the form
@app.get("/", response_class=HTMLResponse)
def get_user_form(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})

app.include_router(user.router, prefix="/users", tags=["Users"])