-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2020 at 11:22 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db1`
--
CREATE DATABASE IF NOT EXISTS `db1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db1`;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `ID` int(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `department` varchar(30) NOT NULL,
  `company` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(50) NOT NULL,
  `color` varchar(20) NOT NULL,
  `units` varchar(5) NOT NULL,
  `price` varchar(8) NOT NULL,
  `image` varchar(50) NOT NULL,
  `nul` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`ID`, `code`, `department`, `company`, `name`, `description`, `color`, `units`, `price`, `image`, `nul`) VALUES
(36, 'AR2041', 'Watches', 'Emporio Armani', 'AR2041', 'Wrist watch', 'Black', '34', '241', 'ar2041.jpg', ''),
(37, 'RDJ31', 'Watches', 'Rolex', 'DateJust 31', 'Luxury wrist watch', 'Purple', '2', '12554', 'Datejust_31.jpg', ''),
(38, 'IWP371605', 'Watches', 'IWC ', 'Portugieser 371', 'Luxury wrist watch', 'White', '12', '2215', 'IW371605_portugieser.jpeg', ''),
(39, 'IWPSW37771', 'Watches', 'IWC', 'Pilot S Watch', 'Luxury wrist watch', 'Black', '2', '3265', 'iwc-pilot-s-watch-chronograph-iw377710-1.jpg', ''),
(40, 'LOSD6921', 'Watches', 'Longines', 'Skin Diver 6921', 'Luxury wrist watch', 'None', '34', '1296', 'longines+skin+diver+reference+6921.jfif', ''),
(41, 'TIXX34533', 'Watches', 'Tissot', 'Ti watch', '', 'Blue', '45', '466', 'afd44289eb3e70c50ae8b14c88015af7.jpg', ''),
(42, 'LO29094783', 'Watches', 'Longines', 'Premium', '', 'White', '12', '908', 'L29094783.jpg', ''),
(43, 'SKPR047487', 'Watches', 'Seiko', 'Presage', 'Luxury wrist watch', 'Blue', '67', '368', 'SRPB41.jpg', '');

-- --------------------------------------------------------

--
-- Table structure for table `t1`
--

CREATE TABLE `t1` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `lname` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
