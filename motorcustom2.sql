-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2023 at 06:38 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `motorcustom2`
--

-- --------------------------------------------------------

--
-- Table structure for table `akun`
--

CREATE TABLE `akun` (
  `id_akun` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  `role` enum('admin','user') NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun`
--

INSERT INTO `akun` (`id_akun`, `username`, `password`, `role`, `nama`, `alamat`) VALUES
(1, 'dikaadmin', 'dikaaja', 'admin', 'dika natakusumah', 'jalan galunggung no.16'),
(2, 'dikauser', 'dikaaja', 'user', 'dikta', 'jalan galunggung no.14'),
(3, 'dilan18', '-dilan16', 'user', 'Adilan Cahya Putra', 'Perum Pesona Intan Blok k3/no.22'),
(4, 'mila12', 'dikaaja', 'user', 'Syamila Putri Kencana', 'Perum Pesona Intan Blok B1/no.25'),
(5, 'dikta221', 'natakusumah18', 'user', 'Alan Frimansyah', 'Jalan Sukajadi NO.202'),
(6, 'alonza', 'alonza1808@', 'user', 'Alonza Nara', 'Jalan Kenangan no.21'),
(7, 'dikta111', 'n@takusumah18', 'user', 'Yakib Frimansyah', 'Jalan anggrek No.111'),
(8, 'flaq', 'asdkadkahdkh21@', 'user', 'astag', 'jln. cikoneng 202');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `id_item` int(11) NOT NULL,
  `jenis_motor` varchar(70) NOT NULL,
  `harga` int(11) NOT NULL,
  `deskripsi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`id_item`, `jenis_motor`, `harga`, `deskripsi`) VALUES
(1, 'Bratcafe V2 Reguler', 23000000, ''),
(2, 'Caferacer V2 Reguler', 20000000, 'Motor custom caferacer dengan desain yang minimalis dan elegan, memberikan pengalaman berkendara bergaya. '),
(3, 'Scrambler V3 Reguler', 25000000, 'Motor custom bergaya scrambler dengan desain yang tangguh dan petualangan.'),
(5, 'Bratcafe V1', 19000000, 'Motor Custom desain basic\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_akun` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `jumlah_pesanan` int(11) NOT NULL,
  `tanggal_pemesanan` date NOT NULL,
  `total_pembayaran` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_akun`, `id_item`, `jumlah_pesanan`, `tanggal_pemesanan`, `total_pembayaran`) VALUES
(1, 4, 2, 2, '2023-10-16', 40000000),
(3, 3, 2, 3, '2023-11-13', 60000000),
(4, 3, 3, 2, '2023-12-18', 50000000),
(6, 6, 5, 2, '2023-11-18', NULL),
(7, 7, 1, 1, '2023-12-20', NULL),
(8, 2, 2, 1, '2023-12-20', 20000000),
(9, 2, 3, 5, '2023-12-20', 125000000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`id_akun`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`id_item`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_akun` (`id_akun`),
  ADD KEY `id_item` (`id_item`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `akun`
--
ALTER TABLE `akun`
  MODIFY `id_akun` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `id_item` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_akun` FOREIGN KEY (`id_akun`) REFERENCES `akun` (`id_akun`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transaksi_item` FOREIGN KEY (`id_item`) REFERENCES `item` (`id_item`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
