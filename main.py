from fastapi import FastAPI
import models
from database import engine
from routes import router

# Create the database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Todo App API")

app.include_router(router, prefix="/api", tags=["todos"])
