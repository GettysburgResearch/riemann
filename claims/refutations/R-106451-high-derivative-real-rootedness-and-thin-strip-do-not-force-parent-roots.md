# R-106451 — High derivative real-rootedness plus an arbitrarily thin strip does not force parent roots

Claim ID: `R-106451`  
Status: **PROVED EXACT COUNTERFAMILY**  
Created: 2026-08-25  
Depends on: elementary Chebyshev identities  
RH status: **not assumed**

Fix `c>1` and an even integer `n`.  Let

\[
p_n(x)=T_n(x)+c,
\]

where `T_n` is the Chebyshev polynomial.

## 1. The parent has no real zero

For `|x|<=1`,

\[
-1\le T_n(x)\le1,
\]

so `p_n(x)>=c-1>0`.  Because `n` is even,

\[
T_n(x)\ge1
\]

for `|x|>=1`.  Hence

\[
\boxed{N_\mathbb R(p_n)=0.}
\tag{R-106451.1
}

## 2. Every positive derivative is real-rooted

The zeros of `T_n` are simple and real.  Repeated Rolle therefore gives

\[
\boxed{
p_n^{(K)}=T_n^{(K)}
\text{ is real-rooted for every }1\le K<n.
}
\tag{R-106451.2
}

In particular the fourth derivative has the maximal possible real-root count.

## 3. The parent roots approach the real line uniformly

Write

\[
a=\operatorname{arcosh}c.
\]

The equation `T_n(z)=-c` is solved by

\[
z_{k,\pm}
 =\cos\left({ (2k+1)\pi\pm ia\over n}\right),
\qquad 0\le k<n.
\]

Consequently

\[
|\operatorname{Im}z_{k,\pm}|
 \le\sinh(a/n)
 ={a\over n}+O_c(n^{-3}).
\]

Thus

\[
\boxed{
\max_{p_n(z)=0}|\operatorname{Im}z|
 \longrightarrow0,
}
\tag{R-106451.3
}

while the parent real-zero proportion remains zero and every fixed positive
derivative is real-rooted.

## 4. Binding consequence

No theorem using only

```text
an arbitrarily thin zero strip;
a 99.48% or even 100% real-rooted fourth derivative;
evenness;
ordinary derivative-root convex majorization;
```

can prove a positive parent real-zero proportion in the ambient real-polynomial
class.  The Xi-specific Fourier source, endpoint residue weights or a genuine
full-signature transfer is load bearing in `HBSIG106451/RESGRAM106450`.

The counterfamily does not satisfy the Xi Fourier-source or decay conditions;
it is a scope firewall, not an Xi counterexample.