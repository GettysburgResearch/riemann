/*
   Rigorous value-only xi'/xi grid using FLINT's Riemann--Siegel zeta jet.

   Grid:
     T_j = T0 + j/32,  -32 <= j <= 32,
     T0  = 20225875608343121406355 / 2^32,
     x   in {2^-17,2^-15,2^-13,2^-11,2^-10,2^-9,2^-7,2^-5}.

   Every point is exact. For each point we emit two rigorous assemblies of
   F=xi'/xi and a positive lower bound for |zeta|. The Python exact checker
   reconstructs scalar, adjacent A/B, second divided differences, and fixed
   [1,-1] Pick contractions.
*/

#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

#define T_MIN (-32)
#define T_MAX 32
#define X_COUNT 8

static const int X_BITS[X_COUNT] = {17, 15, 13, 11, 10, 9, 7, 5};
static const char *T0_MANTISSA = "20225875608343121406355";

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
point_id(char *buffer, size_t size, int tj, int xbits)
{
    snprintf(buffer, size, "t_%s%d_x%d", tj < 0 ? "m" : "p", abs(tj), xbits);
}

static void
set_exact_point(acb_t s, int tj, int xbits)
{
    fmpz_t tnum, texp, increment;
    arb_t x, t, half;
    fmpz_init(tnum);
    fmpz_init(texp);
    fmpz_init(increment);
    arb_init(x);
    arb_init(t);
    arb_init(half);

    arb_one(x);
    arb_mul_2exp_si(x, x, -xbits);

    fmpz_set_str(tnum, T0_MANTISSA, 10);
    /* j/32 = j * 2^27 / 2^32. */
    fmpz_set_si(increment, tj);
    fmpz_mul_2exp(increment, increment, 27);
    fmpz_add(tnum, tnum, increment);
    fmpz_set_si(texp, -32);
    arb_set_fmpz_2exp(t, tnum, texp);

    arb_one(half);
    arb_mul_2exp_si(half, half, -1);
    arb_add(acb_realref(s), half, x, ARF_PREC_EXACT);
    arb_set(acb_imagref(s), t);

    fmpz_clear(tnum);
    fmpz_clear(texp);
    fmpz_clear(increment);
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
evaluate_f(acb_t f_product, acb_t f_parts, arb_t abs_zeta,
           const acb_t s, slong prec)
{
    acb_t sm1, halfs, zratio, digamma;
    acb_t A, Aprime, B, Bprime, G, Gprime, xi, xiprime;
    acb_t exponent, term;
    arb_t pi, logpi, half_logpi, abs_xi, half;
    acb_ptr jet;
    int status = 0;

    acb_init(sm1);
    acb_init(halfs);
    acb_init(zratio);
    acb_init(digamma);
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
    arb_init(abs_xi);
    arb_init(half);
    jet = _acb_vec_init(2);

    acb_dirichlet_zeta_jet_rs(jet, s, 2, prec);
    acb_abs(abs_zeta, jet + 0, prec);
    if (!arb_is_positive(abs_zeta))
    {
        status = 1;
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
        status = 2;
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
        status = 3;

cleanup:
    _acb_vec_clear(jet, 2);
    acb_clear(sm1);
    acb_clear(halfs);
    acb_clear(zratio);
    acb_clear(digamma);
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
    arb_clear(abs_xi);
    arb_clear(half);
    return status;
}

static void
print_point(int tj, int xbits, slong prec, int *first)
{
    acb_t s, f_product, f_parts;
    arb_t abs_zeta;
    fmpz_t tnum, increment;
    char id[64];
    int status;
    ulong denominator = UWORD(1) << xbits;

    acb_init(s);
    acb_init(f_product);
    acb_init(f_parts);
    arb_init(abs_zeta);
    fmpz_init(tnum);
    fmpz_init(increment);
    set_exact_point(s, tj, xbits);
    status = evaluate_f(f_product, f_parts, abs_zeta, s, prec);
    if (status != 0)
    {
        flint_fprintf(stderr, "point evaluation failed at j=%d xbits=%d code=%d\n",
                      tj, xbits, status);
        exit(3 + status);
    }

    fmpz_set_str(tnum, T0_MANTISSA, 10);
    fmpz_set_si(increment, tj);
    fmpz_mul_2exp(increment, increment, 27);
    fmpz_add(tnum, tnum, increment);
    point_id(id, sizeof(id), tj, xbits);

    if (!*first)
        flint_printf(",\n");
    *first = 0;
    flint_printf("{\"id\":\"%s\",", id);
    flint_printf("\"x\":{\"numerator\":\"1\",\"denominator\":\"%wu\"},", denominator);
    flint_printf("\"t\":{\"numerator\":");
    print_fmpz_quoted(tnum);
    flint_printf(",\"denominator\":\"4294967296\"},");
    flint_printf("\"f_via_xi\":");
    print_acb_rectangle(f_product);
    flint_printf(",\"f_via_parts\":");
    print_acb_rectangle(f_parts);
    flint_printf(",\"zeta_abs_lower\":");
    {
        fmpz_t a, b, e;
        fmpz_init(a);
        fmpz_init(b);
        fmpz_init(e);
        arb_get_interval_fmpz_2exp(a, b, e, abs_zeta);
        flint_printf("{\"mantissa\":");
        print_fmpz_quoted(a);
        flint_printf(",\"exponent\":");
        print_fmpz_quoted(e);
        flint_printf("}");
        fmpz_clear(a);
        fmpz_clear(b);
        fmpz_clear(e);
    }
    flint_printf("}");

    acb_clear(s);
    acb_clear(f_product);
    acb_clear(f_parts);
    arb_clear(abs_zeta);
    fmpz_clear(tnum);
    fmpz_clear(increment);
}

static void
print_fraction_one(void)
{
    flint_printf("{\"numerator\":\"1\",\"denominator\":\"1\"}");
}

static void
print_fraction_minus_one(void)
{
    flint_printf("{\"numerator\":\"-1\",\"denominator\":\"1\"}");
}

static void
channel_separator(int *first)
{
    if (!*first)
        flint_printf(",\n");
    *first = 0;
}

static void
print_pair_channel(int declared_only, int *first, const char *tag,
                   const char *kind, const char *a, const char *b)
{
    channel_separator(first);
    if (declared_only)
        flint_printf("\"%s_%s_%s\"", tag, a, b);
    else
        flint_printf("{\"id\":\"%s_%s_%s\",\"kind\":\"%s\",\"points\":[\"%s\",\"%s\"]}",
                     tag, a, b, kind, a, b);
}

static void
print_channels(int declared_only)
{
    int tj, k, first = 1;
    char a[64], b[64], c[64];

    for (tj = T_MIN; tj <= T_MAX; tj++)
    {
        for (k = 0; k < X_COUNT; k++)
        {
            point_id(a, sizeof(a), tj, X_BITS[k]);
            channel_separator(&first);
            if (declared_only)
                flint_printf("\"scalar_%s\"", a);
            else
                flint_printf("{\"id\":\"scalar_%s\",\"kind\":\"scalar\",\"point\":\"%s\"}", a, a);
        }

        for (k = 0; k + 1 < X_COUNT; k++)
        {
            point_id(a, sizeof(a), tj, X_BITS[k]);
            point_id(b, sizeof(b), tj, X_BITS[k + 1]);
            print_pair_channel(declared_only, &first, "A", "two-channel-A", a, b);
            print_pair_channel(declared_only, &first, "B", "two-channel-B", a, b);

            channel_separator(&first);
            if (declared_only)
                flint_printf("\"pick_%s_%s\"", a, b);
            else
            {
                flint_printf("{\"id\":\"pick_%s_%s\",\"kind\":\"real-pick-rayleigh\",\"points\":[\"%s\",\"%s\"],\"vector\":[",
                             a, b, a, b);
                print_fraction_one();
                flint_printf(",");
                print_fraction_minus_one();
                flint_printf("]}");
            }
        }

        for (k = 0; k + 2 < X_COUNT; k++)
        {
            point_id(a, sizeof(a), tj, X_BITS[k]);
            point_id(b, sizeof(b), tj, X_BITS[k + 1]);
            point_id(c, sizeof(c), tj, X_BITS[k + 2]);
            channel_separator(&first);
            if (declared_only)
                flint_printf("\"dd2_%s_%s_%s\"", a, b, c);
            else
                flint_printf("{\"id\":\"dd2_%s_%s_%s\",\"kind\":\"bernstein-divided-difference\",\"points\":[\"%s\",\"%s\",\"%s\"]}",
                             a, b, c, a, b, c);
        }
    }
}

int
main(int argc, char *argv[])
{
    slong prec = 128;
    int tj, k, first = 1;
    if (argc >= 2)
        prec = atol(argv[1]);
    if (prec < 64)
        return 2;
    flint_set_num_threads(2);

    flint_printf("{\n\"schema\":\"riemann.xi-passivity-value-balls.v1\",\n");
    flint_printf("\"producer\":{\"backend\":\"FLINT C acb_dirichlet_zeta_jet_rs grid\",\"precision_bits\":%wd,\"threads\":2,\"t_offsets\":\"j/32,-32<=j<=32\",\"x_bits\":[17,15,13,11,10,9,7,5]},\n", prec);
    flint_printf("\"points\":[\n");
    for (tj = T_MIN; tj <= T_MAX; tj++)
        for (k = 0; k < X_COUNT; k++)
            print_point(tj, X_BITS[k], prec, &first);

    flint_printf("\n],\n\"channels\":[\n");
    print_channels(0);
    flint_printf("\n],\n\"declared_channel_ids\":[\n");
    print_channels(1);
    flint_printf("\n],\n\"classification\":\"rigorous finite high-carrier search grid; exact checker decides all signs\"\n}\n");
    flint_cleanup();
    return 0;
}
