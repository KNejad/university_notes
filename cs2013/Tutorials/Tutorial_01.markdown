# Tutorial 01
Created Thursday 22 September 2016

w, u and v are strings
T is an alphabet
A and B are languages

1)What is the value of | λ | ?
------------------------------

0

2) What can you say about λw and wλ ?
-------------------------------------

They are both the same

3) What is the relationship between |uv|, |u| and |v| ?
-------------------------------------------------------
|uv| = |u| + |v| 
|uv| is the sum of |u| and |v|

4) State a necessary and sufficient condition on T for T* to be finite. If T* is finite, list its members.
----------------------------------------------------------------------------------------------------------

T has to be an alphabet with 0 characters
T* = λ



5) Give an example to show that uv = vu is not always true. Give a non-trivial example to show it is not always false. (in this case trivial means an example using λ)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

u = lala v=vava => lalavava != vavalala

u = baba v= ba => bababa =  bababa

6) Give necessary and sufficient conditions on u and v for uv = vu.
-------------------------------------------------------------------

V and U must be a repetition of C where C is any string

7) List all the (i) prefixes, (ii) suffixes, and (iii) substrings of abb.
-------------------------------------------------------------------------

### i) prefixes
a
ab
abb
λ


### ii) suffixes
b
bb
abb
λ


### iii) sustring
a
ab
abb
b
bb
λ


8) If A = {a, ba} and B = {a, λ , bb}, list, in lexical order, the elements of (i) A+B and (ii) AB, and (iii) the first 12 strings in A * .
-------------------------------------------------------------------------------------------------------------------------------------------

### i) A+B
λ, a, a, ba, bb


### ii) AB
a,  aa, ba, abb, abb, baa, babb


### iii) The first 12 strings in A*
a, aa, ba, aaa, aba, baa, aaaa, aaba, abaa,  baaa, aaaaa


9) Which ordering scheme (dictionary or lexical) is most useful for infinite sets, and why? (give an example of the first 10 elements of some infinite language in both orderings, to illustrate the
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

advantage of one scheme)
------------------------
	
Lexical is more useful because there are infinite sets of "a"
λ, a,aa,aaa,aaaa,aaaaa,aaaaaa,aaaaaaa,aaaaaaaa,aaaaaaaaa
λ, a, b, aa, ab, ba, bb, aaa, aab, aba
	


10) Under what conditions are A * and A + equal?
------------------------------------------------
	
If λ is an element of A
	

11) If T has only two symbols, show that every string over T of length 4 or more must have two adjacent non-empty equal substrings. (hint: for starters you can write out all of the strings of length four and see if it is true for them)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

12) Let T be the alphabet {a,b,c}, and λ be the empty string.
-------------------------------------------------------------

### (i) Write down the first five elements of T* in lexical order and dictionary order.
Lexical: λ, a, aa, aaa, aaaa
Dictionary: λ, a , b, aa, ab


### (ii) Write down the first five elements of T + in lexical order and dictionary order.
Lexical: a, aa, aaa, aaaa, aaaaa
Dictionary: a , b, aa, ab, ba


13) If I have a machine with 1GB of memory, how many possible states can the machine be in?
-------------------------------------------------------------------------------------------

