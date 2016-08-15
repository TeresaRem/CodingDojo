-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema email
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema email
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `email` DEFAULT CHARACTER SET latin1 ;
USE `email` ;

-- -----------------------------------------------------
-- Table `email`.`email`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `email`.`email` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
