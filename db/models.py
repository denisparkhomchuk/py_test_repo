import datetime
import enum
from importlib.metadata import metadata
from typing import Annotated, Optional

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str_256] = mapped_column()


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256] = mapped_column()
    compensation: Mapped[int] = mapped_column(nullable=True)
    workload: Mapped[Workload] = mapped_column()
    worker_id: Mapped[int] = mapped_column(ForeignKey(WorkersOrm.id, ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow(),
                                                          onupdate=datetime.datetime.utcnow())

metadata_obj = MetaData()

workers_table = Table("workers",
                      metadata_obj,
                      Column("id", Integer, primary_key=True),
                      Column("username", String(16)))