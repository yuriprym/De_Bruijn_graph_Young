#!/bin/env python 
import pdb
import networkx as nx
import sys
import matplotlib.pyplot as plt
import pygraphviz as pgv
# this will create the inital call to the kmers value 
class method:
   # def kmers(self,value,seq):
   #     ls="" 
   #     rs=""
   #     i=0
   #     j=0
   #     while (i <= len(seq)):
   #         if (value == i):
   #             ls= seq[value-i:i]
   #         if (value == i):
   #             rs = (seq[2*value-i:2*i])
   #         i= i + 1
   #     side = [ ls , rs ]
   #     j=i
   #     if (j== len(seq)):
   #         self.kmers(value,seq)
   #return side
   ###################I did while following along in a video on john hopkins on how to de burjin graph in python#################
    def de_burjin(self,value,side):
        edges=[]
        nodes=set()
        for i in range(len(side)-value+1):
            edges.append((side[i:i+value-1],side[i+1:i+value]))
            nodes.add(side[i:i+value-1])
            nodes.add(side[i+1:i+value])
        return nodes,edges
    ################ trying to be transparent ###################### 
    def visualization(self,value,side):
        nodes,edges=self.de_burjin(value,side)
        G=nx.Graph()
        G=nx.algorithms.euler.eulerian_circuit(edges,nodes)
        nx.draw(G)
        plt.savfig("de_burgin_eulerain.png")
        plt.show()


def main():
   meth=method()
   #sequence="ATGTACGATCATTTA"
   #subproblem=input("random graphing frame")
   #subproblem=int(subproblem)
   #side=meth.kmers(subproblem,sequence)
   #meth.slideingwindow(subproblem,side)
   sub=input("random graphing frame: ")
   sub=int(sub)
   neon =input("please input a short genome: ")
   print(type(neon))
   seq,k = meth.de_burjin(sub,neon)
   print (seq) 
   print (k)
   print (meth.visualization(sub,neon))
  
main() 



#Hamming distance 
#
