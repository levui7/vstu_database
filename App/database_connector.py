import mysql.connector
from database_config import DB_CONFIG, db_farm_id

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к БД: {err}")
        return None

# --- Функции для таблицы Farm ---
def get_all_farms():
    """Возвращает список всех ферм."""
    conn = get_connection()
    if not conn:
        return []
    farms_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, address, asset_cost FROM farm ORDER BY name")
        farms_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка ферм: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return farms_list

def get_farm_details(farm_id=db_farm_id): # По умолчанию берем детали нашей фермы
    """Возвращает данные указанной фермы."""
    conn = get_connection()
    if not conn:
        return None
    farm_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, address, asset_cost FROM farm WHERE id = %s", (farm_id,))
        farm_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения фермы по ID {farm_id}: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return farm_data