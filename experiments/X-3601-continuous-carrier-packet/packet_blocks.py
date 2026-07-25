#!/usr/bin/env python3
"""Public validation interface for X-3601.

The implementation is split so the shifted-Legendre recurrence and the
continuous sinc formulas can be reviewed independently.
"""
from legendre_kernel import basis_value as legendre_basis_value
from legendre_kernel import carrier_kernel, legendre_values, overlap_matrix
from off_lattice import arch_entry as off_lattice_arch_entry
from off_lattice import box_sinc
from off_lattice import correct_dimensionless_prime_kernel
from off_lattice import frequency_kernel as off_lattice_frequency_kernel
from off_lattice import gram as off_lattice_gram
from off_lattice import naive_fractional_divided_difference
from off_lattice import pole_entry as off_lattice_pole_entry
from off_lattice import sinc

__all__ = [
    "box_sinc",
    "carrier_kernel",
    "correct_dimensionless_prime_kernel",
    "legendre_basis_value",
    "legendre_values",
    "naive_fractional_divided_difference",
    "off_lattice_arch_entry",
    "off_lattice_frequency_kernel",
    "off_lattice_gram",
    "off_lattice_pole_entry",
    "overlap_matrix",
    "sinc",
]
