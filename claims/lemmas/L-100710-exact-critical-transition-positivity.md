# L-100710 — The correctly weighted one-prime transition is positive at every critical Bernstein order

Claim ID: `L-100710`  
Status: **PROVED EXACT ALL-ORDER LOCAL TRANSITION THEOREM**  
Created: 2026-08-21  
Supersedes the normalization discussion in: `L-100704`  
Depends on: the sharp scaling inequality of `L-100000`  
RH status: **not assumed**

Fix an integer `m>=2`. At the final critical Bernstein step put

\[
\kappa_m(t):=\kappa_{m,m-1}(t)>0
\]

and

\[
w_{m,X}(n)
:=n^{-(m+1)/2}
\kappa_m\!\left(\sqrt{n/X}\right).
\tag{L-100710.1}
\]

For a prime label `p`, write

\[
r=p^{-1/2},
\qquad
R_p=rU_p-r^2U_{p^2}
=rU_p(I-rU_p).
\tag{L-100710.2}
\]

The literal contribution of the distinguished transition at a base source
integer `n` is

\[
\boxed{
(R_pw_{m,X})(n)
=r\,w_{m,X}(np)-r^2w_{m,X}(np^2).
}
\tag{L-100710.3}

No coefficient may be dropped from this expression.

## 1. Sharp ratio bound

The critical kernel satisfies

\[
t\longmapsto\frac{\kappa_m(t)}{t^{m-1}}
\quad\text{nonincreasing}.
\]

Therefore, with `s=sqrt(np/X)`,

\[
\frac{\kappa_m(\sqrt p\,s)}{\kappa_m(s)}
\le p^{(m-1)/2}.
\]

Applying this to the two consecutive source states gives

\[
\begin{aligned}
\frac{w_{m,X}(np^2)}{w_{m,X}(np)}
&=
p^{-(m+1)/2}
\frac{\kappa_m(p\sqrt{n/X})}
     {\kappa_m(\sqrt p\sqrt{n/X})}\\
&\le p^{-(m+1)/2}p^{(m-1)/2}
=rac1p.
\end{aligned}
\tag{L-100710.4}

This is the correctly normalized inequality. The stronger comparison
`w(np)>w(np^2)` is sufficient but is not the coefficient-exact statement of
the homotopy transition.

## 2. Strict transition positivity

Substitution of (L-100710.4) into (L-100710.3) yields

\[
\begin{aligned}
(R_pw_{m,X})(n)
&\ge r\,w_{m,X}(np)
\left(1-r\,p^{-1}\right)\\
&=
 p^{-1/2}w_{m,X}(np)
\left(1-p^{-3/2}\right)>0.
\end{aligned}
\tag{L-100710.5
}
\]

Hence

\[
\boxed{
R_pw_{m,X}(n)>0
\qquad(n,X>0,\ p\text{ prime},\ m\ge2).
}
\tag{L-100710.6}

The result includes inactive and active regimes uniformly because the scaling
inequality is global.

## 3. Scope firewall

This is a theorem about the **distinguished local transition before completion
by the other primes**. It does not imply

\[
R_p\prod_{q\ne p}H_{q,t}w_{m,X}\ge0.
\]

The retained exact rough-prime fixture on this branch shows that the latter
pointwise implication is false. Completion can reverse the local sign.

Thus the surviving task is genuinely cross-prime: estimate the balanced sum of
completed transitions while retaining their carrier and activation-collar
cancellation. The local coefficient arithmetic is now fully closed.