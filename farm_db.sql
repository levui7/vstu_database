-- Создание таблицы farm
CREATE TABLE farm (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address TEXT,
    asset_cost FLOAT,
    name TEXT,
    market_id INT,
    product_id INT
);

-- Создание таблицы product
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

-- Создание таблицы field
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

-- Создание таблицы farmer
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

-- Создание таблицы equipment
CREATE TABLE equipment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    conditions TEXT,
    cost FLOAT,
    warranty DATE,
    farm_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id)
);

-- Создание таблицы supplier
CREATE TABLE supplier (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    credit_limit FLOAT,
    contract_number TEXT
);

-- Создание таблицы advertiser
CREATE TABLE advertiser (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    effectiveness INT,
    service_cost FLOAT
);

-- Создание таблицы market
CREATE TABLE market (
    id INT PRIMARY KEY AUTO_INCREMENT,
    money_volume FLOAT,
    trading_platforms INT,
    price_category TEXT,
    market_segment TEXT
);

-- Создание таблицы distributor
CREATE TABLE distributor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name TEXT,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    sales_volume FLOAT,
    license TEXT
);

-- Создание таблицы barn
CREATE TABLE barn (
    id INT PRIMARY KEY AUTO_INCREMENT,
    capacity FLOAT,
    conditions TEXT,
    wear_assessment TEXT,
    farm_id INT,
    FOREIGN KEY (farm_id) REFERENCES farm(id)
);

-- Создание таблицы livestock
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