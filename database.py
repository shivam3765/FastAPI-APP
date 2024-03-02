from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# For sqlite
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


# For postgresSQL
# POSTGRESQL_DATABASE_URL = 'postgresql://postgres:Ss9079581918@localhost/TodoApplicationDatabase'
# engine = create_engine(POSTGRESQL_DATABASE_URL)

# For Mysql
# MYSQL_DATABASE_URL = 'mysql+pymysql://root:Ss9079581918@127.0.0.1:3306/TodoApplicationDatabase'
# engine = create_engine(MYSQL_DATABASE_URL)

# For Productiondatabase
PRODUCTION_DATABASE_URL = 'postgresql://civksdyf:Go3OgtyrzQ4xAtA2HSZD0e7cFawlnIAd@bubble.db.elephantsql.com/civksdyf'
engine = create_engine(PRODUCTION_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
