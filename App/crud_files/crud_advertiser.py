import mysql.connector
from database_connector import get_connection

def create_advertiser(company_name, contact_person, email, phone, effectiveness, service_cost):
    """Добавляет нового рекламодателя в БД."""
    conn = get_connection()
    if not conn: return None
    last_id = None
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO advertiser 
                   (company_name, contact_person, email, phone, effectiveness, service_cost) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        # Передаем None для полей, которые могут быть NULL и не предоставлены
        val = (
            company_name if company_name else None,
            contact_person if contact_person else None,
            email if email else None,
            phone if phone else None,
            effectiveness if effectiveness is not None else None,  # Для чисел проверяем на None
            service_cost if service_cost is not None else None  # Для чисел проверяем на None
        )
        cursor.execute(sql, val)
        conn.commit()
        last_id = cursor.lastrowid  # Получаем ID вставленной записи
        print(f"Рекламодатель добавлен с ID: {last_id}")
    except mysql.connector.Error as err:
        print(f"Ошибка создания рекламодателя: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return last_id


def get_all_advertisers():
    """Получает список всех рекламодателей."""
    conn = get_connection()
    if not conn: return []
    advertisers_list = []
    try:
        cursor = conn.cursor(dictionary=True)  # Возвращает строки как словари
        sql = """SELECT id, company_name, contact_person, email, phone, 
                   effectiveness, service_cost 
                   FROM advertiser ORDER BY company_name, id"""
        cursor.execute(sql)
        advertisers_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка рекламодателей: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return advertisers_list


def get_advertiser_by_id(advertiser_id):
    """Получает одного рекламодателя по его ID."""
    conn = get_connection()
    if not conn: return None
    advertiser_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT id, company_name, contact_person, email, phone, 
                   effectiveness, service_cost 
                   FROM advertiser WHERE id = %s"""
        cursor.execute(sql, (advertiser_id,))
        advertiser_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения рекламодателя по ID {advertiser_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return advertiser_data


def update_advertiser(advertiser_id, company_name, contact_person, email, phone, effectiveness, service_cost):
    """Обновляет существующего рекламодателя в БД."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = """UPDATE advertiser SET 
                   company_name = %s, contact_person = %s, email = %s, 
                   phone = %s, effectiveness = %s, service_cost = %s
                   WHERE id = %s"""
        val = (
            company_name if company_name else None,
            contact_person if contact_person else None,
            email if email else None,
            phone if phone else None,
            effectiveness if effectiveness is not None else None,
            service_cost if service_cost is not None else None,
            advertiser_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)  # True, если хотя бы одна строка была обновлена
        print(f"Рекламодатель ID {advertiser_id} обновлен, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления рекламодателя ID {advertiser_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success


def delete_advertiser(advertiser_id):
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM advertiser WHERE id = %s", (advertiser_id,))
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Рекламодатель ID {advertiser_id} удален, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка удаления рекламодателя ID {advertiser_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success