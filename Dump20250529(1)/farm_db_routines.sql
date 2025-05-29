-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: farm_db
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
-- Temporary view structure for view `activefarmersonproductivefields`
--

DROP TABLE IF EXISTS `activefarmersonproductivefields`;
/*!50001 DROP VIEW IF EXISTS `activefarmersonproductivefields`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `activefarmersonproductivefields` AS SELECT 
 1 AS `farmer_id`,
 1 AS `farmer_name`,
 1 AS `farmer_experience`,
 1 AS `farm_name`,
 1 AS `field_id`,
 1 AS `field_area`,
 1 AS `field_yield`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `farmequipmentsummary`
--

DROP TABLE IF EXISTS `farmequipmentsummary`;
/*!50001 DROP VIEW IF EXISTS `farmequipmentsummary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `farmequipmentsummary` AS SELECT 
 1 AS `farm_id`,
 1 AS `farm_name`,
 1 AS `total_equipment_units`,
 1 AS `total_equipment_cost`,
 1 AS `units_needing_attention`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `productsupplierdetails`
--

DROP TABLE IF EXISTS `productsupplierdetails`;
/*!50001 DROP VIEW IF EXISTS `productsupplierdetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `productsupplierdetails` AS SELECT 
 1 AS `product_id`,
 1 AS `product_category`,
 1 AS `product_price`,
 1 AS `product_volume`,
 1 AS `supplier_company`,
 1 AS `supplier_contact_person`,
 1 AS `supplier_phone`,
 1 AS `farm_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `activefarmersonproductivefields`
--

/*!50001 DROP VIEW IF EXISTS `activefarmersonproductivefields`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `activefarmersonproductivefields` AS select `fm`.`id` AS `farmer_id`,`fm`.`full_name` AS `farmer_name`,`fm`.`work_experience` AS `farmer_experience`,`f`.`name` AS `farm_name`,`fi`.`id` AS `field_id`,`fi`.`area` AS `field_area`,`fi`.`yield` AS `field_yield` from ((`farmer` `fm` join `field` `fi` on((`fm`.`id` = `fi`.`farmer_id`))) join `farm` `f` on((`fm`.`farm_id` = `f`.`id`))) where ((`fi`.`yield` > 5.0) and (`fm`.`work_experience` > 2)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `farmequipmentsummary`
--

/*!50001 DROP VIEW IF EXISTS `farmequipmentsummary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `farmequipmentsummary` AS select `f`.`id` AS `farm_id`,`f`.`name` AS `farm_name`,count(`e`.`id`) AS `total_equipment_units`,sum(`e`.`cost`) AS `total_equipment_cost`,sum((case when (`e`.`conditions` in ('Требует обслуживания','Требует ремонта','Неисправно')) then 1 else 0 end)) AS `units_needing_attention` from (`farm` `f` left join `equipment` `e` on((`f`.`id` = `e`.`farm_id`))) group by `f`.`id`,`f`.`name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `productsupplierdetails`
--

/*!50001 DROP VIEW IF EXISTS `productsupplierdetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `productsupplierdetails` AS select `p`.`id` AS `product_id`,`p`.`category` AS `product_category`,`p`.`price` AS `product_price`,`p`.`volume` AS `product_volume`,`s`.`company_name` AS `supplier_company`,`s`.`contact_person` AS `supplier_contact_person`,`s`.`phone` AS `supplier_phone`,`f`.`name` AS `farm_name` from ((`product` `p` left join `supplier` `s` on((`p`.`supplier_id` = `s`.`id`))) left join `farm` `f` on((`p`.`farm_id` = `f`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-29  9:55:17
