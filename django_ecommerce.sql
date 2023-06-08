-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 08, 2023 at 12:37 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_ecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add feedback', 8, 'add_feedback'),
(30, 'Can change feedback', 8, 'change_feedback'),
(31, 'Can delete feedback', 8, 'delete_feedback'),
(32, 'Can view feedback', 8, 'view_feedback'),
(33, 'Can add order', 9, 'add_order'),
(34, 'Can change order', 9, 'change_order'),
(35, 'Can delete order', 9, 'delete_order'),
(36, 'Can view order', 9, 'view_order'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add products', 11, 'add_products'),
(42, 'Can change products', 11, 'change_products'),
(43, 'Can delete products', 11, 'delete_products'),
(44, 'Can view products', 11, 'view_products'),
(45, 'Can add my cart', 12, 'add_mycart'),
(46, 'Can change my cart', 12, 'change_mycart'),
(47, 'Can delete my cart', 12, 'delete_mycart'),
(48, 'Can view my cart', 12, 'view_mycart');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$gyZyK8T5Z10ErRBij3JAXa$03x3MreHuSYE8oLJWOSvnlU80dkcaMegOKrCqqB1TM0=', '2023-06-05 12:36:14.464707', 1, 'ompatel', '', '', 'ompatel@gmail.com', 1, 1, '2023-05-30 05:58:29.886955');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-06-05 12:36:56.075871', '1', 'Sports', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-06-05 12:37:16.691099', '2', 'Clothes', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-06-05 12:38:19.068291', '1', 'Basketball', 1, '[{\"added\": {}}]', 11, 1),
(4, '2023-06-05 12:39:03.998904', '2', 'Football', 1, '[{\"added\": {}}]', 11, 1),
(5, '2023-06-05 12:39:27.131967', '3', 'T-shirt', 1, '[{\"added\": {}}]', 11, 1),
(6, '2023-06-05 12:39:56.100621', '4', 'Shirt', 1, '[{\"added\": {}}]', 11, 1),
(7, '2023-06-05 19:28:03.762088', '2', 'User object (2)', 3, '', 10, 1),
(8, '2023-06-06 18:00:21.276406', '4', 'Shirt', 3, '', 11, 1),
(9, '2023-06-06 18:00:21.370159', '3', 'T-shirt', 3, '', 11, 1),
(10, '2023-06-06 18:00:21.428003', '2', 'Football', 3, '', 11, 1),
(11, '2023-06-06 18:00:21.590566', '1', 'Basketball', 3, '', 11, 1),
(12, '2023-06-06 18:00:37.803605', '2', 'Clothes', 3, '', 7, 1),
(13, '2023-06-06 18:00:37.836517', '1', 'Sports', 3, '', 7, 1),
(14, '2023-06-06 18:04:08.209529', '3', 'Fridge', 1, '[{\"added\": {}}]', 7, 1),
(15, '2023-06-06 18:06:38.337512', '4', 'TV', 1, '[{\"added\": {}}]', 7, 1),
(16, '2023-06-06 18:08:23.451211', '5', 'Laptop', 1, '[{\"added\": {}}]', 7, 1),
(17, '2023-06-06 18:13:44.384439', '5', 'Asus TUF F15 Gaming Laptop', 1, '[{\"added\": {}}]', 11, 1),
(18, '2023-06-06 18:20:36.611064', '6', 'Samsung Neo QLED TV', 1, '[{\"added\": {}}]', 11, 1),
(19, '2023-06-06 18:24:40.157591', '7', 'Samsung Double Door Fridge', 1, '[{\"added\": {}}]', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'category'),
(8, 'myapp', 'feedback'),
(12, 'myapp', 'mycart'),
(9, 'myapp', 'order'),
(11, 'myapp', 'products'),
(10, 'myapp', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-30 05:54:58.231838'),
(2, 'auth', '0001_initial', '2023-05-30 05:55:10.464914'),
(3, 'admin', '0001_initial', '2023-05-30 05:55:12.783497'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-05-30 05:55:12.844459'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-30 05:55:12.891005'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-05-30 05:55:13.686032'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-05-30 05:55:14.787773'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-05-30 05:55:14.942384'),
(9, 'auth', '0004_alter_user_username_opts', '2023-05-30 05:55:14.998055'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-05-30 05:55:15.875062'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-05-30 05:55:15.944968'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-05-30 05:55:16.020618'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-05-30 05:55:16.407539'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-05-30 05:55:16.614559'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-05-30 05:55:16.837195'),
(16, 'auth', '0011_update_proxy_permissions', '2023-05-30 05:55:16.907786'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-05-30 05:55:17.184943'),
(18, 'myapp', '0001_initial', '2023-05-30 05:55:19.622386'),
(19, 'sessions', '0001_initial', '2023-05-30 05:55:20.270451'),
(20, 'myapp', '0002_mycart', '2023-06-05 17:52:50.093640'),
(21, 'myapp', '0003_delete_mycart', '2023-06-05 17:55:39.648163'),
(22, 'myapp', '0004_mycart', '2023-06-05 17:55:57.228480'),
(23, 'myapp', '0005_alter_mycart_is_bought', '2023-06-05 18:18:20.394684'),
(24, 'myapp', '0006_delete_mycart', '2023-06-05 18:22:20.380076'),
(25, 'myapp', '0007_mycart', '2023-06-05 18:23:09.887643'),
(26, 'myapp', '0008_alter_user_phone', '2023-06-06 11:32:55.036926'),
(27, 'myapp', '0009_delete_feedback', '2023-06-06 17:31:27.659899'),
(28, 'myapp', '0010_feedback', '2023-06-06 17:32:01.025056'),
(29, 'myapp', '0011_mycart_orderid_products_vendorid', '2023-06-08 10:36:16.608380');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5g5u5psmyp3ggfstu5wsyu4dg0i5o6t3', '.eJyFj70OgjAUhd-lsyG1FEqdjImDAzHxBchte_lRaAmUAY3vbpuwMLl-3zkn937I3Y_XAbqenIgbRvDYM0YFo5Sdm8gT7QZyIBUsvq2WGaeqMyF73DMF-oU2CvME27jQsn7qVBIjyWbnpHQG-8uW3Q20MLehLY1SmRQ5Gi651rk2lCECZxlLacEoFAUFmae11koUtRSAwgSaC84zZXgYHWEd0K4l-tbFgx7wdlOAQfkJ7Azad87eogoI__7-_QGD419s:1q7Bwf:0m7cr5RbLKWCWBhUYRZc_pUImNqFQfkVhStRvxNm1nk', '2023-06-22 09:28:41.111928');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_category`
--

CREATE TABLE `myapp_category` (
  `id` bigint(20) NOT NULL,
  `categoryname` varchar(200) NOT NULL,
  `img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_category`
--

INSERT INTO `myapp_category` (`id`, `categoryname`, `img`) VALUES
(3, 'Fridge', 'category/FridgeCategory.jpg'),
(4, 'TV', 'category/TVcategory.jpg'),
(5, 'Laptop', 'category/Laptopcategory.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_feedback`
--

CREATE TABLE `myapp_feedback` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phonenumber` int(11) NOT NULL,
  `message` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_feedback`
--

INSERT INTO `myapp_feedback` (`id`, `name`, `email`, `phonenumber`, `message`) VALUES
(1, 'Om Patel', '', 2147483647, 'Hello');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_mycart`
--

CREATE TABLE `myapp_mycart` (
  `id` bigint(20) NOT NULL,
  `userId` varchar(200) NOT NULL,
  `productid` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `img` varchar(100) NOT NULL,
  `price` varchar(200) NOT NULL,
  `quantity` varchar(200) NOT NULL,
  `totalprice` varchar(200) NOT NULL,
  `is_bought` tinyint(1) NOT NULL,
  `orderId` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_mycart`
--

INSERT INTO `myapp_mycart` (`id`, `userId`, `productid`, `name`, `img`, `price`, `quantity`, `totalprice`, `is_bought`, `orderId`) VALUES
(3, '1', '7', 'Samsung Double Door Fridge', 'products/fridge1.jpg', '2', '1', '2', 0, '0'),
(4, '1', '6', 'Samsung Neo QLED TV', 'products/TV1.jpeg', '2', '1', '2', 0, '0');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_order`
--

CREATE TABLE `myapp_order` (
  `orderDate` datetime(6) NOT NULL,
  `id` bigint(20) NOT NULL,
  `productid` varchar(200) NOT NULL,
  `productqty` varchar(200) NOT NULL,
  `userId` varchar(200) NOT NULL,
  `userName` varchar(200) NOT NULL,
  `userEmail` varchar(200) NOT NULL,
  `userContact` int(11) NOT NULL,
  `address` varchar(300) NOT NULL,
  `orderAmount` int(11) NOT NULL,
  `paymentMethod` varchar(200) NOT NULL,
  `transactionId` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_order`
--

INSERT INTO `myapp_order` (`orderDate`, `id`, `productid`, `productqty`, `userId`, `userName`, `userEmail`, `userContact`, `address`, `orderAmount`, `paymentMethod`, `transactionId`) VALUES
('2023-06-07 06:38:11.622992', 2, '7', '1', '1', 'Om1230', 'ompatel22072002@gmail.com', 1230, 'jamnagar', 2, 'Razorpay', 'pay_LywZFZpRF9vE8i'),
('2023-06-07 06:39:46.829300', 3, '7', '1', '1', 'Om1230', 'ompatel22072002@gmail.com', 1230, 'jamnagar', 2, 'Razorpay', 'pay_LywavkCpEi0ajn');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_products`
--

CREATE TABLE `myapp_products` (
  `productid` bigint(20) NOT NULL,
  `productname` varchar(200) NOT NULL,
  `productimg` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `productdescription` longtext NOT NULL,
  `quantity` int(11) NOT NULL,
  `productcategory_id` bigint(20) NOT NULL,
  `vendorid` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_products`
--

INSERT INTO `myapp_products` (`productid`, `productname`, `productimg`, `price`, `productdescription`, `quantity`, `productcategory_id`, `vendorid`) VALUES
(5, 'Asus TUF F15 Gaming Laptop', 'products/Laptop1.jpg', 2, '11th Gen Intel Core i7 processor\r\n16 GB GDDR4 Ram\r\nNvidia RTX 2070 graphics card(8GB GDDR6 Memory)\r\nUHD 144Hz LED Display', 40, 5, ''),
(6, 'Samsung Neo QLED TV', 'products/TV1.jpeg', 2, '72 inch Display with 120Hz refresh rate at 8K resolution', 30, 4, ''),
(7, 'Samsung Double Door Fridge', 'products/fridge1.jpg', 2, 'Glossy Black Double Door fridge\r\nWi-Fi enabled with on door display', 47, 3, '');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_user`
--

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(200) NOT NULL,
  `phone` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myapp_user`
--

INSERT INTO `myapp_user` (`id`, `name`, `email`, `password`, `phone`) VALUES
(1, 'Om1230', 'ompatel22072002@gmail.com', 'om1', 1230),
(3, 'Account1', 'acc@acc.com', 'acc123', 2147483647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_category`
--
ALTER TABLE `myapp_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_feedback`
--
ALTER TABLE `myapp_feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_mycart`
--
ALTER TABLE `myapp_mycart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_order`
--
ALTER TABLE `myapp_order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_products`
--
ALTER TABLE `myapp_products`
  ADD PRIMARY KEY (`productid`),
  ADD KEY `myapp_products_productcategory_id_f8aadc31_fk_myapp_category_id` (`productcategory_id`);

--
-- Indexes for table `myapp_user`
--
ALTER TABLE `myapp_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `myapp_category`
--
ALTER TABLE `myapp_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `myapp_feedback`
--
ALTER TABLE `myapp_feedback`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_mycart`
--
ALTER TABLE `myapp_mycart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `myapp_order`
--
ALTER TABLE `myapp_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `myapp_products`
--
ALTER TABLE `myapp_products`
  MODIFY `productid` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `myapp_user`
--
ALTER TABLE `myapp_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_products`
--
ALTER TABLE `myapp_products`
  ADD CONSTRAINT `myapp_products_productcategory_id_f8aadc31_fk_myapp_category_id` FOREIGN KEY (`productcategory_id`) REFERENCES `myapp_category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
