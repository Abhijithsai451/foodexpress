CREATE TABLE `Delivery`(
  `de_id` int,
  `de_street` varchar(50),
  `de_city` char(50),
  `de_state` char(25),
  `de_zipcode` varchar(6),
  `emp_id` int,
  `or_id` int,
  PRIMARY KEY (`de_id`),
  KEY `FK` (`emp_id`, `or_id`)
);

CREATE TABLE `User_Taste_Form`(
  `user_int_id` int,
  `int_cuisine` char(50),
  `int_dish_desc` char(50),
  `int_veg_desc` char(50),
  `int_fruits_desc` char(50),
  `int_flavours_desc` char(50),
  `ch_id` int,
  `user_id` int,
  PRIMARY KEY (`user_int_id`),
  KEY `FK` (`ch_id`, `user_id`)
);

CREATE TABLE `Order`(
  `or_id` int,
  `or_date` date,
  `or_time` timestamp,
  `or_cost` float,
  `user_id` int,
  PRIMARY KEY (`or_id`),
  KEY `FK` (`user_id`)
);

CREATE TABLE `Payment`(
  `p_id` int,
  `name` char(50),
  `card_number` int,
  `card_expiry_date` int,
  `card_cvv` int,
  `user_id` int,
  `or_id` int,
  PRIMARY KEY (`p_id`),
  KEY `FK` (`user_id`, `or_id`)
);

CREATE TABLE `Menu`(
  `menu_id` integer,
  `item_name` char(50),
  `item_id` int,
  `item_qty` int,
  `item_price` int,
  `ch_id` int,
  PRIMARY KEY (`menu_id`),
  KEY `FK` (`ch_id`)
);

CREATE TABLE `Employee`(
  `emp_id` int,
  `emp_first_name` varchar(50),
  `emp_last_name` varchar(50),
  `emp_type` varchar(10),
  `emp_phone` varchar(10),
  `emp_email` varchar(50),
  PRIMARY KEY (`emp_id`)
);

CREATE TABLE `Chef`(
  `ch_id` int,
  `ch_first_name` varchar(50),
  `ch_last_name` varchar(50),
  `ch_qualification` varchar(50),
  `ch_expertise` char(10),
  `ch_email` varchar(50),
  `exp_rep_id` int,
  PRIMARY KEY (`ch_id`),
  KEY `FK` (`exp_rep_id`)
);

CREATE TABLE `Expert_User_Report`(
  `exp_rep_id` int,
  `req_vitamins` char(25),
  `req_calories` char(5),
  `avoidable_items` char(50),
  `fat_intake` int,
  `suggested_items` char(50),
  `req_sugar_levels` int,
  `health_experts_id` int,
  PRIMARY KEY (`exp_rep_id`),
  KEY `FK` (`health_experts_id`)
);

CREATE TABLE `User_Health_Report`(
  `status_id` int,
  `user_bp_level` decimal(3,2),
  `user_sugar_level` decimal(3,2),
  `user_height` decimal(3,2),
  `user_weight` decimal(3,2),
  `user_haemoglobin_level` decimal(3,2),
  `user_allergic_items` varchar(50),
  `user_cholesterol_level` decimal(3,2),
  `user_body_mass_index` decimal(3,2),
  `user_id` int,
  PRIMARY KEY (`status_id`),
  KEY `FK` (`user_id`)
);

CREATE TABLE `Health_Expert`(
  `health_expert_id` int,
  `he_first_name` varchar(50),
  `he_last_name` varchar(50),
  `age` int,
  `he_join_date` date,
  `he_type` varchar(20),
  `he_phone` varchar(10),
  `he_email` varchar(50),
  PRIMARY KEY (`health_expert_id`)
);

CREATE TABLE `User`(
  `user_id` int,
  `email_addr` varchar(50),
  `first_name` varchar(50),
  `last_name` varchar(50),
  `age` int,
  `user_street_name` varchar(50),
  `user_city` varchar(50),
  `user_state` varchar(50),
  `user_zipcode` varchar(6),
  `username` varchar(50),
  `user_phone` varchar(10),
  PRIMARY KEY (`user_id`)
);