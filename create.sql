CREATE DATABASE POPSTACK;

USE POPSTACK;

CREATE TABLE users {
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username varchar(60) NOT NULL,
    password varchar(120) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
}
    
CREATE TABLE threads {
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    creator INT NOT NULL,
    subject varchar(60) NOT NULL,
    imgId INT NOT NULL AUTO_INCREMENT,
    imgName varchar(60),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message text,
    FOREIGN KEY(creator) REFERENCES users(id)
}

CREATE TABLE replies {
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    creator INT NOT NULL,
    threadId INT NOT NULL,
    imgId INT,
    imgName varchar(60),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(creator) REFERENCES users(id),
    FOREIGN KEY(threadId) REFERENCES threads(id)
}
