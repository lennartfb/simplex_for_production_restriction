# simplex_for_production_restriction
An algorithm for solving an optimizations problem or a productions restriction with more than one restriction

The method simplex takes an input of the db function to be optimized and the nb functions which are the additional conditions for our problem. The db function is a list of the factors of our contribution margin function wich will be maximized. The nb variable is a List of lists wich each contain the factors of the restrictions.
Example:
DB Function = 20x+30y --> MAX
NB Function1 ->3x+2y = 1800
NB Function2 ->2x+4y = 1600
NB Function3 ->0x+1y = 300

In code it would look like:
db = [20,30]
nb = [[3,2,1800],[2,4,1600],[0,1,300]]
