from fastapi import FastAPI

from .routers import copywriting, scripts, editing, publish, feedback

app = FastAPI(title="Restaurant AI Generator")

app.include_router(copywriting.router, prefix="/copywriting", tags=["copywriting"])
app.include_router(scripts.router, prefix="/scripts", tags=["scripts"])
app.include_router(editing.router, prefix="/editing", tags=["editing"])
app.include_router(publish.router, prefix="/publish", tags=["publish"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant AI Generator API"}
