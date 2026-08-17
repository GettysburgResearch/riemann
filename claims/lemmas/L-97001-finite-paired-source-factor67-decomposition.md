# L-97001 — Finite paired-source factor-67 decomposition for the single scalar

Claim ID: `L-97001`  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — HOSTILE ATOMWISE REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen inputs: PR #555 at `341697b4694ba7f44f2ba2be73cb3fc982939412`; PR #550 at `20646a78c3e8843001cb49ea0c9741f6d0d446f7`

## 1. Root source

For fixed real `X>=1`, retain the finite positive parity-labelled source
\[
\mathscr N_X=
\bigoplus_{k\le X/2,\ \mu(k)\ne0}
 k^{-1/2}[\mathscr Q_{X/k},\operatorname{parity}\mu(k)].
\tag{L-97001.1}
\]
Signed physical observation is postponed. Under the scalar observation
`5R_2+3R_3`, its marginal is exactly `mathcal R_X`.

Every squarefree colour has the unique factorization
\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t.
\tag{L-97001.2}
\]
The label records `d`, ordered rough history, parity, path, and first unused
rough owner.

## 2. Exact one-generation identity

For active rough primes `p_i`, put
\[
r_i=p_i^{-1/2},\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad s_0=1,
\]
\[
\lambda_i=r_i s_{i-1},\qquad
\alpha_i=r_i\lambda_i.
\]
Then, in the paired source category,
\[
\boxed{
P=s_kP+\sum_i\lambda_i(P-r_iU_{p_i}P_i)
+\sum_i\alpha_iU_{p_i}P_i.
}
\tag{L-97001.3}
\]
Indeed `s_k+sum lambda_i=1` and `alpha_i=r_i lambda_i`. The parent is spent
once, and
\[
\sum_i\alpha_i<67^{-1/2}<1/8.
\tag{L-97001.4}
\]
Every unresolved child has scale at most `1/67` of its parent.

## 3. Finite rank induction

Apply the exact paired stopping identity only to unresolved positive children.
Use rank
\[
\operatorname{rk}(Z)=
\min\{m:Z/67^m<67\}.
\tag{L-97001.5}
\]
Each unresolved child has smaller rank; hence induction terminates after
finitely many substitutions. Intermediate oriented differences remain paired
source objects and are never separately observed.

The claimed terminal equality is
\[
\boxed{
\mathscr N_X=
\bigoplus_{\ell\in\mathcal L_X}
\omega_\ell\mathscr P_\ell,
\qquad \omega_\ell\ge0,
}
\tag{L-97001.6}
\]
where every terminal packet is either an outer source of scale `<67` or a
complete grouped leaf `(p,y,d)` with `p>=67`, `1<=y<67`, `d|P61`.

The load-bearing atomwise statement is
\[
\boxed{
\text{every original squarefree occurrence has exactly one terminal owner,
with unchanged coefficient }k^{-1/2}.
}
\tag{L-97001.7}
\]
This follows from unique factorization, first-owner disjointness, exact
coefficient cancellation in (L-97001.3), and finite rank induction. It is the
first hostile reconstruction target.
