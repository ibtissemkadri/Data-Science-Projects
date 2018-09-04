import scipy as sp
from scipy import stats
import pylab as plt

n = 50 
x = sp.linspace(-5,5,n)
a,b = 0.8,-4
y = sp.polyval([a,b],x)
yn = y + sp.randn(n)

(ar,br) = sp.polyfit(x,yn,1)
yr = sp.polyval([ar,br],x)

err = sp.sqrt(sum((yr - yn)**2)/n)
print("Linear regression using polyfit")
print("input parameters: a = %.2f b = %.2f" % (a,b))
print("Regression: a=%.2f b=%.2f, ms error= %.3f" % (ar,br,err)) 

plt.title("Linear Regression Example")
plt.plot(x,y,'g--')
plt.plot(x,yn,'k.') 
plt.plot(x,yr,'r-')
plt.legend(['original','plus noise','regression'])
plt.show()

(a_s,b_s,r,xx,stderr) = stats.linregress(x,yn)
print("Linear regression using stats.linregress")
print("parameters: a = %.2f b = %.2f" % (a,b))
print("Regression: a=%.2f b=%.2f, ms error= %.3f" % (a_s,b_s,stderr)) 
