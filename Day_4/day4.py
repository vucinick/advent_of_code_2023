import numpy as np

def main():
    sum = 0

    with open('day4_input.txt') as file:
        for line in file:
            elf_no, winning_no = line.split(sep = ":")[1].split(sep = "|")
        
            elf_no = [int(s) for s in elf_no.split()]
            winning_no = [int(s) for s in winning_no.split()]

            share = len(np.intersect1d(elf_no, winning_no))
            
            if share != 0:
                sum = sum + 2**(share-1)
        
    return(sum)


if __name__ == "__main__":
    print(main())