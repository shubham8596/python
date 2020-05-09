
create database restapi;

use restapi;

CREATE TABLE IF NOT EXISTS user(
    id                  INT         PRIMARY KEY,
    name          	VARCHAR(25)    NOT NULL,
    age	                INT         NOT NULL,
    department   	VARCHAR(25)    NOT NULL,
    subject		VARCHAR(25)    NOT NULL
);
