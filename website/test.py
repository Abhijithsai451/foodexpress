import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from jinja2.nodes import List
from sqlalchemy import create_engine
from sqlalchemy.engine import CursorResult
from sqlalchemy.sql.functions import user

DB_NAME = "foodexpress"
url = 'mysql+mysqlconnector://root:password@localhost/foodexpress'

engine = create_engine(url, echo=True)
connection = engine.connect()

user_table = sqlalchemy.Table('user', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
query = sqlalchemy.select(user_table)
result: CursorResult = connection.execute(query)

users: List[user] = legacy_cursor_result.fetchall()
