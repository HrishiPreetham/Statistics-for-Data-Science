{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d88c39c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'np' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 22>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mpseudo_uniform\u001b[39m(low\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m,high\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m,seed\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m123456789\u001b[39m,size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m low\u001b[38;5;241m+\u001b[39m(high\u001b[38;5;241m-\u001b[39mlow)\u001b[38;5;241m*\u001b[39mpseudo_uniform_good(seed\u001b[38;5;241m=\u001b[39mseed,size\u001b[38;5;241m=\u001b[39msize)\n\u001b[1;32m---> 22\u001b[0m l\u001b[38;5;241m=\u001b[39m\u001b[43mpseudo_uniform\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlow\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[38;5;241;43m5\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43mhigh\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m7\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43msize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m10000\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     23\u001b[0m plt\u001b[38;5;241m.\u001b[39mhist(l,bins\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m20\u001b[39m,edgecolor\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mk\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     24\u001b[0m plt\u001b[38;5;241m.\u001b[39mxticks(fontsize\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m15\u001b[39m)\n",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36mpseudo_uniform\u001b[1;34m(low, high, seed, size)\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mpseudo_uniform\u001b[39m(low\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m,high\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m,seed\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m123456789\u001b[39m,size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[1;32m---> 21\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m low\u001b[38;5;241m+\u001b[39m(high\u001b[38;5;241m-\u001b[39mlow)\u001b[38;5;241m*\u001b[39m\u001b[43mpseudo_uniform_good\u001b[49m\u001b[43m(\u001b[49m\u001b[43mseed\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mseed\u001b[49m\u001b[43m,\u001b[49m\u001b[43msize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43msize\u001b[49m\u001b[43m)\u001b[49m\n",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36mpseudo_uniform_good\u001b[1;34m(mult, mod, seed, size)\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mpseudo_uniform_good\u001b[39m(mult\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m16807\u001b[39m,mod\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m2\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m31\u001b[39m)\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m,seed\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m123456789\u001b[39m,size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m):\n\u001b[1;32m---> 13\u001b[0m     U\u001b[38;5;241m=\u001b[39m\u001b[43mnp\u001b[49m\u001b[38;5;241m.\u001b[39mzeros(size)\n\u001b[0;32m     14\u001b[0m     x\u001b[38;5;241m=\u001b[39m(seed\u001b[38;5;241m*\u001b[39mmult\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m)\u001b[38;5;241m%\u001b[39mmod\n\u001b[0;32m     15\u001b[0m     U[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m=\u001b[39mx\u001b[38;5;241m/\u001b[39mmod\n",
      "\u001b[1;31mNameError\u001b[0m: name 'np' is not defined"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import numpy\n",
    "#def pseudo_uniform_badmethod(mult=5,mod=11,seed=1,size=1):\n",
    "  #  U=np.zeros(size)\n",
    "  #  x=(seed*mult+1)%mod\n",
    "   # U[0]=x/mod\n",
    "   # for i in range(1,size)\n",
    "   #     x=(x*mult+1)%mod\n",
    "   #     U[i]=x/mod\n",
    "   # return U\n",
    "# This is a bad method of creating a random number generator\n",
    "def pseudo_uniform_good(mult=16807,mod=(2**31)-1,seed=123456789,size=1):\n",
    "    U=np.zeros(size)\n",
    "    x=(seed*mult+1)%mod\n",
    "    U[0]=x/mod\n",
    "    for i in range(1,size):\n",
    "        x=(x*mult+1)%mod\n",
    "        U[i]=x/mod\n",
    "    return U\n",
    "def pseudo_uniform(low=0,high=1,seed=123456789,size=1):\n",
    "    return low+(high-low)*pseudo_uniform_good(seed=seed,size=size)\n",
    "l=pseudo_uniform(low=-5,high=7,size=10000)\n",
    "plt.hist(l,bins=20,edgecolor='k')\n",
    "plt.xticks(fontsize=15)\n",
    "plt.yticks(fontsize=15)\n",
    "plt.xlim(-6,8)\n",
    "plt.show()\n",
    "\n",
    "def sample_pick(lst):\n",
    "    t=time.perf_counter()\n",
    "    seed=int(10**9*float(str(t-int(t))[0:]))\n",
    "    l=len(lst)\n",
    "    s=pseudo_uniform(low=0,high=1,seed=seed,size=1)\n",
    "    idx=int(s)\n",
    "    return (lst[indx])\n",
    "\n",
    "\n",
    "dice_faces=['one','two','three','four','five','six']\n",
    "for _ in range(30):\n",
    "    print(sample_pick(dice_faces))\n",
    "    \n",
    "def pseudo_bernoulli(p=0.5,size=1):\n",
    "    t=time.perf_counter()\n",
    "    seed=int(10**9*float(str(t-int(t))[0:]))\n",
    "    B=pseudo_uniform(seed=seed,size=size)\n",
    "    B=(B<=p).astype(int)\n",
    "    return B\n",
    "\n",
    "def pseudo_binomial(n=100,p=0.5,size=1):\n",
    "    binom=[]\n",
    "    for _ in range(size):\n",
    "        t=time.perf_counter()\n",
    "        seed=int(10**9*float(str(t-int(t))[0:]))\n",
    "        U=pseudo_uniform(size=n,seed=seed)\n",
    "        Y=(U<=p).astype(int)\n",
    "        binom.append(np.sum(Y))\n",
    "    return binom\n",
    "psuedo_binomial(n=100,p=0.75,size=15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17cf7ff8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2668e21",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08b680b4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
