# Inverse-designed genus-two cusp-trace filters

Status: **PROVED EXACTLY FROM SOURCE-LOCKED MARKED-TRACE THEOREMS**.

Scope: every odd prime power \(q\), for the family \(\mathcal H_5(q)\) of
monic squarefree quintics in \(\mathbf F_q[T]\).

Exact dependencies: the source-locked \(T_{(2,0)}\), \(T_{(4,0)}\),
\(T_{(6,0)}\), and \(T_{(8,0)}\) marked-trace theorems listed in Section 1.

What was run: exact integer and `Fraction` algebra, plus 251 atoms from three
already-frozen joint coefficient laws as held-out controls. No field or curve
was enumerated.

Smallest remaining gap: determine whether the cusp-isolated statistic has a
useful arithmetic or cohomological interpretation beyond its exact family
mean. This packet supplies no individualization mechanism.

## Start here

Write

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
 \qquad {1\over P_D(u)}=\sum_{n\ge0}r_D(n)u^n.                 \tag{1}
\]

Among all integral combinations

\[
 F_c(D)=c_2r_D(2)+c_4r_D(4)+c_6r_D(6)+c_8r_D(8),             \tag{2}
\]

the combinations that cancel both the universal \(q\)-term and constant term
in the marked family trace are exactly

\[
 \boxed{(c_2,c_4,c_6,c_8)
 =m(1,-1,-1,1)+k(0,-4,3,0),\qquad m,k\in\mathbf Z.}          \tag{3}
\]

Their marked trace is

\[
 \boxed{T_c(q)=-m\Theta_{8,2}(q).}                           \tag{4}
\]

There is no two-scale filter with nonzero cusp response. Up to overall sign,
the only primitive three-scale cusp filters are

\[
 \boxed{F_4=3r_8-7r_4+3r_2,\qquad T(F_4)=-3\Theta_{8,2},}    \tag{5}
\]

and

\[
 \boxed{F_6=4r_8-7r_6+4r_2,\qquad T(F_6)=-4\Theta_{8,2}.}    \tag{6}
\]

After normalizing each to unit cusp response, \(F_4/3\) has smaller
\(USp(4)\) Haar variance than \(F_6/4\) for every odd \(q\ge3\). If all four
channels are allowed, the unique rational Haar minimizer is

\[
 \boxed{
 G_q=r_8+r_2-{21q^2\over 9q^2+16}r_4
              -{28\over 9q^2+16}r_6,\qquad T(G_q)=-\Theta_{8,2}(q).
 }                                                            \tag{7}
\]

This is a family-mean filter, not a memberwise sign detector. The preferred
sparse filter \(F_4\) has both signs in each frozen \(q=3,5,7\) family.

## 1. Imported marked traces

The packet imports these exact all-\(q\) identities:

\[
\begin{aligned}
T_{(2,0)}(q)&=q-1,\\
T_{(4,0)}(q)&=-3,\\
T_{(6,0)}(q)&=-4,\\
T_{(8,0)}(q)&=-\Theta_{8,2}(q)-q-6.                    \tag{8}
\end{aligned}
\]

The first two are locked by the
[native reciprocal-wavelet packet](native_qadic_reciprocal_wavelet_spectroscopy.json),
the third by the
[\(\operatorname{Sym}^6\) packet](genus2_sym6_marked_trace_average.json),
and the fourth by the
[\(\operatorname{Sym}^8\) packet](genus2_sym8_marked_trace_average.json).
The producer verifies both LF-normalized file hashes and canonical payload
hashes before using them.

For even \(n\), the marked-root adapter gives

\[
 T_{(n,0)}(q)=q^3\,\mathbb E_{D\in\mathcal H_5(q)}r_D(n).       \tag{9}
\]

Consequently \(T_c=q^3\mathbb E F_c\), and

\[
 \sum_{D\in\mathcal H_5(q)}F_c(D)=q(q-1)T_c(q).                \tag{10}
\]

Nothing in the classification below is fitted from the three frozen fields.

## 2. Exact nuisance-channel classification

Substituting (8) into (2) gives

\[
\begin{aligned}
T_c(q)
={}&-c_8\Theta_{8,2}(q)+(c_2-c_8)q\\
   &-c_2-3c_4-4c_6-6c_8.                              \tag{11}
\end{aligned}
\]

The \(q\)- and constant-channel coefficients vanish exactly when

\[
 c_2=c_8,\qquad 3c_4+4c_6=-7c_8.                              \tag{12}
\]

Set \(m=c_8\). The second congruence says \(c_6\equiv-m\pmod3\),
so \(c_6=-m+3k\) for a unique \(k\in\mathbf Z\). Equation (12) then forces
\(c_4=-m-4k\). This proves (3), including uniqueness of \(m,k\), and (11)
immediately gives (4).

If \(m\ne0\), both \(c_2\) and \(c_8\) are nonzero. A two-scale support would
therefore have \(c_4=c_6=0\), contradicting \(0=-7m\). If \(m=0\), the only
primitive two-scale direction is

\[
 (c_2,c_4,c_6,c_8)=(0,4,-3,0),                               \tag{13}
\]

whose marked trace is identically zero. Thus the precise claim is: no
support-at-most-two nuisance-free filter has nonzero cusp response.

For exactly three scales and \(m\ne0\), either \(c_6=0\) or \(c_4=0\).
Primitivity then reduces (12) respectively to

\[
 (c_2,c_4,c_6,c_8)=(3,-7,0,3)\quad\hbox{or}\quad(4,0,-7,4),  \tag{14}
\]

up to sign. These are (5) and (6).

There is also a canonical integral unit-response baseline. Setting \(m=1\)
in (3), every such filter has coefficients

\[
 (1,-1-4k,-1+3k,1),\qquad k\in\mathbf Z.                  \tag{14a}
\]

Among these integral filters, \(k=0\) is the unique Haar-variance minimizer:

\[
 \boxed{H=r_8-r_6-r_4+r_2,\qquad T(H)=-\Theta_{8,2}(q).}   \tag{14b}
\]

## 3. Exact Haar variances

On normalized \(USp(4)\),

\[
 r_D(2j)=q^j\chi_{(2j,0)}(U_D).                               \tag{15}
\]

The four characters in (15) are distinct nontrivial irreducible characters,
so character orthogonality gives

\[
 \boxed{\operatorname{Var}_{\rm Haar}(F_c)
 =c_2^2q^2+c_4^2q^4+c_6^2q^6+c_8^2q^8.}                     \tag{16}
\]

In particular,

\[
\begin{aligned}
\operatorname{Var}_{\rm Haar}(F_4)&=9q^8+49q^4+9q^2,\\
\operatorname{Var}_{\rm Haar}(F_6)&=16q^8+49q^6+16q^2.       \tag{17}
\end{aligned}
\]

Per unit cusp coefficient,

\[
\begin{aligned}
V_4&=q^8+{49\over9}q^4+q^2,\\
V_6&=q^8+{49\over16}q^6+q^2,\\
V_6-V_4&={49q^4(9q^2-16)\over144}>0\qquad(q\ge3).            \tag{18}
\end{aligned}
\]

For the integral baseline \(H_k\) in (14a),

\[
\operatorname{Var}_{\rm Haar}(H_k)-\operatorname{Var}_{\rm Haar}(H)
=q^4k\bigl((8-6q^2)+(16+9q^2)k\bigr).                    \tag{18a}
\]

For \(k\ge1\), the two factors on the right are positive; for \(k\le-1\),
both are negative. This proves the uniqueness assertion in (14b), with

\[
\operatorname{Var}_{\rm Haar}(H)=q^8+q^6+q^4+q^2.        \tag{18b}
\]

For the full four-channel problem, normalize \(c_8=c_2=1\). Put

\[
 \Delta=9q^2+16.                                               \tag{19}
\]

Minimizing \(q^4c_4^2+q^6c_6^2\) subject to
\(3c_4+4c_6=-7\) gives

\[
 c_4=-{21q^2\over\Delta},\qquad c_6=-{28\over\Delta}.        \tag{20}
\]

This is uniquely optimal because, after writing
\(c_6=(-7-3c_4)/4\), exact completion of the square gives

\[
 V-V_{\min}={q^4\Delta\over16}
 \left(c_4+{21q^2\over\Delta}\right)^2.                      \tag{21}
\]

Thus

\[
 \boxed{V_{\min}=q^8+q^2+{49q^6\over\Delta}.}                \tag{22}
\]

Clearing denominators produces the integral \(q\)-dependent filter

\[
 \Delta(r_8+r_2)-21q^2r_4-28r_6,                              \tag{23}
\]

whose marked trace is \(-\Delta\Theta_{8,2}(q)\).

Equation (16) is a compact-group variance. It is not an assertion that the
finite arithmetic-family variance equals Haar variance.

## 4. Prime-power spectroscopy

For an odd prime \(p\), let \(a_p\) be the \(p\)-th coefficient of the
normalized weight-eight level-two newform

\[
 f(z)=\eta(z)^8\eta(2z)^8.
\]

If \(\alpha_p+\beta_p=a_p\) and \(\alpha_p\beta_p=p^7\), then

\[
 \Theta_{8,2}(p^r)=\alpha_p^r+\beta_p^r.                       \tag{24}
\]

Before filtering, the weight-eight marked trace is

\[
 T_{(8,0)}(p^r)
 =-\alpha_p^r-\beta_p^r-p^r-6\cdot1^r.                        \tag{25}
\]

Its four spectral roots are therefore

\[
 \boxed{\{\alpha_p,\beta_p,p,1\}},                            \tag{26}
\]

with annihilating polynomial

\[
 \boxed{(X^2-a_pX+p^7)(X-p)(X-1).}                            \tag{27}
\]

For a general coefficient vector \(c\), the tower trace is

\[
\begin{aligned}
T_c(p^r)={}&-c_8(\alpha_p^r+\beta_p^r)+(c_2-c_8)p^r\\
 &-(c_2+3c_4+4c_6+6c_8)1^r.                         \tag{28}
\end{aligned}
\]

Thus (12) is exactly a spectral notch filter: it kills roots \(p\) and \(1\)
and leaves only the Hecke pair. Every cusp-isolated trace
\(C_r=-c_8\Theta_{8,2}(p^r)\) obeys

\[
 \boxed{C_r=a_pC_{r-1}-p^7C_{r-2}.}                           \tag{29}
\]

The fixture replays (27)--(29) through \(r=8\) for \(p=3,5,7\). The formal
initial convention is \(\Theta_{8,2}(1)=2\); field traces begin at \(r=1\).

## 5. Held-out \(q=3,5,7\) diagnostics

Only after verifying the four trace-theorem sources and closing the lattice,
Haar, and spectroscopy certificates does the producer parse and iterate the
frozen joint \((a_D,b_D)\) atoms. It reconstructs
\(r_D(0),\ldots,r_D(8)\) from (1) and evaluates \(F_4\). These are exact
falsification controls, not inputs to (3)--(29).

| \(q\) | negative / zero / positive | \(\sum_DF_4\) | \(\mathbb EF_4\) | centered arithmetic variance |
|---:|---:|---:|---:|---:|
| 3 | 75 / 0 / 87 | \(-216\) | \(-4/3\) | \(85916/3\) |
| 5 | 1300 / 0 / 1200 | \(12600\) | \(126/25\) | \(1672701534/625\) |
| 7 | 7434 / 0 / 6972 | \(-128016\) | \(-3048/343\) | \(4844515276200/117649\) |

The theorem prediction in each row is

\[
 \sum_DF_4(D)=-3q(q-1)\Theta_{8,2}(q),                         \tag{30}
\]

using \(a_3=12\), \(a_5=-210\), and \(a_7=1016\).

The already-identified \(a_D=b_D=0\) stratum makes a striking but finite
cancellation diagnostic. On it,

\[
 F_4=q^2(3q^2+7)>0.                                           \tag{31}
\]

Its signed contribution and its ratio to the full signed total are

| \(q\) | stratum members | stratum contribution | ratio to full total |
|---:|---:|---:|---:|
| 3 | 12 | \(3672\) | \(-17\) |
| 5 | 50 | \(102500\) | \(1025/126\) |
| 7 | 336 | \(2535456\) | \(-7546/381\) |

This does not establish a stratum law for other fields. It records that a
large same-sign exceptional contribution is cancelled by the rest of each
frozen family.

## 6. Replay and firewalls

Run

```powershell
python research/l-families/atlas/function_field/genus2_inverse_cusp_trace_filters.py --check
python -O research/l-families/atlas/function_field/genus2_inverse_cusp_trace_filters.py --check
python -m unittest tests.test_genus2_inverse_cusp_trace_filters
```

The replay uses at most 512 frozen source atoms, 4096 recurrence updates,
1024 bounded lattice-regression points, and four seconds. The actual held-out
atom count is 251, and the regression grid has 625 points. It performs no
finite field, curve, or polynomial-family enumeration.

The cumulative atom and recurrence budgets are checked before each held-out
recurrence, the lattice budget is checked before its bounded grid, and the
wall-clock postcondition is checked after canonical payload hashing.

Firewalls:

- The packet proves an exact family-trace cancellation, not a memberwise sign.
- Haar variance and finite-family variance are different objects.
- The three frozen fields do not prove an all-\(q\) sign, tail, or variance law.
- The four imported marked-trace identities remain explicit dependencies.
- No RH, GRH, novelty, motive, compatible-system, or global Euler-product
  claim is made.
