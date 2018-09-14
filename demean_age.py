import numpy as np
age = loadtxt('participants.tsv', skiprows=1, usecols=1)
meanage = sum(age)/len(age)
np.savetxt("demeaned_age.txt", age-mean_age)
print("done!")