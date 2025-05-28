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
-- Table structure for table `distributor`
--

DROP TABLE IF EXISTS `distributor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distributor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` text,
  `contact_person` text,
  `email` text,
  `phone` text,
  `sales_volume` float DEFAULT NULL,
  `license` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distributor`
--

LOCK TABLES `distributor` WRITE;
/*!40000 ALTER TABLE `distributor` DISABLE KEYS */;
INSERT INTO `distributor` VALUES (1,'ООО \"АгроДистриб\"','Белов Андрей','belov@agrodistrib.ru','+79123456811',2000000,'Л-001'),(2,'ООО \"СельхозТорг\"','Ковалев Игорь','kovalev@selhoztorg.ru','+79123456812',1800000,'Л-002'),(3,'ООО \"ФермерМаркет\"','Лебедев Виктор','lebedev@fermermarket.ru','+79123456813',2200000,'Л-003'),(4,'ООО \"АгроСбыт\"','Соколов Павел','sokolov@agrosbyt.ru','+79123456814',1900000,'Л-004'),(5,'ООО \"Сельский Сбыт\"','Морозов Олег','morozov@selhozbbyt.ru','+79123456815',2100000,'Л-005'),(6,'ООО \"АгроТрейд\"','Кузнецов Артем','kuznetsov@agrotrade.ru','+79123456816',1950000,'Л-006'),(7,'ООО \"ФермерСбыт\"','Васильев Роман','vasiliev@fermersbyt.ru','+79123456817',2300000,'Л-007'),(8,'ООО \"АгроПостав\"','Смирнов Виктор','smirnov@agropostav.ru','+79123456818',1850000,'Л-008'),(9,'ООО \"СельхозМаркет\"','Николаев Павел','nikolaev@selhozmarket.ru','+79123456819',2050000,'Л-009'),(10,'ООО \"АгроСеть\"','Иванов Сергей','ivanov@agroset.ru','+79123456820',2150000,'Л-010');
/*!40000 ALTER TABLE `distributor` ENABLE KEYS */;
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
