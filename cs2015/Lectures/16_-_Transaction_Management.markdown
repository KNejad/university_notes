# 16 - Transaction Management
Created Friday 4 November 2016


The "ACID" Requirements For a Transaction:
------------------------------------------
Atomicity: Each unit of work is indivisible
Consistency: A transaction transforms the database from one consistent state into another (intermediates may be inconsistent)
Isolation: Each transaction effectively executes independently - one transaction should not see the inconsistent/incomplete state of another transaction
Durability: Once a transaction is complete, its effects cannot be undone or lost (it can only be “undone” with a compensating transaction)


The Lost Update Problem:
------------------------
If 2 queries get run at the same time conflicts may arise.


### Serialising Transactios:
By serialising transactions then no conflicts can arise since no queries are running at the same time
	

### Locks:
Locks may be used to serialise only the required transactions that may cause conflicts
	

### Deadlocks:
If 2 queries are running concurrently and they both need item a and b. Q1 gets a Q2 gets b (they lock the files) then both are waiting for the other and you get a deadlock.
	

