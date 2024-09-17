from db.database import sync_engine
from sqlalchemy import text

with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(res.one())