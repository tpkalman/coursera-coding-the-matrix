# Please fill out this stencil and submit using the provided submission script.

from GF2 import one

def addn(v,w): return [v[i] + w[i] for i in range(len(v))]
def subn(v,w): return [v[i] - w[i] for i in range(len(v))]
def scalar_vector_mult(alpha, v): return [alpha*x for x in v]

## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = addn(p1_v, p1_u) #[...]
p1_v_minus_u = subn(p1_v, p1_u) #[...]
p1_three_v_minus_two_u = subn([3*x for x in p1_v], [2*x for x in p1_u]) #[...]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = addn(p2_v, p2_u)
p2_v_minus_u = subn(p2_v, p2_u)
p2_two_v_minus_u = subn(scalar_vector_mult(2,p2_v), p2_u)
p2_v_plus_two_u = addn(p2_v, scalar_vector_mult(2, p2_u))



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_v = [0, one, one]
p3_u = [one, one, one]
p3_vector_sum_1 = [p3_v[0] + p3_u[0],p3_v[1] + p3_u[1],p3_v[2] + p3_u[2]]
p3_vector_sum_2 = [p3_v[0] + p3_u[0] + p3_u[0],p3_v[1] + p3_u[1] + p3_u[1],p3_v[2] + p3_u[2] + p3_u[2]]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

#a = 1100000 
#b = 0110000 
#c = 0011000 
#d = 0001100
#e = 0000110
#f = 0000011
#    0100010

u_0010010 = {'c','d','e'}
u_0100010 = {'b', 'c', 'd', 'e'}



## Problem 5
# Use the same format as the previous problem

#a = 1110000 
#b = 0111000 
#c = 0011100 
#d = 0001110
#e = 0000111
#f = 0000011
#    0010010

v_0010010 = {'c', 'd'}
v_0100010 = {'b','c','d'}



## Problem 6
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1



## Problem 7
# use 'one' instead of '1'
x_gf2 = [0,one,one,one]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

