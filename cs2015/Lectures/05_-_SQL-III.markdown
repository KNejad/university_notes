# 05 - SQL-III
Created Tuesday 27 September 2016

Table Aliases:
--------------
Help reduce amount of typing
FROM Viewing V Then you can replace Viewing with V


Joins:
------


### Natural Join:
FROM Viewing NATURAL JOIN PropertyForRent
Joins tables together with there primary and foreign keys


### Cross Joins:
Cartesian Product: a join with no WHERE clause
FROM Left CROSS JOIN Right;
Useful for: query optimisation, data mining
	

#### Returns:
Left.left-row-1 - Right.right-row-1
Left.left-row-1 - Right.right-row-2
Left.left-row-1 - Right.right-row-3
.....
Left.left-row-2 - Right.right-row-1
Left.left-row-2- Right.right-row-2
Left.left-row-2 - Right.right-row-3
......
	

### Theta Joins:
WHERE L.LeftCol Θ R.Rightcol;
Θ is one of:  =  ! = <> < > <= >= 
	

### Outer Joins:
A join that may include unmatched rows
	


### Equai Join:
A special case of theta join (= predicate)


### Semi Join:
Theta join that outputs from just one table


### Self Join:
joining a table to itself


### Cross Join:
Cartesian products (no predicates)

