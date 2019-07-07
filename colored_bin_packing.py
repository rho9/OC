import sys
import copy
import math
from collections import deque

bins_weight = 150


def main():
    instance_file = sys.argv[1]
    item_list = infer_file(instance_file)
    taboo_list = deque(maxlen=10)
    bins_new, available_space_new = assign_bin_2(item_list)

    print("Number of used bins at the beginning: ", len(bins_new))
    for bin in bins_new:
        print(bin)

    while True:  # the horror
        bins_old = copy.deepcopy(bins_new)
        available_space_old = copy.deepcopy(available_space_new)
        # try to use n1
        bins_new, available_space_new = copy.deepcopy(n1_lighter(bins_old, available_space_old))
        # if the result is the same as the previous iteration use n2
        if bins_new == bins_old:
            n2(bins_new, available_space_new, taboo_list)
            if bins_new == bins_old:  # if n2 is not applicable -> exit
                break
    bins_weight_ok = True
    for i, bin in enumerate(bins_new):
        if sum(item[1] for item in bin)+available_space_new[i] != bins_weight:
            bins_weight_ok = False
    print("Weight constraint observed: ", bins_weight_ok)

    print("Number of used bins at the end: ", len(bins_new))
    for bin in bins_new:
        print(bin)


def n2(bins, available_space, taboo_list):
    bins.sort(key=sum_bin_weight)
    available_space.sort(reverse=True)
    for i in range(math.ceil(len(bins)/2)):
        j = len(bins)-i -1  # reverse index (starting from bottom)
        item_1 = bins[i][len(bins[i])-1]
        color_1 = item_1[2]
        weight_1 = item_1[1]
        item_2 = bins[j][len(bins[j])-1]
        color_2 = item_2[2]
        weight_2 = item_2[1]
        # swap if the colors are the same and if the items aren't in the taboo list
        if color_1 == color_2 and not {item_1[0], item_2[0]} in taboo_list:
            if weight_1 <= (available_space[j] + weight_2) and weight_2 <= (available_space[i] + weight_1):
                tmp_1 = bins[i].pop(len(bins[i])-1)  # pop the item_1
                tmp_2 = bins[j].pop(len(bins[j])-1)  # pop the item_2
                bins[i].append(tmp_2)
                bins[j].append(tmp_1)
                available_space[i] += (weight_1 - weight_2)
                available_space[j] += (weight_2 - weight_1)
                taboo_list.append({item_1[0], item_2[0]})  # insert elements in the taboo list
                return bins, available_space
    return bins, available_space


def n1_lighter(bins, available_space):  # takes the bin which is lighter (the first) and tries to eliminate it
    bins.sort(key=sum_bin_weight)
    available_space.sort(reverse=True)
    bins_copy = copy.deepcopy(bins)
    available_space_copy = copy.deepcopy(available_space)
    for i in range(len(bins)):  # select bin to eliminate
        suitable = True  # bin_to_eliminate can't be emptied
        while bins_copy[i] and suitable:  # until bin is not empty
            for j in range(len(bins)):  # bins in which we try to place the items
                if i != j:  # check if the two bins are both the same
                    bin_to_remove = copy.deepcopy(bins_copy[i])
                    for item in bin_to_remove:  # select item to remove
                        # check if the item can be fit in the new bin and check if the color of the previous item is different
                        if item[1] <= available_space_copy[j] and item[2] != bins_copy[j][len(bins_copy[j])-1][2]:
                            bins_copy[j].append(item)
                            available_space_copy[j] -= item[1]
                            available_space_copy[i] += item[1]
                            bins_copy[i].remove(item)  # remove the item in the old bin
                    if not bins_copy[i]:
                        break
            if bins_copy[i]:  # it was not possible to empty bin_to_eliminate
                suitable = False
                bins_copy = copy.deepcopy(bins)  # reset the initial bin
                available_space_copy = copy.deepcopy(available_space)
            else:
                bins_copy.pop(i)  # removes the empty list
                available_space_copy.pop(i)
                return bins_copy, available_space_copy
    return bins, available_space


def sum_bin_weight(bin):
    return sum(item[1] for item in bin)


def infer_file(instance_file):  # read input file and return a list of items
    input_file = open(instance_file, "r")
    item_list = []  # each element describes an item [item, weight, color]
    for item, line in enumerate(input_file):
        weight = int(line.split("\t")[0])
        color = int(line.split("\t")[1])
        item_list.append([item+1, weight, color])
    input_file.close()
    return item_list


# assign items to bins in a dumb way (one item for each bin)
def assign_bin_1(item_list):
    bins = []  # bins are being represented as a list
    weights = []
    for item in item_list:
        if item[1] <= bins_weight:
            bins.append([item])  # add one bin
            weights.append(bins_weight - item[1])  # add the weight of the bin
    return bins, weights


# assign items to bins in a smarter way (fills a bin, before going to next one)
def assign_bin_2(item_list):
    bins = [[]]  # bins are being represented as a list
    weights = ['']
    i = 0
    bin_weight = bins_weight
    for item in item_list:
        if item[1] <= bins_weight:
            if item[1] <= bin_weight:
                # check if it's the first item or the previous one has a different color
                if bins[i] == [] or item[2] != bins[i][len(bins[i])-1][2]:
                    bins[i].append(item)
                    bin_weight -= item[1]
                    weights[i] = bin_weight
            else:
                i += 1  # go to the next bin
                bin_weight = bins_weight
                bins.append([])
                bins[i].append(item)
                bin_weight -= item[1]
                weights.append([])
                weights[i] = bin_weight
    return bins, weights


if __name__ == '__main__':
    main()