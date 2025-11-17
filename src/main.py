from contextlib import asynccontextmanager
import models
from fastapi import FastAPI, Depends
from database import engine, SessionLocal

@asynccontextmanager
async def lifespan(app):
    print('starting up...')
    yield
    print('shutting down')

app = FastAPI(lifespan=lifespan)

# Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Endpoint de exemplo# @app.post("/account")
# def create_account(name: str, email: str, db: Session = Depends(get_db)):
#     account = Account(name=name, email=email)
#     db.add(account)
#     db.commit()
#     db.refresh(account)
#     return account

# @app.get("/accounts")
# def get_accounts(db: Session = Depends(get_db)):
#     return db.query(Account).all()
    