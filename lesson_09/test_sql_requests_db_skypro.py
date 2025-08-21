from sqlalchemy import create_engine, text

db_connection_string = ""

db = create_engine(db_connection_string)


def select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    connection.close()
    return rows


def create_subject(subject_id, subject_title):
    connection = db.connect()
    transaction = connection.begin()
    text_insert = text("INSERT into subject (subject_id, subject_title) "
                       "VALUES (:new_subject_id, :new_subject_title)")
    connection.execute(text_insert, {'new_subject_id': subject_id,
                                     'new_subject_title': subject_title})
    transaction.commit()
    connection.close()


def get_max_id():
    connection = db.connect()
    result = connection.execute(text("SELECT MAX(subject_id) FROM subject"))
    max_id = result.scalar()
    connection.close()
    return max_id


def change_subject(changed_subject_id, changed_subject_title):
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE subject SET subject_title = :changed_subject_title "
               "where subject_id = :subject_id")
    connection.execute(sql, {'changed_subject_title': changed_subject_title,
                       'subject_id': changed_subject_id})
    transaction.commit()
    connection.close()


def get_subject_by_id(subject_id):
    conn = db.connect()
    sql = text("SELECT * FROM subject WHERE subject_id = :selected_id")
    result = conn.execute(sql, {"selected_id": subject_id})
    rows = result.mappings().first()
    conn.close()
    return rows


def delete(subject_id):
    connection = db.connect()
    transaction = connection.begin()
    text_delete = (text("DELETE from subject where subject_id = :id"))
    connection.execute(text_delete, {'id': subject_id})
    transaction.commit()
    connection.close()


def test_create_subject():
    # строки до создания предмета
    row_before = select()
    max_id = get_max_id()
    new_id = max_id + 1 if max_id else 1  # Обработка пустой таблицы
    create_subject(new_id, 'PE')

    # строки после создания предмета
    rows_after = select()

    delete(new_id)

    assert len(rows_after) - len(row_before) == 1


def test_change_subject():
    max_id = get_max_id()
    new_id = max_id + 1 if max_id else 1  # Обработка пустой таблицы
    create_subject(new_id, 'PE')
    change_subject(new_id, "Music")
    rows = get_subject_by_id(new_id)

    assert rows["subject_title"] == "Music"

    delete(new_id)


def test_delete_subject():
    max_id = get_max_id()
    new_id = max_id + 1 if max_id else 1  # Обработка пустой таблицы
    create_subject(new_id, 'PE')
    rows_before_deleted = select()
    delete(new_id)
    rows_after_deleted = select()

    assert len(rows_before_deleted) - len(rows_after_deleted) == 1
    assert get_subject_by_id(new_id) is None, "Запись не была удалена"
