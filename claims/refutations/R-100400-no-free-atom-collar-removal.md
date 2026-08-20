# R-100400 — No shifted square removes both activation atoms and collar

Claim ID: `R-100400`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-20

In `L-100400`, the activation-atom coefficient is `(1+c)^2`, while the
collar interval is `(X,lambda_c X]`, with

\[
\lambda_c={(3-c)^2\over9}.
\]

Thus

\[
\text{atoms vanish}\iff c=-1,
\qquad
\text{collar vanishes}\iff\lambda_c=1\iff c=0
\]

on `-1<=c<=0`.  The two conditions are incompatible.

At `c=-1`, `lambda_c=16/9`.  Taking `X=2`, the collar contains only `n=3`.
Since `beta(3)=mu(3)=-1`,

\[
\boxed{
P_{-1}(2)
=-{1\over\sqrt3}
\left(4\sqrt{2/3}-3\right)^2<0.
}
\]

Therefore the atom-free endpoint does not give a positive collar for free.
At `c=0`, the collar is empty, but the full signed future atomic tail remains.
Any quadratic-envelope proof must control one complete atom-plus-collar ledger;
it may not discard either piece.
