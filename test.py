from db.database import sync_engine
from sqlalchemy import text
#from db.queries.core import create_tables
from db.queries.orm import create_tables, insert_workers, select_workers, update_worker, insert_resumes, select_resumes_avg_compensation

with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(res.one())


create_tables()
insert_workers()
workers = select_workers()
print(workers)
#update_worker(1, "Tiger")
#workers = select_workers()
#print(workers)
insert_resumes()
res = select_resumes_avg_compensation()
print(res)



