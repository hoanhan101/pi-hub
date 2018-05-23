CREATE TABLE `readings` (
  `sensor_id` int(11) NOT NULL,
  `location` int(11) NOT NULL,
  `temp` double(11,5) NOT NULL,
  `temp_degree` char(1) NOT NULL,
  `humidity` double(11,5) NOT NULL,
  `timestamp` datetime NOT NULL ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;
