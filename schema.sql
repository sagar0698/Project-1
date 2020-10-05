--$ sqlite3 data.db .dump > schema.sql


PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;


DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS FOLLOW;
DROP TABLE IF EXISTS TWEETS;


/* Create a table called USERS */
CREATE TABLE USERS(
    PK_USERNAME VARCHAR PRIMARY KEY, 
    EMAIL VARCHAR NOT NULL, 
    PASSWORD VARCHAR NOT NULL
);


/* Create few records in this table */
INSERT INTO USERS VALUES('a', 'a@a.com', 'a');
INSERT INTO USERS VALUES('b', 'b@b.com', 'b');
INSERT INTO USERS VALUES('c', 'c@c.com', 'c');
INSERT INTO USERS VALUES('d', 'd@d.com', 'd');
INSERT INTO USERS VALUES('e', 'e@e.com', 'e');
INSERT INTO USERS VALUES('f', 'f@f.com', 'f');


/* Create a table called FOLLOW */
CREATE TABLE FOLLOW(
    FOLLOWERS VARCHAR NOT NULL , 
    FK_USER VARCHAR NOT NULL,
    FOREIGN KEY(FK_USER) REFERENCES USERS(PK_USERNAME)
);


/* Create few records in this table */
INSERT INTO FOLLOW VALUES('b', 'a');
INSERT INTO FOLLOW VALUES('c', 'a');
INSERT INTO FOLLOW VALUES('d','a');
INSERT INTO FOLLOW VALUES('a','b');
INSERT INTO FOLLOW VALUES('a','b');
INSERT INTO FOLLOW VALUES('a','c');
INSERT INTO FOLLOW VALUES('e','d');
INSERT INTO FOLLOW VALUES('f','d');


/* Create a table called TWEETS */
CREATE TABLE TWEETS(
    TWEET TEXT NOT NULL, 
    DAY_OF VARCHAR NOT NULL,
    FK_USER VARCHAR NOT NULL,
    FOREIGN KEY(FK_USER) REFERENCES USERS(PK_USERNAME)
);


INSERT INTO TWEETS VALUES('hello all','today', 'a');
INSERT INTO TWEETS VALUES('goodbye all','today', 'a');
INSERT INTO TWEETS VALUES('b is cool','today', 'b');
INSERT INTO TWEETS VALUES('b is wack','today', 'c');
INSERT INTO TWEETS VALUES('c is cool','today', 'c');
INSERT INTO TWEETS VALUES('hello a','today', 'd');
INSERT INTO TWEETS VALUES('d is best','today', 'd');
INSERT INTO TWEETS VALUES('microblogging service similar to twitter','today', 'e');
INSERT INTO TWEETS VALUES('making them api','today', 'e');
INSERT INTO TWEETS VALUES('who following me','today', 'e');
INSERT INTO TWEETS VALUES('what','today', 'f');


COMMIT;
