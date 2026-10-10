#!/usr/bin/env python3
"""Whole-tail polynomial for marked even/odd removal pairs."""
from fractions import Fraction as Q
from flint import arb
from polynomial_tail import add, multiply, scale, kernel_polynomials
from verify_horizon_stitch import require


def numerator_polynomial(low: Q, high: Q, low_one, selected_high, infinite_one):
    require(1 < low <= high < 2, 'exclusion tail power domain')
    require(low_one.level == 1, 'odd single-label metadata')
    require(set(selected_high) == {2, 4, 6}, 'retained exclusion pair levels')
    caps = {vector.ordinary.cutoff for vector in selected_high.values()}
    require(len(caps) == 1 and low_one.cutoff <= next(iter(caps)),
            'common retained product cap')
    for level, vector in selected_high.items():
        require(vector.ordinary.level == vector.marked.level == level
                and vector.ordinary.cutoff == vector.marked.cutoff
                and vector.ordinary.exponent == vector.marked.exponent,
                'ordinary and marked metadata agree')
    removal = infinite_one.upper()
    tail = (infinite_one-low_one[0]).upper()
    require(removal.is_exact() and bool(removal < 3), 'positive first-pair coefficient')
    require(tail.is_exact() and bool(tail > 0), 'directed omitted prime mass')
    constant = 1-tail
    require(bool(constant > 0), 'positive denominator substitution constant')
    dl, _ = kernel_polynomials(low)
    dh, dh_upper = kernel_polynomials(high)
    _, odd = kernel_polynomials(low, low_one)
    positive = [arb(0)]
    coefficients = {}
    for level, vector in selected_high.items():
        coefficient = 1-removal/(level+1)
        require(bool(coefficient > 0), 'positive retained pair coefficient')
        even, _ = kernel_polynomials(high, vector.ordinary)
        marked, _ = kernel_polynomials(high, vector.marked)
        positive = add(positive, scale(even, coefficient),
                       scale(marked, arb(1)/(level+1)))
        coefficients[str(level)] = str(coefficient)
    numerator = add(scale(multiply(dl, dh), constant),
                    scale(multiply(odd, dh_upper), arb(-1)),
                    multiply(positive, dl))
    return numerator, {'global_removal_upper': str(removal),
                       'omitted_one_label_upper': str(tail),
                       'denominator_constant': str(constant),
                       'positive_pair_coefficients': coefficients}


def certify_positive_tail(polynomial, product_cutoff, max_depth=14):
    """Use a 40-bit dyadic outward cap so every bounded-depth midpoint is exact."""
    from polynomial_tail import bernstein_coefficients
    require(type(product_cutoff) is int and product_cutoff >= 4, 'tail cutoff domain')
    cap = (1/arb(product_cutoff).sqrt()).upper()
    integer = (cap*2**40).ceil().unique_fmpz()
    require(integer is not None, 'unique integer for dyadic tail cap')
    upper = arb(integer)/2**40
    require(upper.is_exact() and bool(upper >= cap) and bool(upper < 1),
            'exact outward dyadic tail cap')
    pending=[(arb(0),upper,0)];leaves=[]
    while pending:
        left,right,depth=pending.pop()
        coefficients=bernstein_coefficients(polynomial,left,right)
        if all(bool(c > 0) for c in coefficients):
            minimum=coefficients[0].lower()
            for c in coefficients[1:]:
                value=c.lower()
                require(value.is_exact(),'directed exact reported endpoint')
                if bool(value < minimum):minimum=value
            leaves.append({'z_interval':[str(left),str(right)],'depth':depth,
                'positive_bernstein_lower_scale':str(minimum),
                'all_entire_bernstein_balls_positive':True})
            continue
        require(depth < max_depth and len(pending)+len(leaves)<1024,
                'Bernstein subdivision did not certify exclusion tail')
        middle=(left+right)/2
        require(middle.is_exact(),'exact dyadic tail subdivision midpoint')
        pending.extend([(middle,right,depth+1),(left,middle,depth+1)])
    return {'polynomial_degree':len(polynomial)-1,'z_domain':['0',str(upper)],
        'tail_endpoint_interval':[product_cutoff,'infinity'],
        'cap_dyadic_denominator_power':40,'bernstein_leaf_count':len(leaves),'leaves':leaves,
        'entire_unbounded_tail_certified':True}
