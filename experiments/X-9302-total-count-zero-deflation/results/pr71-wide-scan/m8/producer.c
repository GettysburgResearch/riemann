/*
   Rigorous direct completed-xi rectangles using FLINT's Riemann--Siegel zeta.

   The producer evaluates nine exact horizontal offsets at the exact common
   dyadic ordinate

       T = 20225875608332518205843 / 2^32.

   It never divides by xi and therefore does not reject a rectangle containing
   zero.  At each point it evaluates xi(s) and xi(1-s) separately and requires
   rectangle overlap before emitting the primitive table.
*/
#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

#define X_COUNT 16
static const int X_BITS[X_COUNT] = {20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5};
static const char *T_MANTISSA = "20225875608332518205843";
static const slong XI_COMMON_SCALE_POWER = 5335951715288L;

static void
print_fmpz_unquoted(const fmpz_t x)
{
    fmpz_print(x);
}

static void
print_rational_fmpz_2exp(const fmpz_t mantissa, const fmpz_t exponent)
{
    fmpz_t numerator, denominator;
    slong e;
    fmpz_init(numerator);
    fmpz_init(denominator);
    fmpz_set(numerator, mantissa);
    fmpz_one(denominator);
    if (!fmpz_fits_si(exponent))
    {
        flint_fprintf(stderr, "binary exponent does not fit slong\n");
        abort();
    }
    e = fmpz_get_si(exponent);
    if (e >= 0)
        fmpz_mul_2exp(numerator, numerator, (ulong)e);
    else
        fmpz_mul_2exp(denominator, denominator, (ulong)(-e));
    flint_printf("{\"numerator\":");
    print_fmpz_unquoted(numerator);
    flint_printf(",\"denominator\":");
    print_fmpz_unquoted(denominator);
    flint_printf("}");
    fmpz_clear(numerator);
    fmpz_clear(denominator);
}

static void
print_arb_rational_interval(const arb_t x)
{
    fmpz_t a, b, e;
    fmpz_init(a);
    fmpz_init(b);
    fmpz_init(e);
    arb_get_interval_fmpz_2exp(a, b, e, x);
    flint_printf("{\"lower\":");
    print_rational_fmpz_2exp(a, e);
    flint_printf(",\"upper\":");
    print_rational_fmpz_2exp(b, e);
    flint_printf("}");
    fmpz_clear(a);
    fmpz_clear(b);
    fmpz_clear(e);
}

static void
print_acb_rational_rectangle(const acb_t z)
{
    flint_printf("{\"real\":");
    print_arb_rational_interval(acb_realref(z));
    flint_printf(",\"imag\":");
    print_arb_rational_interval(acb_imagref(z));
    flint_printf("}");
}

static void
set_exact_point(acb_t s, int xbits)
{
    fmpz_t tnum, texp;
    arb_t x, t, half;
    fmpz_init(tnum);
    fmpz_init(texp);
    arb_init(x);
    arb_init(t);
    arb_init(half);

    arb_one(x);
    arb_mul_2exp_si(x, x, -xbits);
    fmpz_set_str(tnum, T_MANTISSA, 10);
    fmpz_set_si(texp, -32);
    arb_set_fmpz_2exp(t, tnum, texp);
    arb_one(half);
    arb_mul_2exp_si(half, half, -1);
    arb_add(acb_realref(s), half, x, ARF_PREC_EXACT);
    arb_set(acb_imagref(s), t);

    fmpz_clear(tnum);
    fmpz_clear(texp);
    arb_clear(x);
    arb_clear(t);
    arb_clear(half);
}

static void
mul4(acb_t out, const acb_t a, const acb_t b, const acb_t c,
     const acb_t d, slong prec)
{
    acb_t tmp;
    acb_init(tmp);
    acb_mul(tmp, a, b, prec);
    acb_mul(tmp, tmp, c, prec);
    acb_mul(out, tmp, d, prec);
    acb_clear(tmp);
}

static void
evaluate_xi(acb_t xi, const acb_t s, slong prec)
{
    acb_t sm1, halfs, A, B, G, exponent;
    arb_t pi, logpi, half_logpi;
    acb_ptr jet;

    acb_init(sm1);
    acb_init(halfs);
    acb_init(A);
    acb_init(B);
    acb_init(G);
    acb_init(exponent);
    arb_init(pi);
    arb_init(logpi);
    arb_init(half_logpi);
    jet = _acb_vec_init(1);

    acb_dirichlet_zeta_jet_rs(jet, s, 1, prec);
    arb_const_pi(pi, prec);
    arb_log(logpi, pi, prec);
    arb_mul_2exp_si(half_logpi, logpi, -1);

    acb_sub_ui(sm1, s, 1, prec);
    acb_mul_2exp_si(halfs, s, -1);
    acb_mul(A, s, sm1, prec);
    acb_mul_2exp_si(A, A, -1);
    acb_mul_arb(exponent, s, half_logpi, prec);
    acb_neg(exponent, exponent);
    acb_exp(B, exponent, prec);
    acb_gamma(G, halfs, prec);
    mul4(xi, A, B, G, jet + 0, prec);
    acb_mul_2exp_si(xi, xi, XI_COMMON_SCALE_POWER);

    _acb_vec_clear(jet, 1);
    acb_clear(sm1);
    acb_clear(halfs);
    acb_clear(A);
    acb_clear(B);
    acb_clear(G);
    acb_clear(exponent);
    arb_clear(pi);
    arb_clear(logpi);
    arb_clear(half_logpi);
}

static void
print_point(int xbits, slong prec, int *first)
{
    acb_t s, reflected_s, xi, reflected_xi, residual;
    fmpz_t tnum;
    ulong denominator = UWORD(1) << xbits;

    acb_init(s);
    acb_init(reflected_s);
    acb_init(xi);
    acb_init(reflected_xi);
    acb_init(residual);
    fmpz_init(tnum);

    set_exact_point(s, xbits);
    /*
       Evaluate xi(1-s) without sending a negative ordinate to the
       Riemann--Siegel backend.  For r = 1-conj(s),

           conj(xi(r)) = xi(1-s),

       by conjugation symmetry.  This preserves the emitted functional-
       equation rectangle while both RS evaluations stay at positive height.
    */
    acb_conj(reflected_s, s);
    acb_neg(reflected_s, reflected_s);
    acb_add_ui(reflected_s, reflected_s, 1, prec);
    evaluate_xi(xi, s, prec);
    evaluate_xi(reflected_xi, reflected_s, prec);
    acb_conj(reflected_xi, reflected_xi);
    if (!acb_overlaps(xi, reflected_xi))
    {
        flint_fprintf(stderr, "functional-equation rectangles do not overlap at xbits=%d\n", xbits);
        exit(3);
    }
    acb_sub(residual, xi, reflected_xi, prec);
    if (!acb_contains_zero(residual))
    {
        flint_fprintf(stderr, "functional-equation residual misses zero at xbits=%d\n", xbits);
        exit(4);
    }

    if (!*first)
        flint_printf(",\n");
    *first = 0;
    flint_printf("{\"id\":\"x-%d\",", xbits);
    flint_printf("\"x\":{\"numerator\":1,\"denominator\":%wu},", denominator);
    flint_printf("\"xi_rectangle\":");
    print_acb_rational_rectangle(xi);
    flint_printf(",\"functional_equation_reflected_rectangle\":");
    print_acb_rational_rectangle(reflected_xi);
    flint_printf(",\"functional_equation_residual_contains_zero\":true,");
    flint_printf("\"relative_accuracy_bits\":{\"xi_direct\":%wd,\"xi_reflected\":%wd}}",
                 acb_rel_accuracy_bits(xi), acb_rel_accuracy_bits(reflected_xi));

    fmpz_clear(tnum);
    acb_clear(s);
    acb_clear(reflected_s);
    acb_clear(xi);
    acb_clear(reflected_xi);
    acb_clear(residual);
}

int
main(int argc, char **argv)
{
    slong prec;
    int first = 1;
    int i;

    if (argc != 2)
    {
        flint_fprintf(stderr, "usage: %s precision_bits\n", argv[0]);
        return 2;
    }
    prec = atol(argv[1]);
    if (prec < 64)
    {
        flint_fprintf(stderr, "precision must be at least 64 bits\n");
        return 2;
    }

    flint_printf("{\n");
    flint_printf("\"schema\":\"riemann.xi-modulus-primitives.v1\",\n");
    flint_printf("\"normalization_id\":\"riemann-xi-standard-half-s-sminus1-v1\",\n");
    flint_printf("\"precision_bits\":%wd,\n", prec);
    flint_printf("\"common_xi_scale_power_of_two\":%wd,\n", XI_COMMON_SCALE_POWER);
    flint_printf("\"ordinate\":{\"numerator\":20225875608332518205843,\"denominator\":4294967296},\n");
    flint_printf("\"backend\":\"FLINT acb_dirichlet_zeta_jet_rs plus direct completed-xi product\",\n");
    flint_printf("\"points\":[\n");
    for (i = 0; i < X_COUNT; i++)
        print_point(X_BITS[i], prec, &first);
    flint_printf("\n]\n}\n");
    flint_cleanup();
    return 0;
}
