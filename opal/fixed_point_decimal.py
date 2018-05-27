# fixed-point weight/input/bias conversion (decimal) and all save txt files are vectors

import numpy as np
raw_results = np.load("./example_CNN.npz")

# error rate: about 25%
sel = 0 

# based on the data strructure in the dictionary file:
#        Shape of element 0: (5, 5, 3, 32)
#        Shape of element 1: (32,)
#        Shape of element 2: (32,)
#        Shape of element 3: (32,)
#        Shape of element 4: (32,)
#        Shape of element 5: (32,)
#        Shape of element 6: (3, 3, 32, 64)
#        Shape of element 7: (64,)
#        Shape of element 8: (64,)
#        Shape of element 9: (64,)
#        Shape of element 10: (64,)
#        Shape of element 11: (64,)
#        Shape of element 12: (7, 7, 64, 64)
#        Shape of element 13: (64,)
#        Shape of element 14: (64,)
#        Shape of element 15: (64,)
#        Shape of element 16: (64,)
#        Shape of element 17: (64,)
#        Shape of element 18: (256, 10)
#        Shape of element 19: (10,)
#        Shape of element 20: (10,)
#        Shape of element 21: (10,)
#        Shape of element 22: (10,)
#        Shape of element 23: (10,)

f = 8

fil_k1 = 32 
cha_k1 = 3  
row_k1 = 5  
col_k1 = 5  

fil_k2 = 64 
cha_k2 = 3  
row_k2 = 3  
col_k2 = 3  

fil_k3 = 64 
cha_k3 = 3  
row_k3 = 7  
col_k3 = 7  

# Memory allocations for the targeted reshaped kernels
kernel_1 = np.zeros((fil_k1, cha_k1, row_k1, col_k1))
kernel_2 = np.zeros((fil_k2, cha_k2, row_k2, col_k2))
kernel_3 = np.zeros((fil_k3, cha_k3, row_k3, col_k3))
bias_1 = np.zeros(fil_k1)
bias_2 = np.zeros(fil_k2)
bias_3 = np.zeros(fil_k3)


# reshape the first kernel, and do fixed-point conversion
for u1 in range (0, fil_k1):
    for k1 in range (0, cha_k1):
        for i1 in range (0, row_k1):
            for j1 in range (0, col_k1):
                kernel_1[u1][k1][i1][j1] = int(raw_results['pareto_weights'][sel][0][i1][j1][k1][u1] * (2**f)) / (2**f)
                
# reshape the second kernel and do fixed-point conversion
for u2 in range (0, fil_k2):
    for k2 in range (0, cha_k2):
        for i2 in range (0, row_k2):
            for j2 in range (0, col_k2):
                kernel_2[u2][k2][i2][j2] = int(raw_results['pareto_weights'][sel][6][i2][j2][k2][u2] * (2**f)) / (2**f)
                
# reshape the third kernel and do fixed-point conversion
for u3 in range (0, fil_k3):
    for k3 in range (0, cha_k3):
        for i3 in range (0, row_k3):
            for j3 in range (0, col_k3):
                kernel_3[u3][k3][i3][j3] = int(raw_results['pareto_weights'][sel][12][i3][j3][k3][u3] * (2**f)) / (2**f)
                
# bias for first layer and do fixed-point conversion
bias_1 = raw_results['pareto_weights'][sel][1]
for p in range (np.size(raw_results['pareto_weights'][0][1])):
    bias_1[p] = int(bias_1[p] * (2**f)) / 2**f

# bias for second layer and do fixed-point conversion
bias_2 = raw_results['pareto_weights'][sel][7]
for q in range (np.size(raw_results['pareto_weights'][0][7])):
    bias_2[q] = int(bias_2[q] * (2**f)) / 2**f

# bias for third layer and do fixed-point conversion
bias_3 = raw_results['pareto_weights'][sel][13]
for r in range (np.size(raw_results['pareto_weights'][0][13])):
    bias_3[q] = int(bias_3[r] * (2**f)) / 2**f

# reshape them to vector 
kernel_1_vec = kernel_1.ravel()
kernel_2_vec = kernel_2.ravel()
kernel_3_vec = kernel_3.ravel()
bias_1_vec = bias_1.ravel()
bias_2_vec = bias_2.ravel()
bias_3_vec = bias_3.ravel()

# reshape also testing input to a vector 
I = np.loadtxt("test_batch.txt")
I_vec = I.ravel()

# Save
np.savetxt('kernel_1.txt', kernel_1_vec, fmt="%.8f")
np.savetxt('kernel_2.txt', kernel_2_vec, "%.8f")
np.savetxt('kernel_3.txt', kernel_3_vec, "%.8f")
np.savetxt('bias_1.txt', bias_1_vec, "%.8f")
np.savetxt('bias_2.txt', bias_2_vec, "%.8f")
np.savetxt('bias_3.txt', bias_3_vec, "%.8f")
np.savetxt('I_vec.txt', I_vec, "%d")






