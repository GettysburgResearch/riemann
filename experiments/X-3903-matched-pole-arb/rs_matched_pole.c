/*
   Rigorous high-height matched-pole Pick evaluation using FLINT's
   acb_dirichlet_zeta_jet_rs implementation.

   Exact common ordinate:
       T = 20225875608343164356028 * 2^-32
         = 4709203636353.640899999998509883880615234375.

   Exact horizontal nodes:
       x_i = (1,3,10,30,100,300,1000) / 100000.

   The fixed primitive integer vector is the L-3904 matched-pole vector for
   d=9/1000. The program emits primitive outward rectangles and one exact
   real-pick-rayleigh channel consumed by X-3902's standard-library checker.
*/

#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

#define NPOINTS 7

static const ulong X_NUM[NPOINTS] = {1, 3, 10, 30, 100, 300, 1000};
static const char *POINT_ID[NPOINTS] = {
    "matched-x1", "matched-x3", "matched-x10", "matched-x30",
    "matched-x100", "matched-x300", "matched-x1000"
};
static const char *VECTOR[NPOINTS] = {
    "-16539879233914654832354524370000",
    "23515038853801750873712859570000",
    "-7840902633919673843989064577990",
    "888890597261655236548071739110",
    "-23408189640724901265510548343",
    "261023362454990952789561603",
    "-416950807523604621374380"
};
static const char *T_NUM = "20225875608343164356028";

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
mul4(acb_t out, const acb_t a, const acb_t b, const acb_t c,
     const acb_t d, slong prec)
{
    acb_t t;
    acb_init(t);
    acb_mul(t, a, b, prec);
    acb_mul(t, t, c, prec);
    acb_mul(out, t, d, prec);
    acb_clear(t);
}

static void
set_exact_point(acb_t s, ulong x_num, slong prec)
{
    fmpz_t m, e;
    arb_t x, t, half;
    fmpz_init(m);
    fmpz_init(e);
    arb_init(x);
    arb_init(t);
    arb_init(half);

    arb_set_ui(x, x_num);
    arb_div_ui(x, x, 100000, prec);

    if (fmpz_set_str(m, T_NUM, 10) != 0)
    {
        flint_fprintf(stderr, "invalid frozen T numerator\n");
        flint_abort();
    }
    fmpz_set_si(e, -32);
    arb_set_fmpz_2exp(t, m, e);

    arb_one(half);
    arb_mul_2exp_si(half, half, -1);
    arb_add(acb_realref(s), half, x, prec);
    arb_set(acb_imagref(s), t);

    fmpz_clear(m);
    fmpz_clear(e);
    arb_clear(x);
    arb_clear(t);
    arb_clear(half);
}

static int
print_point(const char *identifier, ulong x_num, slong prec, int leading_comma)
{
    int status = 0;
    acb_t s, sm1, halfs, zratio, digamma, f_parts, f_product;
    acb_t A, Aprime, B, Bprime, G, Gprime, xi, xiprime;
    acb_t exponent, term;
    arb_t pi, logpi, half_logpi, abs_zeta, abs_xi, half;
    acb_ptr jet;

    acb_init(s); acb_init(sm1); acb_init(halfs); acb_init(zratio);
    acb_init(digamma); acb_init(f_parts); acb_init(f_product);
    acb_init(A); acb_init(Aprime); acb_init(B); acb_init(Bprime);
    acb_init(G); acb_init(Gprime); acb_init(xi); acb_init(xiprime);
    acb_init(exponent); acb_init(term);
    arb_init(pi); arb_init(logpi); arb_init(half_logpi);
    arb_init(abs_zeta); arb_init(abs_xi); arb_init(half);
    jet = _acb_vec_init(2);

    set_exact_point(s, x_num, prec);
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
    flint_printf("\"x\":{\"numerator\":\"%wu\",\"denominator\":\"100000\"},", x_num);
    flint_printf("\"t\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},", T_NUM);
    flint_printf("\"f_via_xi\":"); print_acb_rectangle(f_product); flint_printf(",");
    flint_printf("\"f_via_parts\":"); print_acb_rectangle(f_parts); flint_printf(",");
    flint_printf("\"zeta_abs_lower\":");
    {
        fmpz_t za, zb, ze;
        fmpz_init(za); fmpz_init(zb); fmpz_init(ze);
        arb_get_interval_fmpz_2exp(za, zb, ze, abs_zeta);
        flint_printf("{\"mantissa\":"); print_fmpz_quoted(za);
        flint_printf(",\"exponent\":"); print_fmpz_quoted(ze); flint_printf("}");
        fmpz_clear(za); fmpz_clear(zb); fmpz_clear(ze);
    }
    flint_printf("}");

cleanup:
    _acb_vec_clear(jet, 2);
    acb_clear(s); acb_clear(sm1); acb_clear(halfs); acb_clear(zratio);
    acb_clear(digamma); acb_clear(f_parts); acb_clear(f_product);
    acb_clear(A); acb_clear(Aprime); acb_clear(B); acb_clear(Bprime);
    acb_clear(G); acb_clear(Gprime); acb_clear(xi); acb_clear(xiprime);
    acb_clear(exponent); acb_clear(term);
    arb_clear(pi); arb_clear(logpi); arb_clear(half_logpi);
    arb_clear(abs_zeta); arb_clear(abs_xi); arb_clear(half);
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
    flint_printf("  \"producer\":{\"backend\":\"FLINT C acb_dirichlet_zeta_jet_rs\",\"precision_bits\":%wd,\"threads\":2,\"assembly_gate\":\"termwise completion intersected with differentiated completed product\"},\n", prec);
    flint_printf("  \"points\":[\n");
    for (i = 0; i < NPOINTS; i++)
    {
        status = print_point(POINT_ID[i], X_NUM[i], prec, i != 0);
        if (status != 0)
            return status;
    }
    flint_printf("\n  ],\n");
    flint_printf("  \"channels\":[{\"id\":\"matched-pole-d9e-3\",\"kind\":\"real-pick-rayleigh\",\"points\":[");
    for (i = 0; i < NPOINTS; i++)
    {
        if (i != 0) flint_printf(",");
        flint_printf("\"%s\"", POINT_ID[i]);
    }
    flint_printf("],\"vector\":[");
    for (i = 0; i < NPOINTS; i++)
    {
        if (i != 0) flint_printf(",");
        flint_printf("{\"numerator\":\"%s\",\"denominator\":\"1\"}", VECTOR[i]);
    }
    flint_printf("]}],\n");
    flint_printf("  \"declared_channel_ids\":[\"matched-pole-d9e-3\"],\n");
    flint_printf("  \"classification\":\"rigorous matched-pole near-null; exact checker decides sign\"\n");
    flint_printf("}\n");
    flint_cleanup();
    return 0;
}
