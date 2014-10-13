# Compute confidence interval for a quantile.
#
# Suppose I'm interested in estimating the 37th percentile.  The
# empirical CDF gives me one estimate for that.  I'd like
# to get a confidence interval: I'm 90% confident that the 37th percentile
# lies between X and Y.
#
# You can compute that with two calls to the following function
# (supposing you're interested in [5%-95%] range) by something like the
# following:
# n = len(sorted_data)
# X_index = CDF_error(n,0.37,0.05)
# Y_index = CDF_error(n,0.37,0.95)
# X=sorted_data[X_index]
# Y=sorted_data[Y_index]
# 90% confidence interval is [X,Y]

from scipy.stats import binom, beta
from scipy import interpolate

# Note: this is the correct (pointwise) distribution
def CDF_error_beta(n,target_quantile,quantile_quantile):
	k=target_quantile*n
	return(beta.ppf(quantile_quantile,k,n+1-k))

# Warning: Bootstrapping fails for 0 and 1 quantile; as
# quantile approaches extremes (generally, within 1/sqrt(n)
# either end of n sample data), things get bad.
def CDF_error_analytic_bootstrap(n,target_quantile,quantile_quantile):
	target_count=int(target_quantile*float(n))

	# Start off with a binary search
	small_ind=0
	big_ind=n-1
	small_prob=1-binom.cdf(target_count,n,0)
	big_prob=1-binom.cdf(target_count,n,float(big_ind)/float(n))

	while big_ind-small_ind>4:
		mid_ind=(big_ind+small_ind)/2
		mid_prob=1-binom.cdf(target_count,n,float(mid_ind)/float(n))
		if mid_prob>quantile_quantile:
			big_prob=mid_prob
			big_ind=mid_ind
		else:
			small_prob=mid_prob
			small_ind=mid_ind    

	# Finish it off with a linear search
	prob_closest=-100
	for p_num in xrange(small_ind,big_ind+1):
		p=float(p_num)/float(n)
		coCDF_prob=1-binom.cdf(target_count,n,p)
		if abs(coCDF_prob-quantile_quantile)<abs(prob_closest-quantile_quantile):
			prob_closest=coCDF_prob
			prob_index=p_num

	return(prob_index)

import matplotlib.pyplot as plt
import numpy as np
# Plot empirical CDF with confidence intervals.
#   num_quantiles=100 means estimate confidence interval at 1%,2%,3%,...,99%.
#   confidence=0.90 mean plot the confidence interval range [5%-95%]
def plot_CDF_confidence(data,num_quantile_regions=100,confidence=0.90,plot_ecdf=True,
	data_already_sorted=False,color='green',label='',alpha=0.3,estimator_name='exact'):
	data=np.array(data)
	if len(np.shape(data))!=1:
		raise NameError('Data must be 1 dimensional!')
	if len(data)<num_quantile_regions:
		num_quantiles=len(data)
	if len(data)<2:
		raise NameError('Need at least 2 data points!')
	if num_quantile_regions<2:
		raise NameError('Need num_quantile_regions > 1 !')
	if not data_already_sorted:
		data=np.sort(data)
	if confidence<=0.0 or confidence>=1.0:
		raise NameError('"confidence" must be between 0.0 and 1.0')
	low_conf=(1.0-confidence)/2.0
	high_conf=1.0-low_conf
	
	quantile_list=np.linspace(1.0/float(num_quantile_regions),1.0-(1.0/float(num_quantile_regions)),num=num_quantile_regions-1)

	low =np.zeros(np.shape(quantile_list))
	high=np.zeros(np.shape(quantile_list))
	emp_quantile_list=np.linspace(1.0/float(len(data)+1),1.0-(1.0/float(len(data)+1)),num=len(data))
	if estimator_name=='exact':
		invCDF_interp=interpolate.interp1d(emp_quantile_list, data)
		CDF_error_function=CDF_error_beta
		for i,q in enumerate(quantile_list):
			low[i] =CDF_error_function(len(data),q, low_conf)
			high[i]=CDF_error_function(len(data),q,high_conf)
		plt.fill_between(invCDF_interp(quantile_list),low,high,alpha=alpha,color=color)		
	elif estimator_name=='analytic bootstrap':
		CDF_error_function=CDF_error_analytic_bootstrap
		for i,q in enumerate(quantile_list):
			low[i] =data[CDF_error_function(len(data),q, low_conf)]
			high[i]=data[CDF_error_function(len(data),q,high_conf)]
		plt.fill_betweenx(quantile_list,low,high,alpha=alpha,color=color)		
	else:
		raise NameError('Unknown error estimator name %s'%(estimator))		

	if plot_ecdf:
		plt.plot(data,emp_quantile_list,label=label,color=color)






