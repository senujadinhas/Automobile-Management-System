-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: abc
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `pwd` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'ADM Karunarathna','123','123');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mechanics_details`
--

DROP TABLE IF EXISTS `mechanics_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mechanics_details` (
  `m_id` int NOT NULL,
  `m_name` varchar(100) NOT NULL,
  `m_address` varchar(100) NOT NULL,
  `m_phone` int NOT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mechanics_details`
--

LOCK TABLES `mechanics_details` WRITE;
/*!40000 ALTER TABLE `mechanics_details` DISABLE KEYS */;
INSERT INTO `mechanics_details` VALUES (1,'ASD Hashan Sanjaya','Unknown',123456789),(2,'OP Deshan Ranathunga','Unknown',123456777),(3,'Mahesh Pathmasiri','No,33 C, First Lane, Matara',412259868),(4,'JKR Athapaththu','Unknown',123456789),(5,'Nadun Sameera','45, Main Street',71456897);
/*!40000 ALTER TABLE `mechanics_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_booking`
--

DROP TABLE IF EXISTS `service_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_booking` (
  `s_id` varchar(12) NOT NULL,
  `paymentRON` varchar(45) DEFAULT NULL,
  `datetime` varchar(45) DEFAULT NULL,
  `c_name` varchar(100) DEFAULT NULL,
  `v_regno` varchar(45) DEFAULT NULL,
  `v_make` varchar(45) DEFAULT NULL,
  `v_model` varchar(45) DEFAULT NULL,
  `v_type` varchar(45) DEFAULT NULL,
  `v_engine` varchar(45) DEFAULT NULL,
  `machanic` varchar(100) DEFAULT NULL,
  `v_milage` varchar(45) DEFAULT NULL,
  `manufacturer_d` varchar(45) DEFAULT NULL,
  `other_m_d` varchar(100) DEFAULT NULL,
  `c_nic` varchar(45) DEFAULT NULL,
  `c_gender` varchar(45) DEFAULT NULL,
  `c_email` varchar(100) DEFAULT NULL,
  `c_phone` int DEFAULT NULL,
  `c_city` varchar(45) DEFAULT NULL,
  `c_state` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_booking`
--

LOCK TABLES `service_booking` WRITE;
/*!40000 ALTER TABLE `service_booking` DISABLE KEYS */;
INSERT INTO `service_booking` VALUES ('1','Yes','26-02-23  08:55','Mr. Janaka','CAL-2023','Nissan','Careven','Van','56-4589','ASD Hashan Sanjaya','10000KM','None','None','None','Female','None',0,'None','None'),('2','No','25-01-23  11:14:51','Uresh Karunarathna','0123456','Micro','Panda','Car','123','OP Deshan Ranathunga','None','None','None','None','None','None',0,'None','None'),('3','Yes','26-03-23  08:55','Mr. Janaka','CAL-2023','Bajaj','4 Strok','Three Wheel','YA-2256','JKR Athapaththu','65000Km','Bajaj','RE ','84598657V','Male','abc@123.com',71258963,'Matara','None'),('4','No','26-03-23  08:55','Mr. Janaka','CAL-2023','Bajaj','4 Strok','Three Wheel','YA-2256','JKR Athapaththu','None','None','None','None','None','None',0,'None','None'),('5','Yes','28-01-28 09:30:45','Mr.Jayaweera','Sp CAL 4589','Honda','Civic','Car','1300 CC','Nadun Sameera','56000 Km','Honda','Civic 1.3 LC','89653254V','Male','125@ffs.',154,'kjh','tyhjh');
/*!40000 ALTER TABLE `service_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `u_name` varchar(100) DEFAULT NULL,
  `u_phone` int DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `pwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Senuja Dinhas',718895687,'Senuja@123','123'),(2,'Nuwan Ekanayaka',718895687,'nuwan','1234'),(3,'Jehan',123456789,'jehan@2023','159'),(4,'Jehan',123456789,'jehan@2023','159'),(5,'Mahesh',701329683,'MaheshP','123');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'abc'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-28 18:43:10
