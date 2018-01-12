-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generato il: Gen 12, 2018 alle 16:45
-- Versione del server: 5.5.58-0ubuntu0.14.04.1
-- Versione PHP: 5.5.9-1ubuntu4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `journal_1`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `clinton_en`
--

CREATE TABLE IF NOT EXISTS `clinton_en` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Tweet` varchar(142) DEFAULT NULL,
  `Stance` varchar(7) DEFAULT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Training',
  `POS` text,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=985 ;

-- --------------------------------------------------------

--
-- Struttura della tabella `dictionary`
--

CREATE TABLE IF NOT EXISTS `dictionary` (
  `word` varchar(150) CHARACTER SET utf8mb4 NOT NULL,
  `language` varchar(4) CHARACTER SET utf8mb4 NOT NULL,
  `frequency` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`word`,`language`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `dictionary_mentions`
--

CREATE TABLE IF NOT EXISTS `dictionary_mentions` (
  `id` bigint(20) NOT NULL,
  `screen_name` varchar(250) CHARACTER SET utf8mb4 NOT NULL,
  `name` varchar(250) CHARACTER SET utf8mb4 NOT NULL,
  `description` varchar(500) CHARACTER SET utf8mb4 NOT NULL,
  `place` varchar(250) CHARACTER SET utf8mb4 NOT NULL,
  `language` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_estonian_ci NOT NULL,
  `json` text CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `dictionary_shorturls`
--

CREATE TABLE IF NOT EXISTS `dictionary_shorturls` (
  `shorturl` varchar(250) NOT NULL,
  `url` varchar(300) NOT NULL,
  `content` text NOT NULL,
  `language` varchar(20) NOT NULL,
  PRIMARY KEY (`shorturl`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `dictionary_tovote`
--

CREATE TABLE IF NOT EXISTS `dictionary_tovote` (
  `word` varchar(150) CHARACTER SET utf8mb4 NOT NULL,
  `language` varchar(4) CHARACTER SET utf8mb4 NOT NULL,
  `frequency` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`word`,`language`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `indipendencia_ca`
--

CREATE TABLE IF NOT EXISTS `indipendencia_ca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Tweet` varchar(500) NOT NULL,
  `Stance` varchar(40) NOT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Training',
  `POS` text NOT NULL,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=5401 ;

-- --------------------------------------------------------

--
-- Struttura della tabella `indipendencia_es`
--

CREATE TABLE IF NOT EXISTS `indipendencia_es` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Tweet` varchar(500) NOT NULL,
  `Stance` varchar(40) NOT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Training',
  `POS` text NOT NULL,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=5401 ;

-- --------------------------------------------------------

--
-- Struttura della tabella `lepen_fr`
--

CREATE TABLE IF NOT EXISTS `lepen_fr` (
  `id` bigint(18) NOT NULL DEFAULT '0',
  `Tweet` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Stance` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Set` varchar(50) NOT NULL DEFAULT 'Training',
  `screen_name` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  `date` varchar(19) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `POS` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Tweet` (`Tweet`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `lepen_fr_row`
--

CREATE TABLE IF NOT EXISTS `lepen_fr_row` (
  `_unit_id` int(10) DEFAULT NULL,
  `_golden` varchar(5) CHARACTER SET utf8 DEFAULT NULL,
  `_unit_state` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `_trusted_judgments` int(1) DEFAULT NULL,
  `_last_judgment_at` varchar(18) CHARACTER SET utf8 DEFAULT NULL,
  `stance` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `date` varchar(19) CHARACTER SET utf8 DEFAULT NULL,
  `id` bigint(18) NOT NULL DEFAULT '0',
  `screen_name` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `text` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `macron_fr`
--

CREATE TABLE IF NOT EXISTS `macron_fr` (
  `id` bigint(18) NOT NULL DEFAULT '0',
  `Tweet` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Stance` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Test',
  `screen_name` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  `date` varchar(19) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `POS` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Tweet` (`Tweet`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `macron_fr_row`
--

CREATE TABLE IF NOT EXISTS `macron_fr_row` (
  `_unit_id` int(10) DEFAULT NULL,
  `_golden` varchar(5) CHARACTER SET utf8 DEFAULT NULL,
  `_unit_state` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `_trusted_judgments` int(1) DEFAULT NULL,
  `_last_judgment_at` varchar(18) CHARACTER SET utf8 DEFAULT NULL,
  `stance` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `date` varchar(19) CHARACTER SET utf8 DEFAULT NULL,
  `id` bigint(18) NOT NULL DEFAULT '0',
  `screen_name` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `text` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `referendum_it`
--

CREATE TABLE IF NOT EXISTS `referendum_it` (
  `id` bigint(18) NOT NULL DEFAULT '0',
  `Tweet` varchar(150) DEFAULT NULL,
  `Stance` varchar(6) DEFAULT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Test',
  `screen_name` varchar(15) DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  `date` varchar(19) DEFAULT NULL,
  `POS` text NOT NULL,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Tweet` (`Tweet`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Struttura della tabella `referendum_it_row`
--

CREATE TABLE IF NOT EXISTS `referendum_it_row` (
  `_unit_id` int(10) DEFAULT NULL,
  `_golden` varchar(5) DEFAULT NULL,
  `_unit_state` varchar(9) DEFAULT NULL,
  `_trusted_judgments` int(1) DEFAULT NULL,
  `_last_judgment_at` varchar(18) DEFAULT NULL,
  `stance` varchar(23) DEFAULT NULL,
  `date` varchar(19) DEFAULT NULL,
  `id` bigint(18) NOT NULL DEFAULT '0',
  `screen_name` varchar(15) DEFAULT NULL,
  `text` varchar(150) DEFAULT NULL,
  `user_id` bigint(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Struttura della tabella `trump_en`
--

CREATE TABLE IF NOT EXISTS `trump_en` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Tweet` varchar(142) DEFAULT NULL,
  `Stance` varchar(7) DEFAULT NULL,
  `Set` varchar(10) NOT NULL DEFAULT 'Test',
  `POS` text NOT NULL,
  `POSplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `textplus` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1957 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
