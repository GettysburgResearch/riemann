# L-100711 — Correct source-atom transition positivity and the surviving harmonic future cost

Claim ID: `L-100711`  
Status: **PROVED EXACT LOCAL THEOREM + CRITICAL SCALING FIREWALL**  
Created: 2026-08-21  
Supersedes: withdrawn `L-100710`  
Depends on: the sharp scaling inequality of `L-100000`  
RH status: **not assumed**

Fix `m>=2`. Put

\[
\kappa_m(t)=\kappa_{m,m-1}(t)>0
\]

and use full source-atom coordinates

\[
\boxed{
w_{m,X}(n)
=n^{-(m+1)/2}
\kappa_m\!\left(\sqrt{n/X}\right).
}
\tag{L-100711.1}

In these coordinates, the endpoint-kernel operator

\[
R_p=p^{-1/2}U_p-p^{-1}U_{p^2}
\]

becomes the atom difference

\[
\boxed{
(\mathscr R_pw)(n)=w(np)-w(np^2).
}
\tag{L-100711.2}

The Euler activities are already contained in the two atom weights.

## 1. Strict local positivity

The critical kernel satisfies

\[
t\longmapsto\frac{\kappa_m(t)}{t^{m-1}}
\quad\text{nonincreasing}.
\]

Consequently

\[
\begin{aligned}
\frac{w(np^2)}{w(np)}
&=p^{-(m+1)/2}
\frac{\kappa_m(p\sqrt{n/X})}
     {\kappa_m(\sqrt p\sqrt{n/X})}\\
&\le p^{-(m+1)/2}p^{(m-1)/2}
=\frac1p.
\end{aligned}
\tag{L-100711.3}

Hence

\[
\boxed{
(\mathscr R_pw)(n)
\ge(1-p^{-1})w(np)>0.
}
\tag{L-100711.4}

This is the correct coefficient-exact local transition theorem.

## 2. The transition kernel retains the critical future exponent

Define, with `s=sqrt(n/X)`,

\[
G_{p,m}(s)
=p^{-(m+1)/2}\kappa_m(\sqrt p\,s)
-p^{-(m+1)}\kappa_m(ps),
\tag{L-100711.5}
\]

so that

\[
(\mathscr R_pw)(n)=n^{-(m+1)/2}G_{p,m}(s).
\]

Let

\[
F_m(s)=\frac{\kappa_m(s)}{s^{m-1}}.
\]

For `s<=1`, `F_m(s)=m-s`. For `s>=1`,

\[
F_m(s)=m-s+s(1-s^{-1})^m.
\tag{L-100711.6}

Its derivative is

\[
F_m'(s)
=-1+(1-s^{-1})^{m-1}
\left(1+\frac{m-1}{s}\right)\le0,
\]

and `-F_m'` is nonincreasing. Direct substitution gives

\[
\frac{G_{p,m}(s)}{s^{m-1}}
=p^{-1}F_m(\sqrt p\,s)-p^{-2}F_m(ps).
\tag{L-100711.7}

Differentiating and using monotonicity of `-F_m'` shows that the right side is
nonincreasing. Therefore, for every fresh prime label `q`,

\[
\boxed{
\frac{(\mathscr R_pw)(nq)}{(\mathscr R_pw)(n)}
\le\frac1q.
}
\tag{L-100711.8}

The bound is sharp in the deep critical regime.

## 3. Exact firewall

Equation (L-100711.8) proves that the distinguished transition remains in the
**prime-harmonic** owner class. It does not gain a `q^(-3/2)` future budget.
Thus

\[
\sum_q\frac1q=\infty
\]

still blocks source-blind adjacent-level completion.

This explains simultaneously why:

```text
the local transition is strictly positive;
completion by other primes can reverse its pointwise sign;
the retained finite counterexample is compatible with the local theorem;
the balanced cross-prime estimate remains RH-bearing.
```

The local arithmetic is closed; the missing cancellation is entirely in the
future-prime completion.