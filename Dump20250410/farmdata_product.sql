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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `category` text,
  `volume` float DEFAULT NULL,
  `farm_id` int DEFAULT NULL,
  `supplier_id` int DEFAULT NULL,
  `advertiser_id` int DEFAULT NULL,
  `market_id` int DEFAULT NULL,
  `distributor_id` int DEFAULT NULL,
  `barn_id` int DEFAULT NULL,
  `livestock_id` int DEFAULT NULL,
  `field_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_id` (`farm_id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `advertiser_id` (`advertiser_id`),
  KEY `market_id` (`market_id`),
  KEY `distributor_id` (`distributor_id`),
  KEY `barn_id` (`barn_id`),
  KEY `livestock_id` (`livestock_id`),
  KEY `field_id` (`field_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`farm_id`) REFERENCES `farm` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`),
  CONSTRAINT `product_ibfk_3` FOREIGN KEY (`advertiser_id`) REFERENCES `advertiser` (`id`),
  CONSTRAINT `product_ibfk_4` FOREIGN KEY (`market_id`) REFERENCES `market` (`id`),
  CONSTRAINT `product_ibfk_5` FOREIGN KEY (`distributor_id`) REFERENCES `distributor` (`id`),
  CONSTRAINT `product_ibfk_6` FOREIGN KEY (`barn_id`) REFERENCES `barn` (`id`),
  CONSTRAINT `product_ibfk_7` FOREIGN KEY (`livestock_id`) REFERENCES `livestock` (`id`),
  CONSTRAINT `product_ibfk_8` FOREIGN KEY (`field_id`) REFERENCES `field` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,150,'Молоко',1000,1,1,1,1,1,1,1,1),(2,80,'Мясо',500,2,2,2,2,2,2,2,2),(3,2.5,'Яйца',10000,3,3,3,3,3,3,3,3),(4,300,'Шерсть',200,4,4,4,4,4,4,4,4),(5,120,'Молоко',800,5,5,5,5,5,5,5,5),(6,140,'Молоко',900,6,6,6,6,6,6,6,6),(7,90,'Мясо',600,7,7,7,7,7,7,7,7),(8,2.8,'Яйца',9000,8,8,8,8,8,8,8,8),(9,280,'Шерсть',180,9,9,9,9,9,9,9,9),(10,110,'Молоко',850,10,10,10,10,10,10,10,10);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-10 22:06:32
