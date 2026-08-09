# L-34411 — The Q4 all-pass reservoir collapses on the Möbius odd-Jordan path

Claim ID: `L-34411`  
Title: Applying the Q4 Euler--Blaschke colligation to the Möbius odd-Jordan path gives an exact compact-current/base-state block identity; its input current is the sum of two consecutive root-Haar detail currents  
Status: **PROPOSED COMPLETE EXACT BLOCK/SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; `L-34409`; odd-Jordan source typing; PR #241 independent-frequency localization  
Scope: aligned logarithmic blocks and aligned integer rows; no estimate of the root-detail square function and no RH conclusion

## 1. Three finite filters over one source path

Put

\[
z=2^{-s},
\qquad
x=z^2=4^{-s},
\qquad
L=\log4,
\]

and retain the Möbius odd-Jordan source path

\[
\boxed{
g_\tau(s)=\frac1{\zeta(s)}J_{{\rm odd},\tau}(s).
}
\tag{L-34411.1}

Define

\[
\boxed{
h_\tau=(1-x)g_\tau,
\qquad
c_\tau=(1-4x)g_\tau.
}
\tag{L-34411.2}

The second path is the odd-prime Jordan part of the denominator-free compact Q4 source:

\[
 c_\tau
 =(\varepsilon-4\delta_4)*\mu*J_{{\rm odd},\tau}.
\]

The first path is the scale-four Haar difference

\[
 h_\tau
 =(\varepsilon-\delta_4)*\mu*J_{{\rm odd},\tau}.
\]

All filters in (L-34411.2) are independent of the Jordan parameter.

## 2. Exact Q4 all-pass factorization

The Q4 Euler--Blaschke multiplier is

\[
E_4(s)=\frac{1-4x}{1-x}.
\]

On the critical line, `E_4/2` is the scalar all-pass function with state reservoir

\[
R(s)=\frac{\sqrt3/2}{1-x}.
\]

By construction

\[
\boxed{c_\tau=E_4h_\tau,}
\tag{L-34411.3}
\]

and the reservoir denominator cancels exactly:

\[
\boxed{
Rh_\tau=\frac{\sqrt3}{2}g_\tau.
}
\tag{L-34411.4}

Thus the all-pass state is not a new inverse source, infinite tail, or unnamed boundary.  It is precisely the base Möbius odd-Jordan path.

## 3. Exact independent-frequency block identity

Let `B_I(f)` denote the independent-frequency physical block Gram of PR #241 on a logarithmic block `I`.  PR #339 `L-33804` gives for every input `f`

\[
4B_I(f)-B_I(E_4f)
=4\bigl[B_I(Rf)-B_{I-L}(Rf)\bigr].
\]

Substitute `f=h_tau` and use (L-34411.3)--(L-34411.4).  One obtains

\[
\boxed{
4B_I(h_\tau)-B_I(c_\tau)
=3\bigl[B_I(g_\tau)-B_{I-L}(g_\tau)\bigr].
}
\tag{L-34411.5}

Every term is source complete and uses the same two independent frequencies.  There is no one-frequency localization or hidden physical-to-carry map.

## 4. Exact Jordan-curvature recurrence

For a twice differentiable Hilbert path `f_tau`, define

\[
\mathfrak C_I(f)
=\|\partial_\tau\mathcal P_f|_0\|_I^2
 -\operatorname{Re}
  \langle\mathcal P_{f_0},
          \partial_\tau^2\mathcal P_f|_0\rangle_I.
\tag{L-34411.6}
\]

Because every filter in Sections 1--2 is independent of `tau`, differentiate (L-34411.5) twice in the imaginary Jordan direction.  The result is the exact curvature identity

\[
\boxed{
4\mathfrak C_I(h)
-\mathfrak C_I(c)
=3\bigl[
 \mathfrak C_I(g)-\mathfrak C_{I-L}(g)
 \bigr].
}
\tag{L-34411.7}

Equivalently,

\[
\boxed{
\mathfrak C_I(c)+3\mathfrak C_I(g)
=4\mathfrak C_I(h)+3\mathfrak C_{I-L}(g).
}
\tag{L-34411.8}

This is already in the coefficient-one state-telescope orientation: the base state returns only on the immediately preceding `log 4` block.

## 5. The all-pass input has zero bare charge

At `tau=0`, the source of `h` is

\[
 b_h=(\varepsilon-\delta_4)*\mu.
\]

Since

\[
\mathbf1*b_h=\varepsilon-\delta_4,
\]

its ordinary prefix stabilizes at zero.  Hence every nontrivial row outside the finite endpoint collar has

\[
\boxed{Y_h=0.}
\tag{L-34411.9}

Consequently its source curvature is a pure current square:

\[
\boxed{
\mathfrak C_I(h)
=\|\mathcal P_{q_h}\|_I^2
}
\tag{L-34411.10}

at the source-coordinate level, with the generalized-prime reserve inserted separately in the complete augmented ledger.

At an aligned integer row `4e`, if

\[
Q_0(e)=\mathcal L_e(\mu*\Lambda_{\rm odd}),
\]

then

\[
\boxed{
Q_h(4e)=Q_0(4e)-Q_0(e).
}
\tag{L-34411.11}

The compact output current is

\[
\boxed{
Q_c(4e)=Q_0(4e)-4Q_0(e).
}
\tag{L-34411.12}

Thus the all-pass colligation places the critical compact current and its base state in one exact source ledger.

## 6. The input current is two consecutive root-Haar details

Define the root-Haar detail of `L-34409` by

\[
D_{\rm root}(e)
=Q_0(4e)-Q_0(2e).
\tag{L-34411.13}
\]

At the immediately lower dyadic stage put

\[
D_{\rm root}^{\downarrow}(e)
=Q_0(2e)-Q_0(e).
\tag{L-34411.14}
\]

Then (L-34411.11) is exactly

\[
\boxed{
Q_h(4e)
=D_{\rm root}(e)+D_{\rm root}^{\downarrow}(e).
}
\tag{L-34411.15}

Both detail channels have zero bare charge and therefore pure-square source curvatures.  The Hilbert-space parallelogram bound gives

\[
\boxed{
\|\mathcal P_{Q_h}\|^2
\le2\|\mathcal P_{D_{\rm root}}\|^2
 +2\|\mathcal P_{D_{\rm root}^{\downarrow}}\|^2.
}
\tag{L-34411.16}

No generalized-prime reserve has been used in (L-34411.16); it is an exact routing of the all-pass input into two already typed zero-bare-charge channels.

## 7. Combined source ledger

Substituting (L-34411.10) and (L-34411.16) into (L-34411.8) gives the rigorous routed inequality

\[
\boxed{
\begin{aligned}
\mathfrak C_I(c)+3\mathfrak C_I(g)
\le{}&8\|\mathcal P_{D_{\rm root}}\|_I^2\\
&+8\|\mathcal P_{D_{\rm root}^{\downarrow}}\|_I^2\\
&+3\mathfrak C_{I-L}(g),
\end{aligned}}
\tag{L-34411.17}

up to only the declared finite collars when block endpoints are not aligned.

Equation (L-34411.17) is not yet the RH recurrence: the two root-detail square functions still require dissipative payment.  It does, however, remove the compact source, Q4 reservoir, and relative odd source as independent states.  The entire unresolved current has been reduced to two consecutive root-Haar details plus one predecessor base state.

## 8. Relation to the corrected odd-relative ledger

`L-34409` proves that each root-detail square is the complementary channel to a corrected odd-relative low-pass curvature:

\[
\mathfrak C_+(4e)
+|D_{\rm root}(e)|^2
=2\mathfrak C_0(4e)+2\mathfrak C_0(2e).
\]

The same identity one stage lower treats `D_root^downarrow`.  Therefore the root terms in (L-34411.17) are not untyped losses. They are the two explicit orthogonal complements of the low-pass relative states already carrying the critical odd-prime reserve.

The remaining theorem can now be stated without hidden source species:

> prove a coefficient-one independent-frequency square-function estimate for the two consecutive root-Haar detail channels against the two corrected low-pass reserve increments.

That statement is still RH-bearing and is not claimed here.

## 9. Proof boundary

Closed exactly:

1. Q4 all-pass input/output/source factorization;
2. exact cancellation of the reservoir denominator;
3. complete independent-frequency block identity;
4. its Jordan-curvature derivative;
5. zero bare charge of the all-pass input;
6. exact routing into two consecutive root-Haar details;
7. the combined compact/base/root source ledger.

Open:

1. dissipative payment of the two root-detail square functions;
2. coefficient-one global block recurrence;
3. subpower reciprocal-zeta pole-current energy;
4. RH.
