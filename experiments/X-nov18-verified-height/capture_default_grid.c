/* Inspect the FLINT 3.6.0 LP64 default planner in a separate diagnostic process.
   The executable interposes the two grid-construction calls so that only their
   exact inputs are emitted. It exits before any zero calculation. */
#include <stdio.h>
#include <stdlib.h>

extern char *arb_dump_str(const void *);
extern void flint_free(void *);
extern long acb_dirichlet_platt_isolate_local_hardy_z_zeros(
    void *, const long *, long, long);

static char *interp_window;
static long interp_sigma;

void acb_dirichlet_platt_ws_precomp_init(
    void *unused, long resolution, const void *window, long sigma, long precision)
{
    (void)unused; (void)resolution; (void)precision;
    interp_window = arb_dump_str(window);
    interp_sigma = sigma;
}

void acb_dirichlet_platt_multieval(
    void *unused, const long *center, long resolution, long width,
    const void *window, const long *cutoff, long order, long sigma, long precision)
{
    (void)unused;
    if (!interp_window)
        exit(2);
    char *grid_window = arb_dump_str(window);
    printf("%ld\t%ld\t%ld\t%ld\t%ld\t%ld\t%ld\t%ld\t%s\t%s\n",
           *center, resolution, width, *cutoff, order, sigma, interp_sigma,
           precision, grid_window, interp_window);
    flint_free(grid_window);
    flint_free(interp_window);
    exit(0);
}

int main(int argc, char **argv)
{
    if (sizeof(long) != 8 || argc != 3)
        return 2;
    long first = strtol(argv[1], NULL, 10);
    long precision = strtol(argv[2], NULL, 10);
    if (first <= 0 || first >= (1L << 61) || precision < 32 || precision > 1024)
        return 2;
    acb_dirichlet_platt_isolate_local_hardy_z_zeros(NULL, &first, 1, precision);
    return 3;
}
