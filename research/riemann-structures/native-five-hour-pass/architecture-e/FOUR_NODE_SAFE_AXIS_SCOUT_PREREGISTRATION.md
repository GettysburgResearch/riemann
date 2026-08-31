# Preregistration: unresolved four-node safe-axis chamber scout

Declared before the first Architecture E safe-axis reconnaissance. This is a
bounded numerical scout, not a theorem and not a finite PSD certificate for
the continuum.

Evaluate the actual completed function through

    xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    F(x)=d/dx log xi(1/2+x).

At x=1/2 use the removable exact formula
'1+EulerGamma/2-log(4*pi)/2'; do not evaluate an infinity-minus-infinity
expression. All other nodes use the literal logarithmic derivative including
the zeta, gamma and rational completion terms.

Primary exact rational grid:

    1/2,9/16,3/4,1,3/2,2,3,4,6,8,12,16,24,32,48,64.

Inspect every four-element subset (1820 packets). Add confluent probes
'c+(0,1,2,3)2^-k' for c in {1/2,1,2,4,8,16,32} and k in {8,16,24,32}, and
two-pair probes '(c,c+2^-k,d,d+2^-k)' for c<d in
{1/2,1,2,4,8,16,32,64}, k in {12,24,32}, where all nodes stay at most64.
Deduplicate exact rational packets before evaluation.

For each packet form

    H_ij=(F(x_i)+F(x_j))/(x_i+x_j), C_ij=1/(x_i+x_j)

and compute the smallest generalized eigenvalue of '(H,C)' by Cholesky
congruence at 100 decimal digits. Retain every packet, eigenvalue, matrix,
condition estimate and precision. Recompute the 24 smallest values at 200
digits and require agreement to 60 significant decimal places; otherwise
return 'PRECISION_UNRESOLVED'. Also retain the E4 high controls
(256,257,300,1024) and full confluence at256.

Fixed outcomes:

- 'NEGATIVE_SCOUT': a recomputed value is strictly below -10^-50;
- 'POSITIVE_ON_REGISTERED_GRID': all recomputed values exceed 10^-50;
- 'PRECISION_UNRESOLVED': neither guarded conclusion is justified.

None is a proof about an uncountable chamber. Do not adapt the grid, delete a
bad packet, infer a continuum minimum, or call a near-zero value a zero.
Preregistered worker cap200MiB, wall cap120s, artifact cap8MiB. Use one
standard-library/mpmath process only; no zero census or external data.

