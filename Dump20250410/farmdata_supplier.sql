CREATE DATABASE  IF NOT EXISTS `farmdata` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `farmdata`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: farmdata
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` text,
  `contact_person` text,
  `email` text,
  `phone` text,
  `credit_limit` float DEFAULT NULL,
  `contract_number` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'ООО \"АгроПоставка\"','Иванов Сергей','ivanov@agropostavka.ru','+79123456789',1000000,'Д-001'),(2,'ООО \"СельхозСнаб\"','Петров Алексей','petrov@selhozsnab.ru','+79123456790',800000,'Д-002'),(3,'ООО \"Фермерский Союз\"','Сидоров Иван','sidorov@fermersouz.ru','+79123456791',1200000,'Д-003'),(4,'ООО \"АгроТех\"','Козлов Дмитрий','kozlov@agrotech.ru','+79123456792',900000,'Д-004'),(5,'ООО \"Зеленый Путь\"','Михайлов Олег','mikhailov@greenpath.ru','+79123456793',1100000,'Д-005'),(6,'ООО \"СельхозРесурс\"','Николаев Павел','nikolaev@selhozresurs.ru','+79123456794',950000,'Д-006'),(7,'ООО \"АгроМир\"','Смирнов Виктор','smirnov@agromir.ru','+79123456795',1300000,'Д-007'),(8,'ООО \"ФермаПлюс\"','Кузнецов Артем','kuznetsov@fermaplus.ru','+79123456796',850000,'Д-008'),(9,'ООО \"Сельский Дом\"','Васильев Роман','vasiliev@seldom.ru','+79123456797',1000000,'Д-009'),(10,'ООО \"АгроСфера\"','Морозов Евгений','morozov@agrosfera.ru','+79123456798',1150000,'Д-010');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-10 22:06:33
