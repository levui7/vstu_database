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
-- Table structure for table `advertiser`
--

DROP TABLE IF EXISTS `advertiser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `advertiser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` text,
  `contact_person` text,
  `email` text,
  `phone` text,
  `effectiveness` int DEFAULT NULL,
  `service_cost` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advertiser`
--

LOCK TABLES `advertiser` WRITE;
/*!40000 ALTER TABLE `advertiser` DISABLE KEYS */;
INSERT INTO `advertiser` VALUES (1,'ООО \"РекламаАгро\"','Соколова Анна','sokolova@reklamaagro.ru','+79123456801',85,50000),(2,'ООО \"АгроПромо\"','Крылова Мария','krylova@agropromo.ru','+79123456802',90,60000),(3,'ООО \"ФермерМедиа\"','Лебедева Ольга','lebedeva@fermermedia.ru','+79123456803',75,45000),(4,'ООО \"АгроБаннер\"','Зайцева Елена','zaitseva@agrobanner.ru','+79123456804',80,55000),(5,'ООО \"СельхозРеклама\"','Попова Ирина','popova@selhozreklama.ru','+79123456805',88,52000),(6,'ООО \"АгроВидео\"','Степанова Светлана','stepanova@agrovideo.ru','+79123456806',82,48000),(7,'ООО \"ФермерТВ\"','Григорьева Юлия','grigorieva@fermertv.ru','+79123456807',78,47000),(8,'ООО \"АгроСМИ\"','Федорова Дарья','fedorova@agrosmi.ru','+79123456808',87,51000),(9,'ООО \"Сельский Баннер\"','Макарова Екатерина','makarova@selbanner.ru','+79123456809',83,49000),(10,'ООО \"АгроПлакат\"','Новикова Алина','novikova@agroplakat.ru','+79123456810',86,53000);
/*!40000 ALTER TABLE `advertiser` ENABLE KEYS */;
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
