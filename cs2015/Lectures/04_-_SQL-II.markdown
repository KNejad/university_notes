# 04 - SQL-II
Created Friday 23 September 2016

Aggregate functions compute summarization (or aggregation) of data

Aggregate functions:
--------------------
SUM
AVG
MIN
MAX
COUNT


Count(*):
---------
Counts the number of rows in a table


Group By:
---------
Aggregate functions help us to summarise the whole column(s) of data into one row.
Sometimes we want to group data before applying aggregate functions
This gives us ‘subtotals’ rather than ‘overall total’
GROUP BY is used to achieve that
GROUP BY column_name;


Having:
-------
Like "where" clause
"where" clause introduces a condition on individual rows; having clause introduces a condition on aggregations


Combining Results:
------------------
Union: Combine rows from both queries
Intersect: Keep only rows in common of both queries
Except: Only keep rows from first query which are not in the second query

