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
-- Table structure for table `farm`
--

DROP TABLE IF EXISTS `farm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` text,
  `asset_cost` float DEFAULT NULL,
  `name` text,
  `market_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm`
--

LOCK TABLES `farm` WRITE;
/*!40000 ALTER TABLE `farm` DISABLE KEYS */;
INSERT INTO `farm` VALUES (1,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',1,1),(2,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',2,2),(3,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',3,3),(4,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',4,4),(5,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',5,5),(6,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',6,6),(7,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',7,7),(8,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',8,8),(9,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',9,9),(10,'ул. Центральная, д. 10, с. Ивановка',5000000,'Ферма \"Золотой Колос\"',10,10);
/*!40000 ALTER TABLE `farm` ENABLE KEYS */;
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
