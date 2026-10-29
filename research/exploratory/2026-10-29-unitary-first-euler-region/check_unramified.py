#!/usr/bin/env python3
"""Check the quotient-free unramified correction algebra exactly."""
import sympy as s

V,W,D,R,Q = s.symbols('V W D R Q', nonzero=True)
P = (1/(1-V) + W/(1-W)
     + (R*((1-1/Q)/(1-V)+W)-D*(1+(Q-1)*W*V/(1-V)))/(1-R))
H = (1-V)*(1-W)*P/(1-D)
num = (-D*R*Q + D*V*W**2*Q**2 - D*V*W**2*Q - D*V*W*Q**2
       + D*V*Q + D*W*Q + R*V*W**2*Q - R*W**2*Q + R*W
       + R*Q - R - V*W*Q)
assert s.cancel(Q*(D-1)*(R-1)*(H-1)-num)==0
assert not s.denom(s.cancel(H)).has(W)
print('Hu unramified H−1 identity verified; the apparent 1−W pole cancels')
