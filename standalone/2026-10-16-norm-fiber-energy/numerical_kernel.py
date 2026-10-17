#!/usr/bin/env python3
"""Non-certified 65-digit checks of the full higher-order Gaussian kernel.

Complete native good ideal columns through norm 13 over Q(omega): unit and
both ideals above each of 7 and 13. Actual sextic rows have norms 1, 3 and 7.
This is finite polynomial quadrature, not an infinite arithmetic evaluation.
Requires mpmath; it is separate from the standard-library exact checker.
"""
from __future__ import annotations
import itertools
import json
import mpmath as mp

mp.mp.dps=65
C=mp.mpf(5)/6
ROOT=mp.exp(mp.j*mp.pi/3)


def character(p: int, omega_root: int, row: tuple[int,int]) -> mp.mpc:
    value=(row[0]+row[1]*omega_root)%p
    if value==0:
        return mp.mpc(0)
    sixth=pow(value,(p-1)//6,p)
    base=(1+omega_root)%p
    j=next(j for j in range(6) if pow(base,j,p)==sixth)
    return ROOT**j


def columns(row: tuple[int,int]) -> list[tuple[int,mp.mpc]]:
    return [(1,mp.mpc(1))]+[(p,-character(p,r,row)) for p in (7,13)
                              for r in range(p) if (r*r+r+1)%p==0]


def source_log(x: mp.mpf, cols: list[tuple[int,mp.mpc]]) -> mp.mpc:
    return mp.fsum(a*mp.exp(-C*(mp.log(n)-x)-(mp.log(n)-x)**2/4)/(2*mp.sqrt(mp.pi))
                   for n,a in cols)


def grouped(k: int, cols: list[tuple[int,mp.mpc]]) -> dict[int,mp.mpc]:
    result={}
    for tup in itertools.product(cols,repeat=k):
        norm=1
        coeff=mp.mpc(1)
        logs=[]
        for n,a in tup:
            norm*=n
            coeff*=a
            logs.append(mp.log(n))
        avg=mp.log(norm)/k
        balance=mp.exp(-mp.fsum((v-avg)**2 for v in logs)/4)
        result[norm]=result.get(norm,mp.mpc(0))+coeff*balance
    return result


def w_k_log(t: mp.mpf,k: int) -> mp.mpf:
    return (2*mp.sqrt(mp.pi))**(-k)*mp.exp(-C*t-t*t/(4*k))


def kernel(n: int, m: int, D: int,k: int) -> mp.mpf:
    beta=2*C-1
    gamma=mp.sqrt(2*mp.pi*k)/k*(2*mp.sqrt(mp.pi))**(-2*k)*mp.exp(k*beta*beta/2)
    a,b=mp.log(n),mp.log(m)
    t=(k*mp.log(D)-(a+b)/2-k*beta)/mp.sqrt(k)
    cdf=mp.erfc(-t/mp.sqrt(2))/2
    return gamma/mp.sqrt(n*m)*mp.exp(-(a-b)**2/(8*k))*cdf


def main() -> dict:
    cases=[]
    for k,row in ((1,(1,0)),(2,(2,1)),(3,(3,1))):
        cols=columns(row)
        grouped_c=grouped(k,cols)
        D=20
        point_errors=[]
        for X in (4,10,25):
            lhs=source_log(mp.log(X),cols)**k
            rhs=mp.fsum(a*w_k_log(mp.log(n)-k*mp.log(X),k) for n,a in grouped_c.items())
            err=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
            if err>mp.mpf('1e-55'):
                raise RuntimeError('finite higher-order Gaussian grouping failed')
            point_errors.append(mp.nstr(err,8))
        integral=mp.quad(lambda x:abs(source_log(x,cols))**(2*k)*mp.exp(-k*x),
                         [-mp.inf,-10,0,mp.log(D)])
        pair=mp.fsum(kernel(n,m,D,k)*a*mp.conj(b)
                     for n,a in grouped_c.items() for m,b in grouped_c.items())
        relative=abs(integral-pair)/max(1,abs(integral),abs(pair))
        if relative>mp.mpf('1e-48'):
            raise RuntimeError('finite Gaussian energy kernel disagrees with quadrature')
        normdiag=mp.fsum(kernel(n,n,D,k)*abs(a)**2 for n,a in grouped_c.items())
        # Absolute sparse-neighbor sum; same complete product-norm fibers.
        graph=[]
        norms=sorted(grouped_c)
        R=12
        degree=max(sum(0<abs(n-m)<=R for m in norms) for n in norms)
        for n in norms:
            for m in norms:
                if 0<abs(n-m)<=R:
                    graph.append(kernel(n,m,D,k)*abs(grouped_c[n]*grouped_c[m]))
        graph_sum=mp.fsum(graph)
        if graph_sum>degree*normdiag+mp.mpf('1e-55'):
            raise RuntimeError('Gaussian sparse graph budget failed')
        cases.append({"k":k,"moment_order":2*k,"row":row,
                      "row_norm":row[0]**2-row[0]*row[1]+row[1]**2,
                      "column_cap":13,"all_good_ideal_columns":len(cols),
                      "nonzero_row_coefficients":sum(a!=0 for _,a in cols),
                      "complete_ordered_k_tuples":len(cols)**k,
                      "product_norm_fibers":len(grouped_c),"D":D,
                      "energy_quadrature":mp.nstr(integral,45),
                      "kernel_relative_error":mp.nstr(relative,8),
                      "pointwise_relative_errors":point_errors,
                      "norm_block":mp.nstr(normdiag,45),
                      "norm_gap_R":R,"actual_max_neighbor_count":degree,
                      "absolute_graph_sum":mp.nstr(graph_sum,45)})
    return {"status":"PASS: finite floating-point checks, NOT certified intervals",
            "decimal_precision":mp.mp.dps,"cases":cases,
            "limits":["Same-author finite checks; no asymptotic evidence.",
                      "Only complete good columns through norm 13, not the infinite source.",
                      "Ordinary arbitrary-precision arithmetic, not directed rounding.",
                      "Kernel and quadrature share source coefficients but use different energy assemblies."]}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
