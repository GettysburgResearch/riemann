# L-97010 — Grouping and scalarization preserve the accumulated rough-history character

Claim ID: `L-97010`  
Status: **PROVED EXACT**  
Base: PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
Compared: PR #556 and PR #559  
RH status: **unproved**

Let `V` be any real vector space of finite-color data and let

\[
\mathscr P=V\oplus V,
\qquad
S(u,v)=(v,u).
\]

The two components record even and odd accumulated arithmetic parity. For any
linear row functional `ell:V->R`, define the signed observation

\[
\mathcal O_\ell(u,v)=\ell(u)-\ell(v).
\]

Then, for every integer `m>=0`,

\[
\boxed{\mathcal O_\ell S^m=(-1)^m\mathcal O_\ell.}
\tag{L-97010.1}
\]

Now let `G:V->W` be any linear finite-color grouping map and act diagonally on
parity space:

\[
\widetilde G(u,v)=(Gu,Gv).
\]

Because `\widetilde G S=S\widetilde G`, every grouped observation satisfies

\[
\boxed{
\mathcal O_\eta\widetilde G S^m
=(-1)^m\mathcal O_\eta\widetilde G
}
\tag{L-97010.2}
\]

for every linear `eta:W->R`. Thus summing all `d|P_61` colors before observation,
as required by PR #556, is the correct color interface but does not erase the
rough-history sign isolated by PR #561.

The same conclusion holds for every fixed scalar combination of rows. If

\[
\mathcal R=5\mathcal O_2+3\mathcal O_3,
\]

then

\[
\boxed{\mathcal R S^m=(-1)^m\mathcal R.}
\tag{L-97010.3}
\]

Consequently the one-dimensional reduction of PR #559 removes the need for a
common-zero argument between two row numerators, but it does not repair a
parity-blind leaf realization or a fixed-depth parity reset.

## Proof

Equation (L-97010.1) follows from

\[
\mathcal O_\ell S(u,v)=\ell(v)-\ell(u)=-\mathcal O_\ell(u,v)
\]

and induction. Equation (L-97010.2) follows from diagonal action and
commutation. Equation (L-97010.3) follows by linearity. No positivity,
asymptotic estimate, or analytic continuation is used.

## Interface consequence

The only safe order of operations is

```text
rough-source ownership and accumulated parity
    -> complete finite-color grouping
    -> row or scalar observation.
```

Changing the second or third stage cannot change the character `(-1)^m`
carried by the first stage.
