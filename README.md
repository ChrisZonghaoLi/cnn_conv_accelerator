# A Fixed-Pointed Rudimentary CNN Accelerator in Verilog

## 1. Introduction

A fixed-pointed (16-bit, 8-bit for decimal and 8-bit for fraction) rudimentary CNN accelerator that is written in Verilog is presented in this repository. First, the software OPAL which
stands for Ordinary People Accelerating Learning is used to train the CNN network whose trainee is the CIFAR-10 dataset.
Then the hyper-parameters are extracted and implemented in Verilog. 

In this project, only the convolutional calculation, biasing increment, and rectified linear unit function (ReLU) is 
prototyped, which means it does not contain the computations such as pooling/dropout/backpropagation etc. The accelerator design is inspired 
by the paper "Eyeriss: an energy-efficient reconfigurable accelerator for deep convolutional neural networks" by Chen, Krishna, Emer, and Sze; particularly, 
row-stationary (row sharing) mechanism is utilized in this implementation is used. Also, the dimension of the processing element is also determined by the input-feature-map
(ifmap), weight matrices, and output-feature-map dimensions (outmap), which is also explained in the paper mentioned above. The convolutional accelerator in
this design is only trained for CIFAR-10 and it is only for one layer, which means if you would like to use this for your application, you need to modified the I/O for this
accelerator.  

- For more information regarding OPAL, please check Dr. Brett Meyer's site (http://bhm.ece.mcgill.ca/~bhm/?p=173)
- For the Eyeriss paper, please visit: https://ieeexplore.ieee.org/document/7738524/
- For CIFAR-10 dataset, please visit: https://www.cs.toronto.edu/~kriz/cifar.html

Due to the reasearch NDA, some details regarding the OPAL will not be illustrated in details. For the access to my report, please 
email the author zonghao.lee@gmail.com for the password. 

## 2. Structure of this repository

This section will explain the directories of this repository.

	1. - opal (where the opal's I/O files are presented; again, due to NDA, please contact the author for more details)
			- example_CNN.cfg: configuration file for opal that defines the parameters.
			- example_CNN.txt: output summary that contains optimized hyper-parameter outlines.
			- example_CNN.npz: Python dictionary file that contains all hyper-parameters.
			- parse_weights.py: a Python parser to parse the dictionary file example_CNN.npz (so that you know what you are dealing with)
			- fixed_point_decimal: extract the weight, bias, and input matrices into vectors and store them in .txt files seperately.
	
	2. - matlab
			- fixed_point_binary: convert input/weight/bias extracted by to 16-bit binary numbers (8-bit.8-bit), and output them in .txt file.
			
	3. - report
			- Project.zip: it is an encrypted .zip file that contains the detailed explanation on this project. Please contact zonghao.lee@gmail.com for the password
			
	4. - verilog
			- project.v: contains the HDL Verilog implementation of the design. Please be reminded that this is just a personal exercise and 
						 the correctness should not be certained. However, you are welcome to point out the mistakes I made and use it for your applications.
			- systolic_array.xlsx: a graphical illustrartion on the architecture of the accelerator.			 
			
