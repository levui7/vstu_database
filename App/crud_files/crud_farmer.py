import mysql.connector
from database_connector import get_connection, db_farm_id

def create_farmer(full_name, work_experience, labor_payment,
                  livestock_id, equipment_id, farm_id=db_farm_id): # farm_id по умолчанию
    """Добавляет нового фермера в БД."""
    conn = get_connection()
    if not conn: return None
    last_id = None
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO farmer 
                   (full_name, work_experience, labor_payment, farm_id, livestock_id, equipment_id) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (
            full_name if full_name else None,
            work_experience if work_experience is not None else None,
            labor_payment if labor_payment is not None else None,
            farm_id, # Предполагаем, что farm_id всегда будет (из SINGLE_FARM_ID)
            livestock_id if livestock_id is not None else None,
            equipment_id if equipment_id is not None else None
        )
        cursor.execute(sql, val)
        conn.commit()
        last_id = cursor.lastrowid
        print(f"Фермер добавлен с ID: {last_id}")
    except mysql.connector.Error as err:
        print(f"Ошибка создания фермера: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return last_id

def get_all_farmers_for_farm(farm_id=db_farm_id):
    """Получает список всех фермеров для указанной фермы."""
    conn = get_connection()
    if not conn: return []
    farmers_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        # Выбираем все поля, включая FK, чтобы их можно было отобразить или использовать
        sql = """SELECT id, full_name, work_experience, labor_payment, 
                   farm_id, livestock_id, equipment_id
                   FROM farmer 
                   WHERE farm_id = %s 
                   ORDER BY full_name, id"""
        cursor.execute(sql, (farm_id,))
        farmers_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка фермеров для фермы ID {farm_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return farmers_list

def get_farmer_by_id(farmer_id):
    """Получает одного фермера по его ID."""
    conn = get_connection()
    if not conn: return None
    farmer_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT id, full_name, work_experience, labor_payment, 
                   farm_id, livestock_id, equipment_id 
                   FROM farmer WHERE id = %s"""
        cursor.execute(sql, (farmer_id,))
        farmer_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения фермера по ID {farmer_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return farmer_data

def update_farmer(farmer_id, full_name, work_experience, labor_payment,
                  livestock_id, equipment_id, farm_id=db_farm_id): # farm_id обычно не меняется
    """Обновляет существующего фермера в БД."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = """UPDATE farmer SET 
                   full_name = %s, work_experience = %s, labor_payment = %s, 
                   farm_id = %s, livestock_id = %s, equipment_id = %s
                   WHERE id = %s"""
        val = (
            full_name if full_name else None,
            work_experience if work_experience is not None else None,
            labor_payment if labor_payment is not None else None,
            farm_id,
            livestock_id if livestock_id is not None else None,
            equipment_id if equipment_id is not None else None,
            farmer_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Фермер ID {farmer_id} обновлен, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления фермера ID {farmer_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success

def delete_farmer(farmer_id):
    """Удаляет фермера из БД по его ID."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        # ВАЖНО: Если на farmer ссылаются из других таблиц (например, field.farmer_id),
        # это удаление может быть запрещено.
        cursor.execute("DELETE FROM farmer WHERE id = %s", (farmer_id,))
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Фермер ID {farmer_id} удален, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка удаления фермера ID {farmer_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success