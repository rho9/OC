import sys
import copy
bins_weight = 150


def main():
    instance_file = sys.argv[1]
    item_list = infer_file(instance_file)
    bins_1, available_space_1 = assign_bin_1(item_list)
    bins_2, available_space_2 = assign_bin_2(item_list)

    for i in range(len(bins_1)):
        bins_new, available_space_new = n1_lighter(bins_1, available_space_1)
        bins_1 = copy.deepcopy(bins_new)
        available_space_1 = copy.deepcopy(available_space_new)

    for i, bin in enumerate(bins_new):
        print(sum(item[1] for item in bin)+available_space_new[i])


def n1_lighter(bins, available_space):  # takes the bin which is lighter and tries to eliminate it
    bins.sort(key=sum_bin_weight)
    available_space.sort(reverse=True)
    bins_copy = copy.deepcopy(bins)
    available_space_copy = copy.deepcopy(available_space)
    for i in range(len(bins)):  # select bin to eliminate
        suitable = True  # bin_to_eliminate can't be emptied
        while bins_copy[i] and suitable:  # until bin is not empty
            for j in range(len(bins)):  # bins in which we try to place the items
                if i != j:  # check if the two bins are both the same
                    for k, item in enumerate(bins_copy[i]):  # select item to remove
                        # check if the item can be fit in the new bin and check if the color of the previous item is different
                        if item[1] <= available_space_copy[j] and item[2] != bins_copy[j][len(bins_copy[j])-1][2]:
                            bins_copy[j].append(item)
                            available_space_copy[j] -= item[1]
                            available_space_copy[i] += item[1]
                            bins_copy[i].pop(k)  # remove the item in the old bin
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