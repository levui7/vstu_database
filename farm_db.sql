-- Создание таблицы farm

DROP TABLE IF EXISTS `farm`;
CREATE TABLE farm (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address TEXT,
    asset_cost FLOAT,
    name TEXT,
    market_id INT,
    product_id INT
);
LOCK TABLES `farm` WRITE;
UNLOCK TABLES;

-- Создание таблицы product

DROP TABLE IF EXISTS `product`;
CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    price FLOAT,
    category TEXT,
    volume FLOAT,
    farm_id INT,
    supplier_id INT,
    advertiser_id INT,
    market_id INT,
    distributor_id INT,
    barn_id INT,
    livestock_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id),
    FOREIGN KEY (supplier_id) REFERENCES supplier(id),
    FOREIGN KEY (advertiser_id) REFERENCES advertiser(id),
    FOREIGN KEY (market_id) REFERENCES market(id),
    FOREIGN KEY (distributor_id) REFERENCES distributor(id),
    FOREIGN KEY (barn_id) REFERENCES barn(id),
    FOREIGN KEY (livestock_id) REFERENCES livestock(id)
);
LOCK TABLES `product` WRITE;
UNLOCK TABLES;

-- Создание таблицы field

DROP TABLE IF EXISTS `field`;
CREATE TABLE field (
    id INT PRIMARY KEY AUTO_INCREMENT,
    area FLOAT,
    yield FLOAT,
    farm_id INT,
    farmer_id INT,
    equipment_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id),
    FOREIGN KEY (farmer_id) REFERENCES farmer(id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);
LOCK TABLES `field` WRITE;
UNLOCK TABLES;

-- Создание таблицы farmer

DROP TABLE IF EXISTS `farmer`;
CREATE TABLE farmer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name TEXT,
    work_experience INT,
    labor_payment FLOAT,
    farm_id INT,
    livestock_id INT,
    equipment_id INT UNIQUE, -- Связь 1:1 с equipment
    FOREIGN KEY (farm_id) REFERENCES farm(id),
    FOREIGN KEY (livestock_id) REFERENCES livestock(id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);
LOCK TABLES `farmer` WRITE;
UNLOCK TABLES;

-- Создание таблицы equipment

DROP TABLE IF EXISTS `equipment`;
CREATE TABLE equipment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    conditions TEXT,
    cost FLOAT,
    warranty DATE,
    farm_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id)
);
LOCK TABLES `equipment` WRITE;
UNLOCK TABLES;

-- Создание таблицы supplier

DROP TABLE IF EXISTS `supplier`;
CREATE TABLE supplier (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    credit_limit FLOAT,
    contract_number TEXT
);
LOCK TABLES `supplier` WRITE;
UNLOCK TABLES;

-- Создание таблицы advertiser

DROP TABLE IF EXISTS `advertiser`;
CREATE TABLE advertiser (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    effectiveness INT,
    service_cost FLOAT
);
LOCK TABLES `advertiser` WRITE;
UNLOCK TABLES;

-- Создание таблицы market

DROP TABLE IF EXISTS `market`;
CREATE TABLE market (
    id INT PRIMARY KEY AUTO_INCREMENT,
    money_volume FLOAT,
    trading_platforms INT,
    price_category TEXT,
    market_segment TEXT
);
LOCK TABLES `market` WRITE;
UNLOCK TABLES;

-- Создание таблицы distributor

DROP TABLE IF EXISTS `distributor`;
CREATE TABLE distributor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    sales_volume FLOAT,
    license TEXT
);
LOCK TABLES `distributor` WRITE;
UNLOCK TABLES;

-- Создание таблицы barn

DROP TABLE IF EXISTS `barn`;
CREATE TABLE barn (
    id INT PRIMARY KEY AUTO_INCREMENT,
    capacity FLOAT,
    conditions TEXT,
    wear_assessment TEXT,
    farm_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id)
);
LOCK TABLES `barn` WRITE;
UNLOCK TABLES;

-- Создание таблицы livestock

DROP TABLE IF EXISTS `livestock`;
CREATE TABLE livestock (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category TEXT,
    productivity FLOAT,
    maintenance_conditions TEXT,
    feed_volume FLOAT,
    quantity INT,
    purpose TEXT,
    farm_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id)
);
LOCK TABLES `livestock` WRITE;
UNLOCK TABLES;