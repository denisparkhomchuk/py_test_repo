from db.database import sync_engine
from db.models import metadata_obj

def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


