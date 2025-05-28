import mysql.connector
from database_connector import get_connection, db_farm_id

def create_product(category, price, volume,
                   supplier_id, advertiser_id, market_id,
                   distributor_id, barn_id, livestock_id, field_id,
                   farm_id=db_farm_id): # farm_id по умолчанию
    """Добавляет новый продукт в БД."""
    conn = get_connection()
    if not conn: return None
    last_id = None
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO product (
                    category, price, volume, farm_id, supplier_id, advertiser_id, 
                    market_id, distributor_id, barn_id, livestock_id, field_id 
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (
            category if category else None,
            price if price is not None else None,
            volume if volume is not None else None,
            farm_id, # Всегда используем db_farm_id
            supplier_id if supplier_id is not None else None,
            advertiser_id if advertiser_id is not None else None,
            market_id if market_id is not None else None,
            distributor_id if distributor_id is not None else None,
            barn_id if barn_id is not None else None,
            livestock_id if livestock_id is not None else None,
            field_id if field_id is not None else None # Добавил field_id
        )
        cursor.execute(sql, val)
        conn.commit()
        last_id = cursor.lastrowid
        print(f"Продукт добавлен с ID: {last_id}")
    except mysql.connector.Error as err:
        print(f"Ошибка создания продукта: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return last_id

def get_all_products_for_farm(farm_id=db_farm_id):
    """Получает все продукты для указанной фермы."""
    conn = get_connection()
    if not conn: return []
    products_list = []
    try:
        cursor = conn.cursor(dictionary=True)
        # Выбираем все поля, которые есть в таблице (кроме farm_id, т.к. он известен)
        sql = """
            SELECT 
                p.id, p.category, p.price, p.volume, p.supplier_id, 
                p.advertiser_id, p.market_id, p.distributor_id, 
                p.barn_id, p.livestock_id, p.field_id 
            FROM product p
            WHERE p.farm_id = %s
            ORDER BY p.category, p.id
        """
        cursor.execute(sql, (farm_id,))
        products_list = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка получения списка продуктов для фермы {farm_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return products_list

def get_product_by_id(product_id):
    """Получает один продукт по его ID."""
    conn = get_connection()
    if not conn: return None
    product_data = None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT 
                id, category, price, volume, farm_id, supplier_id, 
                advertiser_id, market_id, distributor_id, 
                barn_id, livestock_id, field_id
            FROM product
            WHERE id = %s
        """
        cursor.execute(sql, (product_id,))
        product_data = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Ошибка получения продукта по ID {product_id}: {err}")
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return product_data

def update_product(product_id, category, price, volume,
                   supplier_id, advertiser_id, market_id,
                   distributor_id, barn_id, livestock_id, field_id,
                   farm_id=db_farm_id): # farm_id обычно не меняется при обновлении
    """Обновляет существующий продукт в БД."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        sql = """UPDATE product SET 
                    category = %s, price = %s, volume = %s, 
                    farm_id = %s, supplier_id = %s, advertiser_id = %s, 
                    market_id = %s, distributor_id = %s, barn_id = %s, 
                    livestock_id = %s, field_id = %s
                WHERE id = %s"""
        val = (
            category if category else None,
            price if price is not None else None,
            volume if volume is not None else None,
            farm_id, # Передаем farm_id, даже если он не меняется
            supplier_id if supplier_id is not None else None,
            advertiser_id if advertiser_id is not None else None,
            market_id if market_id is not None else None,
            distributor_id if distributor_id is not None else None,
            barn_id if barn_id is not None else None,
            livestock_id if livestock_id is not None else None,
            field_id if field_id is not None else None,
            product_id
        )
        cursor.execute(sql, val)
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Продукт ID {product_id} обновлен, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка обновления продукта ID {product_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success

def delete_product(product_id):
    """Удаляет продукт из БД по его ID."""
    conn = get_connection()
    if not conn: return False
    success = False
    try:
        cursor = conn.cursor()
        # Убедитесь, что на этот продукт нет ссылок из других таблиц (например, из таблицы заказов),
        # если у вас есть такие связи и настроены ограничения FK.
        cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        conn.commit()
        success = (cursor.rowcount > 0)
        print(f"Продукт ID {product_id} удален, затронуто строк: {cursor.rowcount}")
    except mysql.connector.Error as err:
        print(f"Ошибка удаления продукта ID {product_id}: {err}")
        if conn: conn.rollback()
    finally:
        if conn and conn.is_connected():
            if 'cursor' in locals() and cursor: cursor.close()
            conn.close()
    return success