/*
   Precision-escalating rigorous Pick-Rayleigh evaluation for one frozen exact
   direction nominated by the X-3902 128-bit grid.

   Exact ordinate:
       T = 20225875608342450317715 * 2^-32
         = grid center - 5/32.

   Exact horizontal nodes:
       x = 2^-17, 2^-15, 2^-13, 2^-11, 2^-10, 2^-9, 2^-7, 2^-5.

   The integer vector was rounded once from a high-precision midpoint eigensolve
   and frozen before this directed evaluation.  Only the exact checker decides
   the sign.  This file does not itself claim a counterexample.
*/

#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

#define NPOINTS 8

static const int X_BITS[NPOINTS] = {17, 15, 13, 11, 10, 9, 7, 5};
static const char *POINT_ID[NPOINTS] = {
    "candidate-x17", "candidate-x15", "candidate-x13", "candidate-x11",
    "candidate-x10", "candidate-x9", "candidate-x7", "candidate-x5"
};
static const char *VECTOR[NPOINTS] = {
    "195636939617757491029673815477592416810",
    "-266959021123812027267480589292220211689",
    "78579210599617390707865222434596218607",
    "-8625978245797521833136016688956110884",
    "1433229629677485490048250862719075773",
    "-64409641812112416364060934853368983",
    "29166190362703029401659745864134",
    "-1821068355102116775346559903"
};
static const char *T_NUM = "20225875608342450317715";

static void
print_fmpz_quoted(const fmpz_t x)
{
    flint_printf("\"");
    fmpz_print(x);
    flint_printf("\"");
}

static void
print_arb_interval(const arb_t x)
{
    fmpz_t a, b, e;
    fmpz_init(a);
    fmpz_init(b);
    fmpz_init(e);
    arb_get_interval_fmpz_2exp(a, b, e, x);
    flint_printf("{\"lower\":{\"mantissa\":");
    print_fmpz_quoted(a);
    flint_printf(",\"exponent\":");
    print_fmpz_quoted(e);
    flint_printf("},\"upper\":{\"mantissa\":");
    print_fmpz_quoted(b);
    flint_printf(",\"exponent\":");
    print_fmpz_quoted(e);
    flint_printf("}}");
    fmpz_clear(a);
    fmpz_clear(b);
    fmpz_clear(e);
}

static void
print_acb_rectangle(const acb_t z)
{
    flint_printf("{\"real\":");
    print_arb_interval(acb_realref(z));
    flint_printf(",\"imag\":");
    print_arb_interval(acb_imagref(z));
    flint_printf("}");
}

static void
set_exact_point(acb_t s, int xbits)
{
    fmpz_t m, e;
    arb_t x, t, half;
    fmpz_init(m);
    fmpz_init(e);
    arb_init(x);
    arb_init(t);
    arb_init(half);

    arb_one(x);
    arb_mul_2exp_si(x, x, -xbits);

    if (fmpz_set_str(m, T_NUM, 10) != 0)
    {
        flint_fprintf(stderr, "invalid frozen T numerator\n");
        flint_abort();
    }
    fmpz_set_si(e, -32);
    arb_set_fmpz_2exp(t, m, e);

    arb_one(half);
    arb_mul_2exp_si(half, half, -1);
    arb_add(acb_realref(s), half, x, ARF_PREC_EXACT);
    arb_set(acb_imagref(s), t);

    fmpz_clear(m);
    fmpz_clear(e);
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

static int
print_point(const char *identifier, int xbits, slong prec, int leading_comma)
{
    int status = 0;
    acb_t s, sm1, halfs, zratio, digamma, f_parts, f_product;
    acb_t A, Aprime, B, Bprime, G, Gprime, xi, xiprime;
    acb_t exponent, term;
    arb_t pi, logpi, half_logpi, abs_zeta, abs_xi, half;
    acb_ptr jet;
    ulong denominator = UWORD(1) << xbits;

    acb_init(s);
    acb_init(sm1);
    acb_init(halfs);
    acb_init(zratio);
    acb_init(digamma);
    acb_init(f_parts);
    acb_init(f_product);
    acb_init(A);
    acb_init(Aprime);
    acb_init(B);
    acb_init(Bprime);
    acb_init(G);
    acb_init(Gprime);
    acb_init(xi);
    acb_init(xiprime);
    acb_init(exponent);
    acb_init(term);
    arb_init(pi);
    arb_init(logpi);
    arb_init(half_logpi);
    arb_init(abs_zeta);
    arb_init(abs_xi);
    arb_init(half);
    jet = _acb_vec_init(2);

    set_exact_point(s, xbits);
    acb_dirichlet_zeta_jet_rs(jet, s, 2, prec);
    acb_abs(abs_zeta, jet + 0, prec);
    if (!arb_is_positive(abs_zeta))
    {
        flint_fprintf(stderr, "%s: zeta ball contains zero\n", identifier);
        status = 3;
        goto cleanup;
    }

    arb_const_pi(pi, prec);
    arb_log(logpi, pi, prec);
    arb_mul_2exp_si(half_logpi, logpi, -1);
    arb_one(half);
    arb_mul_2exp_si(half, half, -1);

    acb_sub_ui(sm1, s, 1, prec);
    acb_mul_2exp_si(halfs, s, -1);
    acb_digamma(digamma, halfs, prec);
    acb_mul_2exp_si(digamma, digamma, -1);
    acb_div(zratio, jet + 1, jet + 0, prec);

    acb_inv(f_parts, s, prec);
    acb_inv(term, sm1, prec);
    acb_add(f_parts, f_parts, term, prec);
    acb_sub_arb(f_parts, f_parts, half_logpi, prec);
    acb_add(f_parts, f_parts, digamma, prec);
    acb_add(f_parts, f_parts, zratio, prec);

    acb_mul(A, s, sm1, prec);
    acb_mul_2exp_si(A, A, -1);
    acb_sub_arb(Aprime, s, half, prec);
    acb_mul_arb(exponent, s, half_logpi, prec);
    acb_neg(exponent, exponent);
    acb_exp(B, exponent, prec);
    acb_mul_arb(Bprime, B, half_logpi, prec);
    acb_neg(Bprime, Bprime);
    acb_gamma(G, halfs, prec);
    acb_mul(Gprime, digamma, G, prec);

    mul4(xi, A, B, G, jet + 0, prec);
    acb_abs(abs_xi, xi, prec);
    if (!arb_is_positive(abs_xi))
    {
        flint_fprintf(stderr, "%s: completed xi ball contains zero\n", identifier);
        status = 4;
        goto cleanup;
    }

    mul4(xiprime, Aprime, B, G, jet + 0, prec);
    mul4(term, A, Bprime, G, jet + 0, prec);
    acb_add(xiprime, xiprime, term, prec);
    mul4(term, A, B, Gprime, jet + 0, prec);
    acb_add(xiprime, xiprime, term, prec);
    mul4(term, A, B, G, jet + 1, prec);
    acb_add(xiprime, xiprime, term, prec);
    acb_div(f_product, xiprime, xi, prec);

    if (!acb_overlaps(f_parts, f_product))
    {
        flint_fprintf(stderr, "%s: two assemblies are disjoint\n", identifier);
        status = 5;
        goto cleanup;
    }

    if (leading_comma)
        flint_printf(",\n");
    flint_printf("    {\"id\":\"%s\",", identifier);
    flint_printf("\"x\":{\"numerator\":\"1\",\"denominator\":\"%wu\"},", denominator);
    flint_printf("\"t\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},", T_NUM);
    flint_printf("\"f_via_xi\":");
    print_acb_rectangle(f_product);
    flint_printf(",\"f_via_parts\":");
    print_acb_rectangle(f_parts);
    flint_printf(",\"zeta_abs_lower\":");
    {
        fmpz_t za, zb, ze;
        fmpz_init(za);
        fmpz_init(zb);
        fmpz_init(ze);
        arb_get_interval_fmpz_2exp(za, zb, ze, abs_zeta);
        flint_printf("{\"mantissa\":");
        print_fmpz_quoted(za);
        flint_printf(",\"exponent\":");
        print_fmpz_quoted(ze);
        flint_printf("}");
        fmpz_clear(za);
        fmpz_clear(zb);
        fmpz_clear(ze);
    }
    flint_printf("}");

cleanup:
    _acb_vec_clear(jet, 2);
    acb_clear(s);
    acb_clear(sm1);
    acb_clear(halfs);
    acb_clear(zratio);
    acb_clear(digamma);
    acb_clear(f_parts);
    acb_clear(f_product);
    acb_clear(A);
    acb_clear(Aprime);
    acb_clear(B);
    acb_clear(Bprime);
    acb_clear(G);
    acb_clear(Gprime);
    acb_clear(xi);
    acb_clear(xiprime);
    acb_clear(exponent);
    acb_clear(term);
    arb_clear(pi);
    arb_clear(logpi);
    arb_clear(half_logpi);
    arb_clear(abs_zeta);
    arb_clear(abs_xi);
    arb_clear(half);
    return status;
}

int
main(int argc, char *argv[])
{
    slong prec = 384;
    int i, status;
    if (argc >= 2)
        prec = atol(argv[1]);
    if (prec < 128)
    {
        flint_fprintf(stderr, "precision must be at least 128 bits\n");
        return 2;
    }

    flint_set_num_threads(2);
    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.xi-passivity-value-balls.v1\",\n");
    flint_printf("  \"producer\":{\"backend\":\"FLINT C acb_dirichlet_zeta_jet_rs\",\"precision_bits\":%wd,\"threads\":2,\"assembly_gate\":\"termwise completion intersected with differentiated completed product\",\"discovery_boundary\":\"vector frozen before directed evaluation\"},\n", prec);
    flint_printf("  \"points\":[\n");
    for (i = 0; i < NPOINTS; i++)
    {
        status = print_point(POINT_ID[i], X_BITS[i], prec, i != 0);
        if (status != 0)
            return status;
    }
    flint_printf("\n  ],\n");
    flint_printf("  \"channels\":[{\"id\":\"frozen-grid-pick-candidate\",\"kind\":\"real-pick-rayleigh\",\"points\":[");
    for (i = 0; i < NPOINTS; i++)
    {
        if (i != 0)
            flint_printf(",");
        flint_printf("\"%s\"", POINT_ID[i]);
    }
    flint_printf("],\"vector\":[");
    for (i = 0; i < NPOINTS; i++)
    {
        if (i != 0)
            flint_printf(",");
        flint_printf("{\"numerator\":\"%s\",\"denominator\":\"1\"}", VECTOR[i]);
    }
    flint_printf("]}],\n");
    flint_printf("  \"declared_channel_ids\":[\"frozen-grid-pick-candidate\"],\n");
    flint_printf("  \"classification\":\"precision escalation of a frozen exact near-null Pick direction; exact checker decides sign\"\n");
    flint_printf("}\n");
    flint_cleanup();
    return 0;
}
