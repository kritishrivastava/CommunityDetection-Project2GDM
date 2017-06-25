# CommunityDetection-Project2GDM
Points to be covered:


Software that needs to be installed (if any) with URL’s to download and
instructions to install them.
○ Environment variable settings (if any) and OS it should/could run on.
○ Instructions on how to run the program, with specific run command example that
can be copy pasted.
○ Instructions on how to interpret the results.
○ Sample input and output files.
○ Citations to any software you may have used or any dataset you may have tested
your code on.


This is an implementation for the algorithm from the paper 1: Efficient Identification of Overlapping
Communities?

Python version used: Python 3.6.0
OS used: Windows 10 64bit (RAM:16GB)

Python libraries needed:
Networkx: install using the command "pip install networkx" or follow the instructions mentioned here https://networkx.github.io/documentation/development/install.html
Numpy: install using the command "pip install numpy" or follow the intructions mentioned here https://docs.scipy.org/doc/numpy/user/install.html

Instructions to run the program:
1. Open python shell
2. Give the command "main.py filename" where filename is the name of the graph you want to find the communities for.
   ex. main.py amazon.graph.medium

For the above input graph "amazon.graph.medium", the outfile file is amazon.graph.medium.clusters.txt

The output file contains the list of communities identified for the graph given as input.
Every line is a community and
