-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: loja
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `cidade` varchar(15) DEFAULT NULL,
  `telefone` varchar(30) DEFAULT NULL,
  `cep` varchar(15) DEFAULT NULL,
  `endereco` varchar(40) DEFAULT NULL,
  `numero` varchar(15) DEFAULT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (6,'Ricardo','Xique-Xique','1234567891','16901125','Guararapes','2213','Stella Maris'),(7,'Denise','Guaraçai','123456789','16901125','Jardins','1234','Europa'),(8,'Pedro','Murutinga','123456789','16901125','França','3456','Villa'),(9,'lauany','','','','','',''),(11,'','',NULL,'','','',''),(12,'Vinicius','Andradina ',NULL,'16901410','Rua piaui','1357','piscina '),(13,'Douglas Camata','das','12323123','13213','13213','1321','dsd'),(15,'Julio moreira','fgbnh','1234','12345','qwesfg','cxvbn',' vfbn'),(16,'bruna','andradina','73620','82656214','homero','6543','stella'),(17,'Bianca Justino Justino','Andradina','18991057115','1600400','','','');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacoes`
--

DROP TABLE IF EXISTS `notificacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificacoes` (
  `id_notificacao` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(500) DEFAULT NULL,
  `id_venda` int DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_notificacao`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacoes`
--

LOCK TABLES `notificacoes` WRITE;
/*!40000 ALTER TABLE `notificacoes` DISABLE KEYS */;
INSERT INTO `notificacoes` VALUES (1,'Venda para o cliente Douglas Camata',NULL,3),(2,'Notificação teste 01',NULL,3),(3,NULL,35,NULL),(4,'Venda realizada para o cliente (Denise)',36,3),(5,'Venda realizada para o cliente (Douglas Camata)',37,3),(6,'Venda realizada para o cliente (Pedro)',38,3),(7,'Venda realizada para o cliente (Denise)',39,3),(8,'Venda realizada para o cliente (Douglas Camata)',40,3),(9,'Venda realizada para o cliente (Douglas Camata)',41,3),(10,'Venda realizada para o cliente (Ricardo)',42,3),(11,'Venda realizada para o cliente (lauany)',43,3),(12,'Venda realizada para o cliente (Julio moreira)',44,3);
/*!40000 ALTER TABLE `notificacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos` (
  `ID_PRODUTO` int NOT NULL AUTO_INCREMENT,
  `TITULO` varchar(255) NOT NULL,
  `PRECO` decimal(10,2) DEFAULT NULL,
  `IMAGEM` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID_PRODUTO`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (2,'Produto testando ',220.90,'https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg'),(4,'Pulseira de prata',509.95,'https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg'),(5,'Anel de brilhante ',2.00,'https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg'),(6,'SSD Sandisk 240gb',199.90,'https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg'),(7,'Monitor Acer',6900.00,'https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg'),(8,'Brinco',169.00,'https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg'),(9,'Blush',54.00,'https://oceane.vtexassets.com/arquivos/ids/202627/AP2000916CR80F_blush_cintilante_glossy_blush_oceane_edition_1.jpg?v=638330622680270000'),(14,'Iphone 14 PRO MAX',5000.00,'https://www.iplace.com.br/ccstore/v1/images/?source=/file/v4467257797733810589/products/222282.01.638479044523980203-apple-iphone-14-pro-max-1tb-prateado-mqc33be.jpg&height=350&width=350&quality=1.0'),(15,'Capacete',34.00,'https://th.bing.com/th/id/R.53380264b33550e7d1ac4501b63b05fd?rik=VuylBnN5a1qjOw&pid=ImgRaw&r=0'),(18,'Creme Facial Dior Prestige Le Micro-Caviar de Rose 75ml',3549.00,'https://www.sephora.com.br/dw/image/v2/BFJC_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/pt_BR/dw1fbe2310/images/hi-res-BR/P0_3348901450263_1500px.jpg?sw=1200&sh=1200&sm=fit'),(19,'Jogo',2.00,'https://th.bing.com/th/id/OIP.8rLYyg96YgpGnOUuCIs4JgHaE0?w=240&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'),(21,'tenis',120.00,'https://th.bing.com/th?q=Tenis+All-Star+Preto&w=120&h=120&c=1&rs=1&qlt=90&cb=1&dpr=1.3&pid=InlineBlock&mkt=pt-BR&cc=BR&setlang=pt-br&adlt=strict&t=1&mw=247'),(25,'prata 925',50.00,'https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg'),(27,'celular do alexandre',12.00,'https://carrefourbr.vtexassets.com/arquivos/ids/141430595-1280-auto?v=638488918264230000&width=1280&height=auto&aspect=true'),(41,'Iphone 15 Pro Max',8999.00,'https://a-static.mlcdn.com.br/1500x1500/apple-iphone-15-pro-max-256gb-titanio-natural-67-48mp-ios-5g/magazineluiza/237922600/82b62d765f251a646ed8f83d4fa25ede.jpg'),(42,'pool party',23400.00,'https://th.bing.com/th/id/OIP.arNXXRq1hKMGMAQXxJqXAQHaIr?w=171&h=201&c=7&r=0&o=5&dpr=1.3&pid=1.7'),(43,'Tênis',69.00,'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTh3vt6Bk_bu-pPgdAdFQWqZ1_ULb_aWw2xFFa6Rhmpd2_NEh5idsA2y5zKmrB-SgLjCJpm2d-RxgPxrh1LUtV5LtY2VXRQdOdK-Dr6d4vF0gTp-TB7ur0G&usqp=CAE'),(44,'tetete',2222.00,''),(45,'',NULL,''),(46,'',NULL,''),(47,'',NULL,''),(48,'sdds',23.00,'swswsw'),(49,'',NULL,''),(50,'',NULL,''),(51,'',NULL,''),(52,'',NULL,''),(53,'',NULL,''),(54,'',NULL,''),(55,'buda',45.00,''),(56,'',NULL,'');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `nome_usuario` varchar(15) DEFAULT NULL,
  `senha` varchar(10) DEFAULT NULL,
  `tipo_usuario` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Douglas','Douglas','1234','vendedor'),(3,'Gerente admin','admin','123','gerente');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_produto` int NOT NULL,
  `id_usuario` int DEFAULT NULL,
  `data_venda` date DEFAULT NULL,
  PRIMARY KEY (`id_venda`,`id_cliente`,`id_produto`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_produto` (`id_produto`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `vendas_ibfk_2` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`ID_PRODUTO`),
  CONSTRAINT `vendas_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES (2,7,5,3,'2024-05-13'),(3,7,27,3,'2024-05-14'),(4,7,6,3,'2024-05-14'),(5,7,8,3,'2024-05-14'),(8,7,18,3,'2024-05-14'),(9,7,7,3,'2024-05-14'),(13,6,14,3,'2024-05-14'),(23,8,15,3,'2024-05-14'),(24,8,8,3,'2024-05-14'),(25,13,14,3,'2024-05-14'),(27,7,7,3,'2024-05-15'),(28,7,25,3,'2024-05-15'),(35,7,5,3,'2024-05-20'),(36,7,7,3,'2024-05-21'),(37,13,9,3,'2024-05-27'),(38,8,19,3,'2024-05-27'),(39,7,7,3,NULL),(40,13,27,3,'2024-05-27'),(41,13,15,3,'2024-05-27'),(42,6,27,3,'2024-05-27'),(43,9,27,3,'2024-05-27'),(44,15,19,3,'2024-05-27');
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-29 15:44:56
