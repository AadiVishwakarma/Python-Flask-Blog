-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jan 17, 2021 at 06:17 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nutcrack`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `Sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phoneNum` varchar(15) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`Sno`, `name`, `email`, `phoneNum`, `msg`, `date`) VALUES
(1, 'First Post', 'firstpost@gmail.com', '123456789', 'First Post', '2020-11-12 20:09:03'),
(2, 'dkpnc sdknavndk nw nn s ', 'aditya20041999@gmail.com', '9716279036', 'hey everyone', '0000-00-00 00:00:00'),
(3, 'dkpnc sdknavndk nw nn s ', 'aditya20041999@gmail.com', '9716279036', 'hey everyone', '0000-00-00 00:00:00'),
(16, 'Aditya', 'aditya20041999@gmail.com', '1234567890', 'chal ja', '2020-11-12 23:15:30'),
(17, 'End', 'aditya20041999@gmail.com', '1234567890', 'bbbb lect 12', '2020-11-13 20:54:14'),
(18, 'End', 'aditya20041999@gmail.com', '1234567890', 'bbbb lect 12', '2020-11-13 20:55:44'),
(19, 'End', 'aditya20041999@gmail.com', '1234567890', 'bbbb lect 12', '2020-11-13 21:00:14'),
(20, 'End', 'aditya20041999@gmail.com', '1234567890', 'bbbb lect 12', '2020-11-13 21:06:37'),
(21, 'admin', 'aditya20041999@gmail.com', '1234567890', 'chal ja', '2020-11-13 22:13:55'),
(22, 'End', 'aditya20041999@gmail.com', '1234567890', 'jfguv', '2020-11-13 22:27:51'),
(23, 'Aditya', 'aditya20041999@gmail.com', '1234567890', 'bbbbjhiih', '2020-11-13 22:29:12'),
(24, 'Aditya', 'aadi.vishwakarma.engineer@gmail.com', '1234567890', 'bbbbjhiih', '2020-11-13 22:29:39'),
(25, 'Aditya', 'aadi.vishwakarma.engineer@gmail.com', '1234567890', 'plllz', '2020-11-13 22:30:37'),
(26, 'Aditya', 'adityavishwakarma013@gmail.com', '1234567890', 'hey', '2020-11-18 12:11:57'),
(27, 'Aditya', 'adityavishwakarma013@gmail.com', '1234567890', 'hey', '2020-11-18 12:12:21'),
(28, 'Aditya', 'aditya20041999@gmail.com', '1234567890', 'bk', '2020-11-18 12:13:50');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `Sno` int(12) NOT NULL,
  `postTitle` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(30) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`Sno`, `postTitle`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(4, 'fourth', 'post', '4', 'usual', '', '2020-12-06 20:48:01'),
(5, 'fifth', 'five', '5', 'really', '', '2020-12-06 20:48:18'),
(6, 'first', 'first post', '1', 'ply', '', '2020-12-06 20:52:28'),
(7, 'second', 'second post', '2', 'ibibi', '', '2020-12-06 21:02:19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`Sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`Sno`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `Sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `Sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
