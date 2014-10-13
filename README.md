CDF-confidence
==============

These python tools allow users to compute and/or plot (empirical) CDFs with confidence intervals.

The code currently offers two choices for *pointwise* confidence intervals for CDFs:
  (1) A beta distribution (which is exact, so you should use it), and
  (2) An analytic bootstrap (i.e. an exact computation of the bootstrap, but the bootstrap is inexact; moreover, even in the limit, bootstrapping fails on extreme quantiles.)

In the future, we will add support for *function-wise* confidence intervals for CDFs (a.k.a. "confidence bands"). To do:
  (1) Include an option to use the Dvoretzky-Kiefer-Wolfowitz inequality
  (2) Include an option for the error from the (inverse of the) Kolmovorov-Smirnov test

It seems that the Komlós–Major–Tusnády approximation offers a pretty good quantitive
bound (see also the Donsker theorem), although it's not clear that the constants are explicit.

