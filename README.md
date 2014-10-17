CDF-confidence
==============

These python tools allow users to compute and/or plot (empirical) CDFs with confidence intervals.
Given a vector "x" of real-valued observations, then to plot the CDF with error bars, you'd run:

    CDF_confidence.plot_CDF_confidence(x)

All the default values should be pretty reasonable; to see what the output looks like, see "sample_CDF.png".


If you'd like to know more about the details, there are several important wrinkles in defining these things.  First, you can either ask "For a given data point, please produce a confidence interval for the corresponding quantile", or "For a particular quantile, produce a confidence interval for the corresponding data points."  We will refer to the first objects as "data confidence intervals" and the second as "quantile confidence intervals".  (If you look at a plot of these across the whole CDF, however, they're visually pretty indistinguishable.)

Second, you can ask for a (pointwise) confidence interval, or a confidence band.  If, for example, you chose a 90% pointwise confidence interval, then you would expect 10% of the true CDF to fall outside of it.  You can see this effect in "sample_CDF.png"-- small stretches of the true CDF lie outside of the confidence intervals.  If you want your entire CDF to fall inside the confidence interval simultaneously, then you can use a confidence band instead.  The cost, of course, is that the confidence band is much thicker.

The code currently offers three choices for estimators:

  (1) A beta distribution: this produces pointwise quantile confidence intervals.  It is exact.

  (2) An analytic bootstrap: this produces pointwise data confidence intervals. By "analytic bootstrap", we mean that we analytically compute the theoretical result of performing an infinite number of bootstrap resamples.  Note, however, that the bootstrap itself is only asymptotically correct.  Moreover, even asymptotically, bootstrapping fails on extreme quantiles (e.g. the distribution of the maximum and minimum can be incorrect even asymptotically.)

  (3) The Dvoretzky–Kiefer–Wolfowitz (DKW) inequality: this produces quantile confidence bands.  The inequality is not tight, but it holds even in the finite sample regime (i.e. not just asymptotically).

Some possible future features:
  (1) Include an option for the error from the (inverse of the) Kolmovorov-Smirnov test

It seems that the Komlós–Major–Tusnády approximation offers a pretty good quantitive
bound (see also the Donsker theorem), although it's not clear that the constants are explicit.

