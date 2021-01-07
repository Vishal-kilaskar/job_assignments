"""
You are choreographing a circus show with various animals. For one act,
you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
If it is possible, return YES, otherwise return NO.

"""

"""
solution to this problem is,
step 1) as we know "two kangaroos on a number line ready to jump in the positive direction(i.e toward positive infinity)"
        we should iterate towards infinite. 
        
step 2) as given in an example both kangaroo meet in "(x1+v1) == (x2+v2)" they met at position x=3 after (2+1) == (1+2).

step 3) we will add the x1 position with the distance v1 --- x1=x1+v1 
"""

"""
limit = 1000
position = 0
while(position < limit):
    if x1+v1 == x2+v2:
        return "yes"
    
    x1 += v1
    x2 += v2
return "No"

"""