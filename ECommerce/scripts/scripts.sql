CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `categories` varchar(255) NOT NULL,
  `appliances` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `mrp` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `discount` varchar(255) NOT NULL,
  `quantity` varchar(255) NOT NULL,
  `warranty` varchar(255) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `product_features` (
  `product_id` int NOT NULL,
  `powersource` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `modelname` varchar(255) DEFAULT NULL,
  `specialfeature` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `product_images` (
  `product_id` int NOT NULL,
  `main_image` varchar(255) DEFAULT NULL,
  `front_image` varchar(255) DEFAULT NULL,
  `left_image` varchar(255) DEFAULT NULL,
  `right_image` varchar(255) DEFAULT NULL,
  `back_image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO `sakila`.`product`
(`product_id`,
`categories`,
`appliances`,
`color`,
`description`,
`mrp`,
`price`,
`discount`,
`quantity`,
`warranty`)
VALUES
(1,
'Home & Kitchen',
'Air Conditioner',
'Red',
'LG 1.5 Ton 5 Star AI DUAL Inverter Split AC (Copper, Super Convertible 6-in-1 Cooling, HD Filter with Anti-Virus Protection, 2022 Model, PS-Q19YNZE, White)',
'19090',
'1782',
'15%',
'1',
'10');


INSERT INTO `sakila`.`product_features`
(`product_id`,
`powersource`,
`brand`,
`modelname`,
`specialfeature`,
`description`)
VALUES
(1,
'coded electric',
'LG',
'PS-Q19YNZE',
'CoolingInverter compressor, Convertible, High Density Filter',
'testing');

INSERT INTO `sakila`.`product_images`
(`product_id`,
`main_image`,
`front_image`,
`left_image`,
`right_image`,
`back_image`)
VALUES
(1,
'E://mainimage.png',
'E://frontimage.png',
'E://leftimage.png',
'E://rightimage.png',
'E://backimage.png');


