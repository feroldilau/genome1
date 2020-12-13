#!/bin/env python3
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

"""Perform assembly based on debruijn graph."""

import argparse
import os
import sys
import networkx as nx
import matplotlib
from operator import itemgetter
import random
random.seed(9001)
from random import randint
import statistics

__author__ = "Laurent Feroldi"
__copyright__ = "Eisti"
__credits__ = ["Laurent"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Laurent"
__email__ = "feroldilau@eisti.eu"
__status__ = "Developpement"

def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path

def get_arguments():
    """Retrieves the arguments of the program.
      Returns: An object that contains the arguments
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description=__doc__, usage=
                                     "{0} -h"
                                     .format(sys.argv[0]))
    parser.add_argument('-i', dest='fastq_file', type=isfile,
                        required=True, help="Fastq file")
    parser.add_argument('-k', dest='kmer_size', type=int,
                        default=21, help="K-mer size (default 21)")
    parser.add_argument('-o', dest='output_file', type=str,
                        default=os.curdir + os.sep + "contigs.fasta",
                        help="Output contigs in fasta file")
    return parser.parse_args()


def read_fastq(fastq):
    '''Renvoie les séquences contenues dans un fichier fastq '''
    
    with open(fastq, "r") as filin:
        for line in filin:
            yield next(filin).strip()
            next(filin)
            next(filin)

def cut_kmer(seq, k):
    '''Renvoie les k-mer de taille k d'une séquence '''
    
    for base in range(len(seq)-k+1):
        yield seq[base:base+k]



def build_kmer_dict(fastq, k):
    '''Renvoie le dictionnaire des k-mers'''
    
    dict_kmer = {}
    for seq in read_fastq(fastq):
        for kmer in cut_kmer(seq, k):
            if not kmer in dict_kmer:
                dict_kmer[kmer] = 1
            else:
                dict_kmer[kmer] += 1

    return dict_kmer


def build_graph(dict_kmer):
    '''Créer graphe à partir des k-mers
    '''
    graph = nx.DiGraph()
    for key, value in dict_kmer.items():
        key_pre = key[:-1]
        key_suf = key[1:]
        graph.add_node(key_pre)
        graph.add_node(key_suf)
        graph.add_edge(key_pre, key_suf, weight=value)

    return graph




def remove_paths(graph, list_path, delete_entry_node, delete_sink_node):
    '''Supprimer un chemin donné du graphique
    '''
    start = 1
    end = 1
    if delete_entry_node:
        start = 0
    if delete_sink_node:
        end = 0

    for path in list_path:
        for node in range(start, len(path)-end):
            graph.remove_node(path[node])

    return graph

def std(list_val):
    '''Calcul écart-type d'une liste de valeurs
    '''
    if len(list_val) == 1:
        return 0
    return statistics.stdev(list_val)



def select_best_path(graph, path_list, path_length, weight_avg_list, 
                     delete_entry_node=False, delete_sink_node=False):
    pass

def path_average_weight(graph, path):
    '''Calcul le poids moyen d'un chemin
    '''
    weight = 0
    for i in range(len(path)-1):
        weight += graph.edges[path[i], path[i+1]]["weight"]

    return weight/(len(path)-1)

def solve_bubble(graph, ancetre, descend):
  

def simplify_bubbles(graph):
  
   

def solve_entry_tips(graph, list_in):



def get_starting_nodes(graph):
    '''Trouver noeuds d'entrée
    '''
    list_start = []
    for node in graph.nodes.data():
        if not list(graph.predecessors(node[0])):
            list_start.append(node[0])

    return list_start

def get_sink_nodes(graph):
    '''Trouver noeuds de sortie
    '''
    list_end = []
    for node in graph.nodes.data():
        if not list(graph.successors(node[0])):
            list_end.append(node[0])

    return list_end

def get_contigs(graph, list_start, list_end):
    '''Retourner tuple de contigs
    '''
    list_contig = []
    for start in list_start:
        for end in list_end:
            for path in nx.all_simple_paths(graph, start, end):
                contig = path[0]
                for i in range(1, len(path)):
                    contig += path[i][-1]

                list_contig.append((contig, len(contig)))

    return list_contig

def save_contigs(list_tupple, filename):
    '''Sauvegarder contigs dans fichier de sortie
    '''
    with open(filename, "w") as filout:
        for i in range(len(list_tupple)):
            contig = list_tupple[i][0]
            l_contig = list_tupple[i][1]
            filout.write(">contig_{} len={}\n{}\n".format(
                i, l_contig, fill(contig)))













def fill(text, width=80):
    """Split text with a line return to respect fasta format"""
    return os.linesep.join(text[i:i+width] for i in range(0, len(text), width))

#==============================================================
# Main program
#==============================================================
def main():
    """
    Main program function
    """
    # Get arguments
    args = get_arguments()

if __name__ == '__main__':
    main()
