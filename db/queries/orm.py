from db.database import sync_engine, session_factory
from db.models import metadata_obj, Base, WorkersOrm, ResumesOrm
from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text

def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def insert_workers():
    worker_bobr = WorkersOrm(username="Bobr")
    worker_volk = WorkersOrm(username="Volk")
    with session_factory() as session:
        session.add_all([worker_bobr, worker_volk])
        session.commit()

def select_workers():
    with session_factory() as session:
        query = select(WorkersOrm)
        result = session.execute(query)
        workers = result.scalars().all()
        return workers


def update_worker(worker_id, username_new):
    with session_factory() as session:
        worker_to_update = session.get(WorkersOrm, worker_id)
        worker_to_update.username = username_new
        #session.refresh(worker_to_update)
        session.commit()