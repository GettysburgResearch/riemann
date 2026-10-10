#!/usr/bin/env python3
"""Prime-tail activation envelopes for exact exclusion-pair polynomials.

Each infinite prime tail is partitioned into finite bins and one complete
Euler tail. Bin weights multiply an upper kernel at the lower bin edge.
"""
from fractions import Fraction as Q
from flint import arb
from polynomial_tail import add, multiply, scale, kernel_polynomials
from verify_horizon_stitch import as_arb, primes_through, require

TAIL_ORDER=32
TAIL_VMAX=Q(15,16)


def kernel_upper(power, representative, product_cutoff):
    power=Q(power)
    require(1<power<2, 'prime activation power domain')
    require(type(representative) is int and 1<=representative,
            'positive representative product')
    require(Q(9*representative,16*product_cutoff)<=TAIL_VMAX**2,
            'activation bin kernel domain')
    coefficients=[Q(1),-power,power*(power-1)/2]
    for j in range(3,TAIL_ORDER+1):
        coefficients.append(coefficients[-1]*Q(j-1-power,j))
    root=3*arb(representative).sqrt()/4
    polynomial=[as_arb(coefficients[j])*root**j for j in range(TAIL_ORDER)]
    polynomial.append(as_arb(coefficients[TAIL_ORDER]/(1-TAIL_VMAX))*root**TAIL_ORDER)
    return polynomial


def prime_tail_bins(exponent, selected_one, infinite_one, product_cutoff, primes=None):
    B=selected_one.cutoff
    require(B==product_cutoff//2,'selected single-label cap')
    edges=[B,3*product_cutoff//4,product_cutoff,5*product_cutoff//4,
           3*product_cutoff//2]
    primes=primes if primes is not None else primes_through(edges[-1])
    require(primes and primes[-1]<=edges[-1], 'prime bin list domain')
    require(primes==primes_through(edges[-1]),'complete prime bin sieve')
    mass=[arb(0)]*(len(edges)-1)
    position=0
    for q in primes:
        if q<=B:continue
        while q>edges[position+1]:position+=1
        mass[position]+=arb(q)**(-as_arb(exponent))
    tail=infinite_one-selected_one[0]-sum(mass,arb(0))
    require(bool(tail>0),'positive complete remaining prime Euler tail')
    bins=[]
    for edge,value in zip(edges,mass+[tail]):
        upper=value.upper()
        require(upper.is_exact() and bool(upper>0),'directed prime bin mass')
        bins.append((edge,upper))
    return bins


def numerator_polynomial(low,high,low_one,selected_high,infinite_one,product_cutoff,primes=None):
    require(1<low<=high<2,'activation slab domain')
    require(low_one.level==1 and low_one.exponent==(low+1)/2,
            'single-label kernel metadata')
    require(set(selected_high)=={2,4,6},'retained even pair levels')
    removal=infinite_one.upper()
    require(removal.is_exact() and bool(removal<3),'positive even-pair coefficients')
    dl,_=kernel_polynomials(low);dh,dh_upper=kernel_polynomials(high)
    _,odd=kernel_polynomials(low,low_one)
    bins=prime_tail_bins((low+1)/2,low_one,infinite_one,product_cutoff,primes)
    for representative,mass in bins:
        odd=add(odd,scale(kernel_upper(low,representative,product_cutoff),mass))
    positive=[arb(0)]
    for level,vector in selected_high.items():
        require(level in [2,4,6] and vector.ordinary.level==vector.marked.level==level,
                'positive pair selected metadata')
        require(vector.ordinary.cutoff==vector.marked.cutoff==product_cutoff
                and vector.ordinary.exponent==vector.marked.exponent==(high+1)/2,
                'active product cutoff and exponent metadata')
        ordinary,_=kernel_polynomials(high,vector.ordinary)
        marked,_=kernel_polynomials(high,vector.marked)
        positive=add(positive,scale(ordinary,1-removal/(level+1)),
                     scale(marked,arb(1)/(level+1)))
    polynomial=add(multiply(dl,dh),scale(multiply(odd,dh_upper),arb(-1)),
                   multiply(positive,dl))
    return polynomial,{'global_removal_upper':str(removal),
                       'tail_kernel_order':TAIL_ORDER,
                       'tail_kernel_vmax':str(TAIL_VMAX),
                       'prime_tail_bins':[{'lower_edge':edge,'mass_upper':str(mass)}
                                          for edge,mass in bins]}
