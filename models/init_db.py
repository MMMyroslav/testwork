from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from const import SQL_ALCHEMY_DB_URL


engine = create_engine(SQL_ALCHEMY_DB_URL,
                       echo=False,
                       pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()
    :return: create db
    """
    import models.model

    Base.metadata.create_all(bind=engine)
