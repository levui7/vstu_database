import mysql.connector
from database_connector import get_connection, db_farm_id

def create_field(area, yield_value, farmer_id, equipment_id, farm_id=db_farm_id):
    conn = get_connection()
    if not conn: return None
    last_id = None
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO field 
                   (area, `yield`, farm_id, farmer_id, equipment_id) 
                   VALUES (%s, %s, %s, %s, %s)""" # Используем `yield` в SQL
        val = (
            area if area is not None else None,
            yield_value if yield_value is not None else None, # Используем yield_value для параметра Python
            farm_id,
            farmer_id if farmer_id is not None else None,
            equipment_id if equipment_id is not None else None
        )
        cursor.execute(sql, val)
        conn.commit()
        last_id = cursor.lastrowid
        print(f"Поле добавлено с ID: {last_id}")
    except mysql.connector.Error as err:
        print(f"Ошибка создания поля: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return last_id

def get_all_fields_for_farm(farm_id=db_farm_id):
    """Получает список всех полей для указанной фермы."""
    conn = get_connection()
    if not conn: return []
    fields_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        # В SELECT выбираем все нужные поля, включая FK, если их нужно будет отображать
        # или использовать для JOIN с именами фермеров/оборудования в GUI.
        sql = """SELECT id, area, `yield`, farm_id, farmer_id, equipment_id
                   FROM field 
                   WHERE farm_id = %s 
                   ORDER BY id""" # Используем `yield` в SQL
        cursor.execute(sql, (farm_id,))
        fields_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка полей для фермы ID {farm_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return fields_list

def get_field_by_id(field_id):
    """Получает одно поле по его ID."""
    conn = get_connection()
    if not conn: return None
    field_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT id, area, `yield`, farm_id, farmer_id, equipment_id 
                   FROM field WHERE id = %s""" # Используем `yield` в SQL
        cursor.execute(sql, (field_id,))
        field_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения поля по ID {field_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return field_data

def update_field(field_id, area, yield_value, farmer_id, equipment_id, farm_id=db_farm_id):
    """Обновляет существующее поле в БД."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = """UPDATE field SET 
                   area = %s, `yield` = %s, farm_id = %s, 
                   farmer_id = %s, equipment_id = %s
                   WHERE id = %s""" # Используем `yield` в SQL
        val = (
            area if area is not None else None,
            yield_value if yield_value is not None else None,
            farm_id,
            farmer_id if farmer_id is not None else None,
            equipment_id if equipment_id is not None else None,
            field_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Поле ID {field_id} обновлено, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления поля ID {field_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success

def delete_field(field_id):
    """Удаляет поле из БД по его ID."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        # ВАЖНО: Если на field ссылаются из других таблиц, это удаление может быть запрещено.
        cursor.execute("DELETE FROM field WHERE id = %s", (field_id,))
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Поле ID {field_id} удалено, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка удаления поля ID {field_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success