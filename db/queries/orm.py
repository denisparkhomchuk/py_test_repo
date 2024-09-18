from db.database import sync_engine, session_factory
from db.models import metadata_obj, Base, WorkersOrm, ResumesOrm, Workload
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


def insert_resumes():
    with session_factory() as session:
        resume_jack_1 = ResumesOrm(
            title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
        resume_jack_2 = ResumesOrm(
            title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
        resume_michael_1 = ResumesOrm(
            title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
        resume_michael_2 = ResumesOrm(
            title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
        session.add_all([resume_jack_1, resume_jack_2,
                         resume_michael_1, resume_michael_2])
        session.commit()

def select_resumes_avg_compensation(like_language: str = "Python"):
    """
    select workload, avg(compensation)::int as avg_compensation
    from resumes
    where title like '%Python%' and compensation > 40000
    group by workload
    having avg(compensation) > 70000
    """
    with session_factory() as session:
        query = (
            select(
                ResumesOrm.workload,
                # 1 вариант использования cast
                # cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation"),
                # 2 вариант использования cast (предпочтительный способ)
                func.avg(ResumesOrm.compensation).cast(Integer).label("avg_compensation"),
            )
            .select_from(ResumesOrm)
            .filter(and_(
                ResumesOrm.title.contains(like_language),
                ResumesOrm.compensation > 40000,
            ))
            .group_by(ResumesOrm.workload)
            .having(func.avg(ResumesOrm.compensation) > 70000)
        )
        print(query.compile(compile_kwargs={"literal_binds": True}))
        res = session.execute(query)
        result = res.all()
        return result