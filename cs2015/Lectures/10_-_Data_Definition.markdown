# 10 - Data Definition
Created Thu Dec 1 2016

IEF: Integrity Enhancement Features

Domains:
--------
Domains are data types (VARCHAR FLOAT TIME etc)
	

### User Defined Domains:
Domains can be created by the user with the CREATE DOMAIN command


#### Example:
CREATE DOMAIN SexType AS CHAR(1)
DEFAULT 'M'
CHECK (VALUE IN ('M', 'F'));


Scalar Functions:
-----------------
Scalar functions convert/manipulate data values (ie. SUBTEXT)


Referential Integrity:
----------------------
If a foreign key is non-null, it must match an existing row in the parent table.
SQL will reject operations that would violate referential integrity
	

Constraints:
------------
Constraints prevent tables from having certain characteristics (ie A member of staff may manage no more than 100 properties) 
	

Example:
--------
CREATE ASSERTION StaffNotOverLoaded
CHECK (NOT EXISTS
(SELECT StaffNo FROM PropertyForRent
GROUP BY StaffNo HAVING COUNT (*) > 100));
CREATE TABLE PropertyForRent ( ...
CONSTRAINT StaffNotOverLoaded); 


Triggers:
---------
Triggers are ways of the database doing something if something happens.


Schemas:
--------
A schema is a collection of named DBMS objects (ie Tables, Domains, Views etc)
	

