# L-93283 - Rows two and three have no common Mellin cancellation in the open strip

Claim ID: `L-93283`  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: the fixed-row transform `L-96000` from PR #542  
RH status: **not assumed**

For the component-row transform of PR #542, write

\[
P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
-C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-93283.1}
\]

For `j=2,3`, direct simplification gives

\[
\boxed{P_2(z)=2\,2^{-z}-1-3^{-z},}
\tag{L-93283.2}
\]

and

\[
\boxed{3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.}
\tag{L-93283.3}
\]

Suppose `P_2(z)=P_3(z)=0`, and put

\[
x=2^{-z},\qquad y=3^{-z}.
\]

The first equation gives `y=2x-1`. Substitution into the second gives

\[
0=5(2x-1)-x-1-3x^2=-3(x-1)(x-2).
\tag{L-93283.4}
\]

Hence either `(x,y)=(1,1)` or `(x,y)=(2,3)`.

If `2^{-z}=3^{-z}=1`, moduli give `Re z=0`. The phase equations would make
`log 2/log 3` rational unless `Im z=0`; unique factorization excludes that.
Thus `z=0`.

If `2^{-z}=2` and `3^{-z}=3`, moduli give `Re z=-1`, and the same phase
argument gives `Im z=0`. Thus `z=-1`.

Therefore

\[
\boxed{
P_2(z)=P_3(z)=0
\quad\Longrightarrow\quad z\in\{0,-1\}.
}
\tag{L-93283.5}
\]

In particular, the two numerators have no common zero in

\[
0<\Re z<1.
\tag{L-93283.6}
\]

Every hypothetical off-line zeta zero is retained by at least one of the two
fixed rows. This replaces the ineffective phrase "all sufficiently large rows"
by one explicit two-row consumer.
