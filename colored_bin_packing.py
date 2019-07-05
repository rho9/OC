import sys
bins_weight = 150


def main():
    instance_file = sys.argv[1]
    item_list = infer_file(instance_file)
    bins = assign_bin_1(item_list)
    bins = assign_bin_2(item_list)


def n1_lighter(bins):  # takes the bin which is lighter and tries to eliminate it
    min_weight = bins_weight
    index_min_bin = 0
    for i, bin in enumerate(bins):
        temp_weight = 0
        for item in bin:
            temp_weight += item[1]  # sum of the weight in a bin
        if temp_weight < min_weight:
            min_weight = temp_weight
            index_min_bin = i

    # FINIRE QUI
    for bin in bins:  # per cercare lo spazio minimo in cui ci sta un item del bin che vogliamo togliere
        bin_weight = sum(item[1] for item in bin)  # matrice con pesi per non rifare (?)
        for min_items in bins[index_min_bin]:
            print(min_items)


    return bins


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
    for item in item_list:
        if item[1] <= bins_weight:
            bins.append([item])  # add one bin
    return bins


# assign items to bins in a smarter way (fills a bin, before going to next one)
def assign_bin_2(item_list):
    bins = [[]]  # bins are being represented as a list
    i = 0
    bin_weight = bins_weight
    for item in item_list:
        if item[1] <= bins_weight:
            if item[1] <= bin_weight:
                bins[i].append(item)
                bin_weight -= item[1]
            else:
                i += 1  # go to the next bin
                bin_weight = bins_weight
                bins.append([])
                bins[i].append(item)
                bin_weight -= item[1]
    return bins


if __name__ == '__main__':
    main()