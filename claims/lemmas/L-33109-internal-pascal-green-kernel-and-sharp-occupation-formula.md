# L-33109 — The internal-uniform Pascal chain has an exact constant entrance Green kernel

Claim ID: `L-33109`  
Title: For the uniform nontrivial Pascal split law, every lower node has parent-independent hitting probability `2/(n+1)`; the exact average-carry inverse is therefore one closed Green potential of the Möbius divergence  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Dependencies: `L-33107`; PR #329/PR #337 exact average-carry inverse formulas  
Scope: exact Green kernel and SHARP reformulation; no proof of the final sign or RH

## 1. Uniform nontrivial split law

For a parent `m>=2`, choose `J` uniformly from

\[
1,2,\ldots,m-1
\]

and then follow a uniformly selected unit of parent mass into its child. The selected child `K` has the exact law

\[
\boxed{
 P_m(K=k)={2k\over m(m-1)},
 \qquad1\le k<m.
}
\tag{L-33109.1}

Indeed the split `J=k` contributes `k/[m(m-1)]`, and the reflected split `J=m-k` contributes the same amount; at the central split the two size contributions belong to the same child and add correctly.

This is the non-lazy version of the finite Pascal law in `L-33104`, obtained by conditioning away the two zero-carry endpoint splits.

## 2. Exact hitting probability

Fix a node `n>=1`. Let

\[
 h_m^{(n)}=\Pr_m(\tau_n<\infty)
\]

for the strictly descending chain (L-33109.1). Clearly

\[
 h_n^{(n)}=1,
 \qquad h_m^{(n)}=0\quad(m<n).
\]

For `m>n`, harmonicity gives

\[
 h_m^{(n)}
 ={2\over m(m-1)}
 \sum_{k=n}^{m-1}k h_k^{(n)}.
\tag{L-33109.2}

The exact solution is

\[
\boxed{
 h_m^{(n)}={2\over n+1}
 \qquad(m>n).
}
\tag{L-33109.3}

### Proof

At `m=n+1`,

\[
 h_{n+1}^{(n)}
 ={2n\over(n+1)n}={2\over n+1}.
\]

Assume (L-33109.3) for `n<k<m`. Then

\[
\begin{aligned}
 h_m^{(n)}
 &={2\over m(m-1)}
 \left[n+{2\over n+1}
       \sum_{k=n+1}^{m-1}k\right]\\
 &={2\over m(m-1)}
 \left[n+{m(m-1)-n(n+1)\over n+1}\right]\\
 &=\boxed{{2\over n+1}}.
\end{aligned}
\]

Thus the entrance probability is independent of the starting parent once that parent lies above `n`.

Because the chain is strictly descending, a node is visited at most once. Therefore the Green kernel itself is

\[
\boxed{
 G(m,n)=
 \begin{cases}
 1,&m=n,\\
 {2\over n+1},&m>n,\\
 0,&m<n.
 \end{cases}}
\tag{L-33109.4
}

## 3. Green occupation of an arbitrary source

Let `r_1,...,r_X` be any node divergence and put

\[
 s_m=mr_m.
\]

The signed size occupation solving

\[
 M-MP=s
\]

is, by (L-33109.4),

\[
\boxed{
 M_n=s_n+{2\over n+1}
 \sum_{m=n+1}^{X}s_m.
}
\tag{L-33109.5
}

No recursion remains.

For the corresponding uniform internal split flow, `L-33107` gives

\[
 D_n={M_n\over n},
 \qquad
 d_{n,j}={M_n\over n(m-1)}\quad(1\le j<n),
\]

where the parent in the denominator is `n`; equivalently

\[
 d_{n,j}={M_n\over n(n-1)}.
\tag{L-33109.6}

## 4. Identification with the exact average-carry inverse

Let `c_X(n)` be the unique inverse coefficients of the ordinary row-averaged carry matrix

\[
 w_X(q)=\sum_{n=q}^{X}c_X(n)\beta_{nq},
\]

where

\[
 \beta_{nq}={1\over n+1}\sum_{j=0}^{n}\chi_{n,j}(q).
\]

The endpoint splits `j=0,n` carry zero, so assigning

\[
 d_{n,j}={c_X(n)\over n+1},
 \qquad1\le j<n,
\]

reproduces the same carry load. Its total outgoing coefficient is

\[
 D_n={n-1\over n+1}c_X(n).
\]

Thus

\[
 M_n=nD_n={n(n-1)\over n+1}c_X(n),
\]

and hence

\[
\boxed{
 c_X(n)={n+1\over n(n-1)}M_n.
}
\tag{L-33109.7
}

Combining with (L-33109.5),

\[
\boxed{
 c_X(n)
 ={n+1\over n(n-1)}
 \left[
 nr_X(n)+{2\over n+1}
 \sum_{m=n+1}^{X}mr_X(m)
 \right].
}
\tag{L-33109.8
}

This is the exact Green interpretation of the Möbius-increment inverse formula on the SHARP branches.

## 5. Local-versus-tail form of Carry Saturation

Define the upper size tail

\[
\boxed{
 S_X(n)=\sum_{m=n}^{X}mr_X(m).
}
\tag{L-33109.9
}

Since the factor in (L-33109.7) is positive,

\[
 c_X(n)\ge0
\]

is equivalent to

\[
\boxed{
 nr_X(n)+{2\over n+1}S_X(n+1)\ge0.
}
\tag{L-33109.10
}

Equivalently, because `S_X(n)=nr_X(n)+S_X(n+1)`,

\[
\boxed{
 2S_X(n)+(n-1)nr_X(n)\ge0.
}
\tag{L-33109.11
}

Thus the complete average-carry positivity theorem is one sharp statement comparing each negative local Möbius source jump with the positive mass remaining strictly above it.

## 6. Multiple-Möbius coordinate form

For the critical target let

\[
 U_X(n)=\sum_{k\le X/n}\mu(k)w_X(nk),
 \qquad
 r_X(n)=U_X(n)-U_X(n+1).
\]

Summation by parts gives

\[
\boxed{
 S_X(n)=nU_X(n)+\sum_{m=n+1}^{X}U_X(m).
}
\tag{L-33109.12
}

Substitution into (L-33109.8) gives

\[
\boxed{
\begin{aligned}
 c_X(n)={1\over n(n-1)}\Big[&
 (n+1)(nU_X(n)-(n-2)U_X(n+1))\\
 &+2\sum_{m=n+2}^{X}U_X(m)
 \Big],
\end{aligned}}
\tag{L-33109.13
}

which is exactly the previously derived triangular carry-inverse formula, now obtained as a Green-potential identity.

## 7. Proof boundary

Established exactly:

1. the non-lazy internal Pascal selected-child law;
2. its parent-independent entrance probability;
3. the complete Green kernel;
4. closed Green occupation for an arbitrary signed divergence;
5. exact identification with the average-carry inverse;
6. local-versus-upper-tail formulation of Carry Saturation;
7. equivalence with the existing Möbius-increment inverse formula.

Still open:

1. the sign inequality (L-33109.10)/(L-33109.11) for the critical target at every depth;
2. SHARP/Carry Saturation;
3. RH.
