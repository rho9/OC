import sys


def main():
    instance_file = sys.argv[1]
    item_list = infer_file(instance_file)


def infer_file(instance_file):  # read input file and return a list of items
    input_file = open(instance_file, "r")
    item_list = []  # each element describes an item [item, weight, color]
    for item, line in enumerate(input_file):
        weight = int(line.split("\t")[0])
        color = int(line.split("\t")[1])
        item_list.append([item+1, weight, color])
    input_file.close()
    return item_list


if __name__ == '__main__':
    main()