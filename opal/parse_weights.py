import numpy as np

sel = 7

# load the raw results into a dictionary structure
raw_results = np.load("./example_CNN.npz")

print("The available keys in the dictionary are:")
results_keys = raw_results.keys()
for k in results_keys:
    print("\t" + k)

print("\nIf one were to examine the weights of the Pareto-optimal networks, there would be " + str(len(raw_results["pareto_weights"])) + " elements stored.")
print("\nBy inspecting the sixth set of weights, we see that there are " + str(len(raw_results['pareto_weights'][sel])) + " matrices/vectors stored.")
print("This implies there are " + str(len(raw_results['pareto_weights'][sel])//2) + " network layers (including the output layer and ignoring the input layer).")

print("\nLooking at each set of weights individually yields:")
for n in range(len(raw_results['pareto_weights'][sel])):
    print("\tShape of element " + str(n) + ": " + str(np.shape(raw_results['pareto_weights'][sel][n])))

print("\nFrom the above, it is clear that the weights are for a network with " + str(np.shape(raw_results['pareto_weights'][sel][0])[0]) + " inputs, and " + str(np.shape(raw_results['pareto_weights'][sel][0])[1]) + " elements in the first layer, etc...")

print("\nThe first, third, etc. elements shown above are the weight matrices (as explained in class), while the vectors shown are the bias values associated with the weights of the preceding matrices.")

print("\nLooking at the last two elements as an example, results in:")
print("Weight matrix:\n" + str(raw_results['pareto_weights'][sel][-2]))
print("Bias vector:\n" + str(raw_results['pareto_weights'][sel][-1]))
print("\nFrom the above, it can clearly be deduced that an input vector of " + str(np.shape(raw_results['pareto_weights'][sel][-2])[0]) + " elements multiplied by the matrix, then summed with the bias vector, will result in " + str(np.shape(raw_results['pareto_weights'][sel][-1])[0]) + " output elements (which can then have the nonlinear activation functions applied to).")

print("\nNote that this is just an example with randomly generated data; but it should illustrate the general structure of how the weights are stored.")

