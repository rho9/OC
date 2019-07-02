import sys
import random


def main():
    percentage = sys.argv[1]
    instances_file = sys.argv[2]
    instances_file_out_path = sys.argv[3]
    input_file = open(instances_file, "r")
    output_file = open(instances_file_out_path, "w+")
    sum = 0
    for line in input_file:
        chance = random.uniform(1, 100)
        color = "-1" if chance <= int(percentage) else "+1"  # percentage used as threshold.
        output_file.write(line.split("\n")[0] + "\t" + color + "\n")
        sum += int(color)
    output_file.close()
    input_file.close()
    print(sum)


if __name__ == '__main__':
    main()
