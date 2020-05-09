
create database if not exists restapi;

use restapi;

drop table if exists user;

CREATE TABLE IF NOT EXISTS user(id INT PRIMARY KEY,name VARCHAR(25) NOT NULL,age INT NOT NULL,department VARCHAR(25) NOT NULL,subject VARCHAR(25) NOT NULL);

insert into user values(1,"shubham",24, "PUSCD", "dos");
insert into user values(2,"pratik", 25, "Physics", "phy");
insert into user values(3,"sagar", 26, "Math", "algebra");
