import numpy as np
import re

def main():
    sum = 0
    dict = {}
    
    with open('day4_input.txt') as file:
        for line in file:
            card, elf_no, winning_no = line.replace('|', ':').split(sep = ":")
            card = int(re.findall(r'\d+', card)[0])
            
            elf_no = [int(s) for s in elf_no.split()]
            winning_no = [int(s) for s in winning_no.split()]

            share = len(np.intersect1d(elf_no, winning_no))

            # For the first part
            if share != 0:
                sum = sum + 2**(share-1)
            
            # For the second part
            dict[card] = np.arange(card+1, card+share+1)

    visited = [] # List for visited nodes.
    queue = list(dict.keys())    #Initialize a queue

    def mod_bfs(visited, graph, node): #function for BFS
        if visited:
            visited.append(node)
            queue.append(node)

        while queue:          # Creating loop to visit each node
            m = queue.pop(0)

            for neighbour in graph[m]:
                visited.append(neighbour)
                queue.append(neighbour)
        
        if len(queue) == 0:
            return(visited)

    print("Modified Breadth-First Search")
    result = mod_bfs(visited, dict, 1)
    return(len(dict.keys()) + len(result))


if __name__ == "__main__":
    print(main())