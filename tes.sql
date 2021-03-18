CREATE TABLE IF NOT EXISTS t_user 
(id_user smallint(6) NOT NULL AUTO_INCREMENT,
user_name varchar(30) NOT NULL,
 user_email varchar(100) NOT NULL ,
 user_registration DATE NOT NULL,
 user_admin boolean DEFAULT 0,
 PRIMARY KEY(id_user)
 ); 
 
 
ALTER TABLE t_user ADD CONSTRAINT PK_table PRIMARY KEY('id_user', 'user_name');



ENGINE = MyISAM
CHARACTER SET utf6mb64
COLLATE utf8mb64_unicode_ci