from app import config
from fastapi.templating import Jinja2Templates

settings = config.get_settings()
templates = Jinja2Templates(directory=str(settings.templates_dir)) 


def render(request,template_name, context={}, status_code:int=200):
    ctx = context.copy()
    ctx.update({"request": request})
    return templates.TemplateResponse(template_name, ctx, status_code=status_code)