# Scale-matched root-residue programme: attempted closure, retraction, and corrected frontier

Date: 2026-08-25  
Execution PR: #751  
Programme issues: #743, #736, #737  
Parent merged into branch: PR #719 at `60285de21fafdd1b3c185ddd19b57191a41c08dd`  
Continuation base: PR #751 at `74916ff37b98574e17e6f979453879c472f8b596`  
Status: **full closure proposal retracted; corrected quadratic frontier published**

## 1. Valid block-local mechanism

On one stopped-Vaughan block

\[
u\sim U,\qquad v\sim V,\qquad m\sim M,\qquad B=UVM,
\]

every core lies in \([B,8B)\).  Four disjoint Bertrand intervals provide four
candidate primes; after excluding the marked prime `67`, three remain with

\[
16B<\ell_j<256B.
\]

Colour each linear source atom by the subset of these palette primes dividing
its semiprime owner product.  Since an owner has at most two prime factors, one
palette prime is absent.  Choosing that prime gives a disjoint source
partition on which the principal character is literally the native block.

For fixed owners \(P,Q\), character orthogonality gives

\[
Pc^2\equiv Qd^2\pmod\ell.
\]

A nonsquare owner ratio vanishes; a square ratio gives

\[
c\equiv\pm\tau d\pmod\ell.
\]

Because \(c,d\in[B,8B)\) and \(\ell>16B\), each line is a partial matching.
This proves that repeated cores inside one fixed owner-pair line are not the
remaining obstruction.

## 2. Valid conductor payments

The exact block energy is

\[
E_{P,B}\ll\frac{X^{o(1)}}{PB}.
\]

Since \(\ell\asymp B\), the diagonal character cost is subpower:

\[
\ell\sum_P E_{P,B}=X^{o(1)}.
\]

The same energy also pays the quartic matched-pair tensor

\[
\ell\sum_{P,Q,d}
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2
=X^{o(1)}.
\]

These statements remain proved.

## 3. Hostile audit and retraction

The attempted closure then identified the quartic tensor above with the
quadratic Dirichlet-family occupancy.  That was false.

The exact family object is

\[
\boxed{
\mathcal Q_{B,A}
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r\pmod\ell}Z_{P,c}
\right\|^2.
}
\]

It scales quadratically in the source.  The matched-pair tensor scales
quartically.  `R-106071` gives an explicit one-residue many-owner fixture in
which the quadratic Gram equals one while \(\ell\) times the quartic tensor
can be arbitrarily small.

Therefore:

```text
first L-106073 HBC closure              retracted;
first T-106070 RH closure proposal       retracted;
Riemann Hypothesis                       unproved.
```

The exact first failed edge was

```text
quartic matched-pair occupancy
    -> quadratic character-family moment.
```

## 4. Corrected normal form

`L-106074` proves exact character Parseval:

\[
\frac1{\ell-1}\sum_\chi\|V_\chi\|^2
=
\mathcal Q_{B,A},
\]

and principal inclusion

\[
\|R_{B,A}\|^2\le(\ell-1)\mathcal Q_{B,A}.
\]

For one owner and residue there are at most two core lifts.  If \(\nu_r\) is
the number of distinct owner packets in residue cell \(r\), then

\[
\|A_r\|^2
\le
2\nu_r
\sum_{Pc^2\equiv r}\|Z_{P,c}\|^2.
\]

Thus every cell with \(\nu_r=X^{o(1)}\) is closed.  The surviving theorem is
only the high-crowding quadratic owner assembly:

```text
HQORO106071:
  the source-weighted logarithmic sum of ell * ||A_r||^2 over cells containing
  a power-sized coherent family of distinct owners is subpower.
```

The exact conditional chain is

\[
\mathrm{HQORO}_{106071}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
\]

`HQORO106071` remains open.

## 5. Relation to `BPOE103300`

The remaining high-crowding residue cell is a finite-field block coordinate of
the global physical occupancy map `BPOE103300`: source-orthogonal owner
packets become coherent after their arithmetic labels are identified by the
physical product observation.

The scale-matched pass has therefore removed:

```text
modulus/source-order ambiguity;
ramified-principal ambiguity;
repeated-core residue multiplicity;
diagonal conductor cost;
all subpower owner-crowding cells.
```

It has not removed coherent aggregation of a power-sized owner family.

## 6. Replays

```text
PASS_X_106070_SCALE_MATCHED_ROOT_OCCUPANCY
checks=166834
sha256=67e946c4710d492cae450d7a2581f72e81ab7d8b72c11f5871ad24121212748b

PASS_X_106071_QUADRATIC_VS_QUARTIC_FIREWALL
checks=7472
sha256=145e8e6e7fa3cc38c75fef3083ede2a6dfdb7feba6f441222e0605921315d9a7
```

`X-106070` continues to certify its finite palette, matching and quartic
payment algebra.  `X-106071` certifies the homogeneity counterexample, exact
quadratic residue Gram and low-crowding Cauchy theorem.  Neither replay proves
`HQORO106071`, `BPOE103300`, the Mellin consumer, or RH.