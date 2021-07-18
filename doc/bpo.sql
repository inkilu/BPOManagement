/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.26 : Database - bpo_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bpo_management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bpo_management`;

/*Table structure for table `client_call_updates` */

DROP TABLE IF EXISTS `client_call_updates`;

CREATE TABLE `client_call_updates` (
  `update_id` int(11) NOT NULL AUTO_INCREMENT,
  `call_id` int(11) DEFAULT NULL,
  `update_description` varchar(100) DEFAULT NULL,
  `updated_by` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`update_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `client_call_updates` */

insert  into `client_call_updates`(`update_id`,`call_id`,`update_description`,`updated_by`) values (1,1,'Chettayi','2021-04-07');

/*Table structure for table `client_calls` */

DROP TABLE IF EXISTS `client_calls`;

CREATE TABLE `client_calls` (
  `call_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `call_type` varchar(30) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `call_status` varchar(30) DEFAULT NULL,
  `date_time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`call_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `client_calls` */

insert  into `client_calls`(`call_id`,`client_id`,`staff_id`,`call_type`,`description`,`call_status`,`date_time`) values (1,1,2,'Service','sdfghjkl','Responsed','2021-04-07 01:54:47');

/*Table structure for table `client_services` */

DROP TABLE IF EXISTS `client_services`;

CREATE TABLE `client_services` (
  `client_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) DEFAULT NULL,
  `services_id` int(11) DEFAULT NULL,
  `started_date` varchar(30) DEFAULT NULL,
  `current_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`client_service_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `client_services` */

insert  into `client_services`(`client_service_id`,`client_id`,`services_id`,`started_date`,`current_status`) values (1,1,1,'2021-04-01','pending'),(2,1,1,'2021-04-20','pending');

/*Table structure for table `clients` */

DROP TABLE IF EXISTS `clients`;

CREATE TABLE `clients` (
  `client_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `house_name` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `pincode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `clients` */

insert  into `clients`(`client_id`,`company_id`,`first_name`,`last_name`,`phone`,`email`,`house_name`,`place`,`pincode`) values (1,1,'Ammu','Kutty','2345678900','g@g.g','Nira Nivas','Palakkad','123456'),(2,0,'f','l','23456789','@.','hname','pl','234567');

/*Table structure for table `companies` */

DROP TABLE IF EXISTS `companies`;

CREATE TABLE `companies` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `company_name` varchar(30) DEFAULT NULL,
  `mode_of_work` varchar(30) DEFAULT NULL,
  `description` varchar(60) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `companies` */

insert  into `companies`(`company_id`,`login_id`,`company_name`,`mode_of_work`,`description`,`phone`,`email`,`website`) values (1,10,'Riss ','qswdfghj','Gastro Medicine','7012758728','anntreataregina@gmail.com','asdfghjkl'),(3,12,'Riss  jjjjjjjjjjj','qswdfghj','Beauty Medicine','1234567890','anntreata@gmail.com','asdfghjkl');

/*Table structure for table `company_services` */

DROP TABLE IF EXISTS `company_services`;

CREATE TABLE `company_services` (
  `services_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `service_title` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `charge_for_service` varchar(60) DEFAULT NULL,
  `service_duration` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`services_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `company_services` */

insert  into `company_services`(`services_id`,`company_id`,`service_title`,`description`,`charge_for_service`,`service_duration`) values (1,1,'Heist h','rfgvbhn m','100','5');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'ss','ss','staff'),(3,'anu','anu','user'),(4,'asds@f.mmmmm','0987654321','technical'),(6,'annregina@gmail.com','1234567890','c_care'),(10,'anntreataregina@gmail.com','7012758728','company'),(12,'anntreata@gmail.com','1234567890','company');

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `message` varchar(400) DEFAULT NULL,
  `reply` varchar(300) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

insert  into `notifications`(`notification_id`,`staff_id`,`message`,`reply`,`date`) values (1,4,'fghjk','pending','123456789'),(2,2,'fghj1','ok','2021-04-03 00:44:14'),(3,2,'fghjkl','pending','2021-04-04 21:01:06'),(4,2,'dfghjkl','nothing','2021-04-04 21:09:02'),(5,4,'sdfghjkl','hai','2021-04-07'),(6,2,'efrghjk','pending','2021-04-07');

/*Table structure for table `staffs` */

DROP TABLE IF EXISTS `staffs`;

CREATE TABLE `staffs` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `staffs` */

insert  into `staffs`(`staff_id`,`login_id`,`company_id`,`first_name`,`last_name`,`phone`,`email`,`photo`,`gender`,`age`) values (1,0,0,'Aswathy','Achu','0','0','0','0','0'),(2,4,1,'Staff','One','0987654321','asds@f.mmmmm','static/3be2db03-6b1f-4550-b746-bc16e24cbceb5.png','female','19'),(4,6,1,'Staff','Two','1234567891','annregina@gmail.com','static/c0286e6b-bfe5-47f9-aff0-4be274e3732aAlternative.gif','female','19');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
