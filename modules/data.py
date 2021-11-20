
def make_list_file(target_file):
    target_list = []
    with open(target_file, 'r') as f:
        for line in f:
            target_list.append(line.strip())
    return target_list
