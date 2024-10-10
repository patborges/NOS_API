CREATE TABLE `geoloc`.`cp_dist_conc` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `codigo_postal` VARCHAR(10) NOT NULL,
  `concelho` VARCHAR(45) NULL,
  `distrito` VARCHAR(45) NULL,
  UNIQUE INDEX `idcp_dist_conc_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `codigo_postal_UNIQUE` (`codigo_postal` ASC) VISIBLE,
  PRIMARY KEY (`id`));

