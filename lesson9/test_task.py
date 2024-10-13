from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:0000@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_get_teacher():
    db = create_engine(db_connection_string)
    db.execute("select * from teacher").fetchall()


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("""insert into teacher
               ("teacher_id", "email", "group_id") values
                (:teacher_id, :email, :group_id)""")
    db.execute(sql, teacher_id='101', email='name@gmail.com', group_id='101')


def test_up_data():
    db = create_engine(db_connection_string)
    sql = text("update teacher set email = :email where group_id = :group_id")
    db.execute(sql, email='new-name@gmail.com', group_id=101)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from teacher where group_id = :group_id")
    db.execute(sql, group_id='101')
