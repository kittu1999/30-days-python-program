create database json_file
CREATE TABLE person (
    name char(20),
    place char(50),
    phone no int(20)
    email_id varchar(50)
    married boolean()
    gender char(10),
);
SELECT * 
FROM OPENROWSET (BULK 'C:\Users\diwak\Desktop\python\task12', SINGLE_CLOB) as import
