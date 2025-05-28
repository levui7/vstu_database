import mysql.connector
from database_config import DB_CONFIG, db_farm_id

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к БД: {err}")
        return None

# CRUD для advertiser
from crud_files.crud_advertiser import (
    create_advertiser,
    get_all_advertisers,
    get_advertiser_by_id,
    update_advertiser,
    delete_advertiser
)

# CRUD для barn
from crud_files.crud_barn import (
    create_barn,
    get_all_barns_for_farm,
    get_barn_by_id,
    update_barn,
    delete_barn
)

# Урезанные CRUD для farm
from crud_files.crud_farm import (
    get_farm_by_id,
    update_farm_details
)

# CRUD для farmer
from crud_files.crud_farmer import (
    create_farmer,
    get_all_farmers_for_farm,
    get_farmer_by_id,
    update_farmer,
    delete_farmer
)

# CRUD для field
from crud_files.crud_field import (
    create_field,
    get_all_fields_for_farm,
    get_field_by_id,
    update_field,
    delete_field
)

# CRUD для product
from crud_files.crud_product import (
    create_product,
    get_all_products_for_farm,
    get_product_by_id,
    update_product,
    delete_product
)