import mysql.connector
from database_connector import get_connection, db_farm_id

def create_barn(capacity, conditions, wear_assessment, farm_id=db_farm_id):
    """Добавляет новый амбар в БД."""
    conn = get_connection()
    if not conn: return None
    last_id = None
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO barn 
                   (capacity, conditions, wear_assessment, farm_id) 
                   VALUES (%s, %s, %s, %s)"""
        val = (
            capacity if capacity is not None else None, # Для FLOAT
            conditions if conditions else None,         # Для TEXT
            wear_assessment if wear_assessment else None, # Для TEXT
            farm_id # Для INT (предполагается, что farm_id всегда будет)
        )
        cursor.execute(sql, val)
        conn.commit()
        last_id = cursor.lastrowid
        print(f"Амбар добавлен с ID: {last_id}")
    except mysql.connector.Error as err:
        print(f"Ошибка создания амбара: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return last_id

def get_all_barns_for_farm(farm_id=db_farm_id):
    """Получает список всех амбаров для указанной фермы."""
    conn = get_connection()
    if not conn: return []
    barns_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        # farm_id в SELECT не обязателен, если мы и так фильтруем по нему,
        # но может быть полезен для проверки.
        sql = """SELECT id, capacity, conditions, wear_assessment, farm_id
                   FROM barn 
                   WHERE farm_id = %s 
                   ORDER BY id"""
        cursor.execute(sql, (farm_id,))
        barns_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка амбаров для фермы ID {farm_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return barns_list

def get_barn_by_id(barn_id):
    """Получает один амбар по его ID."""
    conn = get_connection()
    if not conn: return None
    barn_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT id, capacity, conditions, wear_assessment, farm_id FROM barn WHERE id = %s"
        cursor.execute(sql, (barn_id,))
        barn_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения амбара по ID {barn_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return barn_data

def update_barn(barn_id, capacity, conditions, wear_assessment, farm_id=db_farm_id):
    """Обновляет существующий амбар в БД."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = """UPDATE barn SET 
                   capacity = %s, conditions = %s, wear_assessment = %s, farm_id = %s
                   WHERE id = %s"""
        val = (
            capacity if capacity is not None else None,
            conditions if conditions else None,
            wear_assessment if wear_assessment else None,
            farm_id, # farm_id обычно не меняется при обновлении, если он уже задан, но можно разрешить
            barn_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Амбар ID {barn_id} обновлен, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления амбара ID {barn_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success

def delete_barn(barn_id):
    """Удаляет амбар из БД по его ID."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        # ВАЖНО: Если на barn ссылаются из других таблиц (например, product.barn_id),
        # это удаление может быть запрещено. Нужно либо сначала обновить/удалить
        # зависимые записи, либо настроить ON DELETE SET NULL / ON DELETE CASCADE в БД.
        cursor.execute("DELETE FROM barn WHERE id = %s", (barn_id,))
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Амбар ID {barn_id} удален, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка удаления амбара ID {barn_id}: {err}") # Ошибка может быть из-за FK
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success