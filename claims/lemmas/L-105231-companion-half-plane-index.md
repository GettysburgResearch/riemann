# L-105231 — Lower companion poles are exactly the nonreal-pair index

Claim ID: `L-105231`  
Status: **PROVED EXACT FOR REAL POLYNOMIALS; ENTIRE PASSAGE USES THE PR #720 CANONICAL-PRODUCT INTERFACE**  
Depends on: L-104510 at PR #720 head `10bba584c...`

Let `p` be a real polynomial with `gcd(p,p')=1` and let `delta>0`.  Define
\[
G_\delta=p'+i\delta p.
\]
Since
\[
G_\delta=i\delta\bigl(p-i\delta^{-1}p'\bigr),
\]
L-104510 gives
\[
\boxed{
N_-(G_\delta)=\frac{N_{\rm nr}(p)}2,
}
\tag{1}
\]
where `N_-` counts lower-half-plane zeros and `N_nr(p)` counts nonreal zeros,
both with multiplicity.

Apply (1) with `p=F_k`.  The lower-half-plane poles introduced by the
companion field in L-105230 are therefore owned exactly by the nonreal
conjugate pairs of `F_k`.  If `F_k` is real-rooted, there is no lower companion
pole at all.

For a finite horizontal window, a thin collar around the real axis may be
chosen to contain its real `F_k` zeros while avoiding every nonreal `F_k` zero
and every upper companion zero.  Formula L-105230.5 on that collar contains
only:

```text
real square-defect residues;
lower companion-pole residues;
one explicit boundary flux.
```

The collar height may shrink with the window.  Controlling that degeneration
is part of the remaining analytic estimate, not part of the index theorem.
