with open('input.txt') as f:
    data = f.readlines()

data = [x.strip().split(' ') for x in data]
data = [(x[0].split('-'), x[1][0], x[2]) for x in data]


def check_valid_pass_pt1(line):
    range_, char_, pass_ = line

    min_, max_ = [int(x) for x in range_]

    occs = sum([1 if l == char_ else 0 for l in pass_])

    return int(max_ >= occs >= min_)


def pt1(data_):
    ctr = 0
    for line in data_:
        ctr += check_valid_pass_pt1(line)
    return ctr


pt1_ = pt1(data)
print('Part 1:', pt1_)


def check_valid_pass_pt2(line):
    range_, char_, pass_ = line
    min_, max_ = [int(x) for x in range_]
    occs = int(pass_[min_-1] == char_) + int(pass_[max_-1] == char_)

    return int(occs == 1)


def pt2(data_):
    ctr = 0
    for line in data_:
        ctr += check_valid_pass_pt2(line)
    return ctr


pt2_ = pt2(data)
print('Part 2:', pt2_)
