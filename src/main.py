from contextlib import asynccontextmanager
import uuid
import models
from fastapi import FastAPI, Depends, Request, Response
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

@app.middleware("http")
async def request_id_logging(request: Request, call_next):
    response = await call_next(request)
    request_id = uuid.uuid4()
    print(request_id)
    response.headers['Request-Id'] = str(request_id)
    return response

@app.get('/health')
async def health_check():
    return 'App running...'

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
    