# word = input("Please input your word here: \n")
word = r'''
     \mathrm{d} u_{1}(t)=&\left(u_{1}(t)+A\right)\left(\frac{b\left(u_{2}(t)+B\right)}{u_{1}(t)+A}-\frac{b B}{A}-c_{1} u_{1}(t)-\alpha_{1} v(t)-\lambda_{1} w(t)\right) \mathrm{d} t \\
     &-\left(u_{1}(t)+A\right) \sigma_{1} w(t) \mathrm{d} B_{1}(t) , \\
      \mathrm{d}u_{2}(t)=&\left(u_{2}(t)+B\right)\left(\frac{\gamma\left(u_{1}(t)+A\right)}{u_{2}(t)+B}-\frac{\gamma A}{B}-c_{2} u_{2}(t)-\alpha_{2} v(t)-\frac{\lambda_{2} w^{p}(t)}{1+\beta w^{q}(t)}\right) \mathrm{d} t \\
     &-\left(u_{2}(t)+B\right) \frac{\sigma_{2} w^{p}(t)}{1+\beta w^{q}(t)} \mathrm{d} B_{2}(t) \\ \mathrm{d} v(t)=&[k u(t)-(g+m+b) v(t)] \mathrm{d} t , \\
     \mathrm{d} w(t)=&\left[u_{e}(t)-h w(t)\right] \mathrm{d} t .
'''

old_strs = [
    '(t)','\\left(x, y, C_{o}, C_{e}\\right)',
]
new_strs = [
    '','(t)',
]
if len(old_strs) == len(new_strs):
    for i in range(len(old_strs)):
        word = word.replace(old_strs[i], new_strs[i])
    print("The new word is: \n" + word)
else:
    print("The length of old_strs unequals to the new_strs.")
