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
1. Go the the directory containing the python script.
2. Give the command "python main.py filename" where filename is the name of the graph you want to find the communities for.
   ex. python main.py amazon.graph.medium

For the above input graph "amazon.graph.medium", the outfile file is "amazon.graph.medium.clusters.txt".

The output file contains the list of communities identified for the graph given as input.
Every line represents one community and it contains the list of nodes in that community.

ex. 

1917 1918 1919 1920 4906 4980 

2099 2100 2101 2102 2104 2105 2789 3997 

This output contains 2 communities. The first community contains 6 nodes and the second community contains 8 nodes.

Datasets tested:
amazon.medium.graph
youtube.medium.graph
dblp.small.graph
