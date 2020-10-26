/*
* The create statements that build out the rule portion of
the SQL database

* AUTHOR: MIDN 1/C Polmatier
*/

CREATE TABLE Rules (
  ruleID        int NOT NULL AUTO_INCREMENT,
  adminID       int NOT NULL,
  rule          varchar(255) NOT NULL,
  title         varchar(255) NOT NULL,
  description   varchar(400),
  PRIMARY KEY (ruleID),
  FOREIGN KEY (adminID) REFERENCES Admins(adminID)
);

CREATE TABLE Admins (
  adminID       int NOT NULL AUTO_INCREMENT,
  name          varchar(255) NOT NULL,
  PRIMARY KEY (adminID)
);
