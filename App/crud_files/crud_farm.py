import mysql.connector
from database_connector import get_connection

def get_farm_by_id(farm_id):
    conn = get_connection()
    if not conn: return None
    farm_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT id, name, address, asset_cost FROM farm WHERE id = %s"
        cursor.execute(sql, (farm_id,))
        farm_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения фермы по ID {farm_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return farm_data

def update_farm_details(farm_id, name, address, asset_cost):
    """Обновляет данные указанной фермы."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = "UPDATE farm SET name = %s, address = %s, asset_cost = %s WHERE id = %s"
        val = (
            name if name else None,
            address if address else None,
            asset_cost if asset_cost is not None else None,
            farm_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Ферма ID {farm_id} обновлена, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления фермы ID {farm_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success