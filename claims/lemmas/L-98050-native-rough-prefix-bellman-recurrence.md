# L-98050 — Native rough-prefix Bellman recurrence and continuous Dickman margin

Claim ID: `L-98050`  
Status: **PROVED EXACT SOURCE RECURRENCE + CONTINUOUS MODEL INEQUALITY**  
Created: 2026-08-18  
Depends on: `L-98040`; classical Dickman differential-delay equation  
RH status: **not assumed**

Let

\[
U(Y,z)={\mathcal F(Y,z)\over\sqrt Y},
\]

where `mathcal F` is the literal native rough state of `L-98040`.  If `p` is the least allowed rough prime and `p^+` denotes the next-prime state, unique least-prime ownership gives exactly

\[
\boxed{
U(Y,p)=U(Y,p^+)-{1\over p}U(Y/p,p^+).
}
\tag{L-98050.1}
\]

No truncation, smoothing, or unsigned comparison enters this identity.

For the homogeneous Dickman model with

\[
L=\log p,
\qquad
u={\log Y\over L},
\]
write

\[
D(Y,p)=a_*\rho(u).
\]

The child endpoint `Y/p` has Dickman coordinate `u-1`, so the corresponding Bellman margin is

\[
\boxed{
\mathfrak M(u,p)
=a_*\left[\rho(u)-{1\over p}\rho(u-1)\right].
}
\tag{L-98050.2}
\]

For `u>1`, Dickman's equation `u rho'(u)+rho(u-1)=0` implies

\[
{\rho(u-1)\over\rho(u)}
=-u{\rho'(u)\over\rho(u)}.
\]

The standard de Bruijn ratio estimate gives

\[
{\rho(u-1)\over\rho(u)}\ll u\log(u+2).
\tag{L-98050.3}
\]

Hence there is an absolute constant `C_D` such that

\[
\boxed{
p\ge 2C_Du\log(u+2)
\Longrightarrow
\mathfrak M(u,p)\ge {a_*\over2}\rho(u)>0.
}
\tag{L-98050.4}
\]

Thus the continuous model has a quantitative one-prime Bellman margin throughout the region

\[
p\gg u\log u.
\]

The exact discrete problem is to show that the prime-measure discrepancy in `L-98042` is smaller than this margin. This is strictly stronger than mere positivity of the parent and child states and is the source-faithful form of the surviving Bellman gate.
