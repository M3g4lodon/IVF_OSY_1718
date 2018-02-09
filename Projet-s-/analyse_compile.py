import os
import re

from Language import *

CURRENT_DIRECTORY = os.getcwd()


def read(relative_location):
    with open(CURRENT_DIRECTORY + '/' + relative_location, 'r') as f:
        content = f.read()
    return content

class Control_Flow_Graph:
    def __init__(self, file_location):
        self.graph = Control_Flow_Graph.construct_graph(read(file_location))

    @staticmethod
    def construct_graph(input):
        programme_txt = [re.sub(r'#.+', '', line) for line in input.split('\n')]
        programme_txt = filter(lambda line: line != '', programme_txt)
        programme_txt = [line.strip() for line in programme_txt]
        for i, line in enumerate(programme_txt):
            if line == '}': continue
            expression = line.split()[1]
            label = re.findall(r'(\w+):', expression)[0]
            print(i, line, label)
"""graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}"""

if __name__ == "__main__":
    Control_Flow_Graph('exemple_0.txt')
