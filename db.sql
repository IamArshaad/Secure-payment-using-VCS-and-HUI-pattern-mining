/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - qr_payment
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`qr_payment` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `qr_payment`;

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `accid` int(11) NOT NULL AUTO_INCREMENT,
  `accountno` varchar(200) DEFAULT NULL,
  `cvv` varchar(200) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  PRIMARY KEY (`accid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`accid`,`accountno`,`cvv`,`balance`) values 
(1,'1','1',999995);

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `om_id` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `total_amount` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bill` */

insert  into `bill`(`b_id`,`om_id`,`date`,`time`,`total_amount`) values 
(1,1,'2023-02-09',NULL,1000);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`c_id`,`c_name`) values 
(1,'Beauty Products'),
(2,'Fashion'),
(3,'Bags'),
(4,'Stationary'),
(5,'Grocery');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_description` varchar(200) DEFAULT NULL,
  `c_date` varchar(50) DEFAULT NULL,
  `c_time` varchar(15) DEFAULT NULL,
  `c_reply` varchar(50) DEFAULT NULL,
  `v_lid` int(11) DEFAULT NULL,
  `c_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`comp_id`,`c_description`,`c_date`,`c_time`,`c_reply`,`v_lid`,`c_status`) values 
(1,'aaaaaaaaaaaaaa','2023-02-15','04:45:00','okk',2,'Replied'),
(2,'','0000-00-00','00:00:00','',0,''),
(3,'','2023-02-13','16:04:56','pending',0,'pending'),
(4,'ghgg','2023-02-13','16:09:57','pending',0,'pending'),
(5,'ghgg','2023-02-13','16:09:58','pending',0,'pending'),
(6,'ghgg','2023-02-13','16:09:59','pending',0,'pending'),
(7,'ghgg','2023-02-13','16:10:00','pending',0,'pending'),
(8,'ghgg','2023-02-13','16:10:00','pending',0,'pending'),
(9,'ghgg','2023-02-13','16:10:01','pending',0,'pending'),
(10,'ghj','2023-02-13','16:12:21','pending',0,'pending'),
(11,'cbc','2023-02-13','16:12:30','pending',0,'pending'),
(12,'gggmm','2023-02-13','16:20:03','pending',0,'pending'),
(13,'hgahak','2023-02-13','16:41:38','pending',0,'pending'),
(14,'iytyy','2023-02-13','16:45:06','pending',3,'pending'),
(15,'neww','2023-02-22','16:06:37','pending',3,'pending'),
(16,'hhhh','2023-02-22','16:34:18','pending',3,'pending'),
(17,'gg','2023-03-01','14:45:47','pending',3,'pending');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_description` varchar(50) DEFAULT NULL,
  `f_date` date DEFAULT NULL,
  `f_time` time DEFAULT NULL,
  `u_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`f_id`,`f_description`,`f_date`,`f_time`,`u_lid`) values 
(1,'hihihi','2023-02-02','01:05:00',3),
(2,'sdsdsds','2023-02-09','10:45:00',4),
(3,'vvvv','2023-02-13','00:00:00',3),
(4,'vvvv','2023-02-13','00:00:00',3),
(5,'vvvv','2023-02-13','16:49:14',3),
(6,'gggdh','2023-02-13','16:51:09',3);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'vendor','vendor','vendor'),
(3,'user@gmail.com','123','user'),
(4,'','',''),
(5,'hhhhh','1234','vendor'),
(6,'arshad@gmail.com','Arshad','vendor'),
(7,'ars@gmail.com','Arshad','vendor'),
(8,'jack@gmail','zzzzzzzzzzzzz','vendor'),
(9,'aaaa@gmail.com','Arshad','user'),
(10,'ashid@gmail.com','12345','user');

/*Table structure for table `order_main` */

DROP TABLE IF EXISTS `order_main`;

CREATE TABLE `order_main` (
  `om_id` int(11) NOT NULL AUTO_INCREMENT,
  `v_lid` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `u_lid` int(11) DEFAULT NULL,
  `total_amount` int(11) DEFAULT NULL,
  `status` varchar(15) DEFAULT 'pending',
  PRIMARY KEY (`om_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `order_main` */

insert  into `order_main`(`om_id`,`v_lid`,`date`,`time`,`u_lid`,`total_amount`,`status`) values 
(1,6,'2023-03-22','15:39:54',10,4099,'Done'),
(2,6,'2023-03-22','15:40:18',10,6329,'pending'),
(3,6,'2023-03-27','12:07:20',3,2200,'pending'),
(4,6,'2023-03-27','13:02:19',3,2200,'pending'),
(5,6,'2023-03-27','13:09:06',3,2200,'pending'),
(6,6,'2023-03-27','15:58:18',3,900,'pending'),
(7,6,'2023-03-27','16:12:42',3,900,'pending'),
(8,6,'2023-03-27','16:14:23',3,900,'pending'),
(9,6,'2023-03-27','16:18:45',3,315,'pending'),
(10,6,'2023-03-31','14:47:44',NULL,NULL,'pending'),
(11,6,'2023-04-03','11:55:59',3,11960,'pending'),
(12,6,'2023-04-03','14:41:00',3,2000,'pending'),
(13,6,'2023-04-03','15:04:49',3,2000,'pending'),
(14,6,'2023-04-03','16:35:26',3,90,'pending'),
(15,6,'2023-04-03','16:50:21',3,7164,'pending'),
(16,6,'2023-04-03','17:08:18',3,4776,'pending'),
(17,6,'2023-04-03','17:18:42',3,45,'pending'),
(18,6,'2023-04-03','17:24:24',3,8955,'pending'),
(19,6,'2023-04-03','17:26:25',NULL,NULL,'pending'),
(20,6,'2023-04-03','17:28:42',3,540,'Done'),
(21,6,'2023-04-03','18:17:10',NULL,NULL,'pending'),
(22,6,'2023-04-03','18:17:38',3,35880,'Done'),
(23,6,'2023-04-03','18:20:43',3,349,'Done'),
(24,6,'2023-04-03','18:22:07',3,50,'pending'),
(25,6,'2023-04-03','18:27:34',3,4196,'Done'),
(26,6,'2023-04-03','18:31:40',3,698,'Done');

/*Table structure for table `order_sub` */

DROP TABLE IF EXISTS `order_sub`;

CREATE TABLE `order_sub` (
  `os_id` int(11) NOT NULL AUTO_INCREMENT,
  `om_id` int(11) DEFAULT NULL,
  `p_id` int(11) DEFAULT NULL,
  `quantity` int(20) DEFAULT NULL,
  PRIMARY KEY (`os_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

/*Data for the table `order_sub` */

insert  into `order_sub`(`os_id`,`om_id`,`p_id`,`quantity`) values 
(1,1,8,2),
(2,1,2,1),
(3,1,10,1),
(4,2,3,2),
(5,2,4,1),
(6,3,7,1),
(7,4,7,1),
(8,5,7,1),
(9,6,1,20),
(10,7,1,20),
(11,8,1,20),
(12,9,1,7),
(13,11,3,4),
(14,12,11,1),
(15,13,11,1),
(16,14,1,1),
(17,14,1,1),
(18,15,2,12),
(19,15,2,12),
(20,15,2,12),
(21,16,2,12),
(22,16,2,12),
(23,17,1,1),
(24,18,2,45),
(25,20,1,12),
(26,22,3,12),
(27,23,4,1),
(28,24,15,5),
(29,25,9,4),
(30,25,7,1),
(31,26,4,2);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `p_name` varchar(50) DEFAULT NULL,
  `p_price` int(11) DEFAULT NULL,
  `v_lid` int(11) DEFAULT NULL,
  `profit` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`p_id`,`c_id`,`p_name`,`p_price`,`v_lid`,`profit`) values 
(1,1,'Soap',45,6,'1'),
(2,1,'Face Wash',199,6,'2'),
(3,1,'Lipstick',2990,6,'3'),
(4,1,'Moisturizer',349,6,'2'),
(5,2,'Shirts',1999,6,'1'),
(7,2,'Jeans',2200,6,'5'),
(8,2,'Kurtas',1200,6,'6'),
(9,2,'Hat',499,6,'4'),
(10,3,'American Tourister',1500,6,'6'),
(11,3,'Skybag',2000,6,'5'),
(12,3,'Wildcraft',1300,6,'1'),
(13,3,'Puma',4500,6,'2'),
(14,4,'Pen',10,6,'2'),
(15,4,'Pencil',10,6,'2'),
(16,4,'Notebooks',40,6,'2'),
(17,4,'Eraser',5,6,'2'),
(18,4,'File',20,6,'2'),
(19,5,'Rice',32,6,'2'),
(20,5,'Biriyani Rice',75,6,'2'),
(21,5,'Atta',50,6,'2'),
(22,5,'Tea',200,6,'2'),
(23,5,'Sugar',45,6,'2'),
(24,5,'Masala Powder',25,6,'1');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`s_id`,`p_id`,`quantity`) values 
(1,0,0),
(3,1,4),
(4,4,15);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_lid` int(11) DEFAULT NULL,
  `u_name` varchar(50) DEFAULT NULL,
  `u_place` varchar(50) DEFAULT NULL,
  `u_post` varchar(50) DEFAULT NULL,
  `u_pin` bigint(20) DEFAULT NULL,
  `u_district` varchar(50) DEFAULT NULL,
  `u_state` varchar(50) DEFAULT NULL,
  `u_email` varchar(50) DEFAULT NULL,
  `u_phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`u_id`,`u_lid`,`u_name`,`u_place`,`u_post`,`u_pin`,`u_district`,`u_state`,`u_email`,`u_phone`) values 
(1,3,'aaa','hg','hg',9898,'hg','gg','user@gmail.com',8484845858),
(2,NULL,'','','',0,'','','',0),
(3,4,'','','',0,'','','',0),
(4,0,'','','',0,'','','',0),
(5,9,'aaaa','aaaa','aaaa',78787,'aaaa','aaaa','aaaa@gmail.com',6474858),
(6,10,'Ashid T','Chelannur','Kannankara',673616,'Kozhikode','Kerala','ashid@gmail.com',8137007696);

/*Table structure for table `vendors` */

DROP TABLE IF EXISTS `vendors`;

CREATE TABLE `vendors` (
  `v_id` int(11) NOT NULL AUTO_INCREMENT,
  `v_lid` int(11) DEFAULT NULL,
  `v_name` varchar(50) DEFAULT NULL,
  `v_place` varchar(50) DEFAULT NULL,
  `v_post` varchar(50) DEFAULT NULL,
  `v_pin` bigint(20) DEFAULT NULL,
  `v_district` varchar(50) DEFAULT NULL,
  `v_state` varchar(50) DEFAULT NULL,
  `v_ownername` varchar(50) DEFAULT NULL,
  `v_email` varchar(50) DEFAULT NULL,
  `v_phone` bigint(20) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`v_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `vendors` */

insert  into `vendors`(`v_id`,`v_lid`,`v_name`,`v_place`,`v_post`,`v_pin`,`v_district`,`v_state`,`v_ownername`,`v_email`,`v_phone`,`status`) values 
(1,2,'Arjun','Malappuram','Pmna',673639,'MLP','Kerala','Arjun','Arjun@gmail.com',8593862660,'Approved'),
(2,3,'ss','sss','sss',0,'sssss','ssss','ssss','sss',0,'Rejected'),
(3,0,'','','',0,'','','','',0,''),
(4,5,'aaa','adss','xxxxc',77,'sss','cdmc','jjjcvnc','hhhhh',78855555,'pending'),
(5,6,'Arshad','Calicut','Calicut',673639,'Calicut','Kerala','Arshad','arshad@gmail.com',8593862660,'pending'),
(6,7,'Arshad Mk','Malapp','Mall',673639,'malp','Kerala','Arshad','ars@gmail.com',7306103133,'Approved'),
(7,8,'Jack','Pmna','Pmna',673639,'pmna','kerala','ssssssss','jack@gmail',85968626323232,'pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
