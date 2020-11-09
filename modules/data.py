
def make_list_file(target_list):
    host_list = []
    with open(target_list, 'r') as f:
        for line in f:
            host_list.append(line.strip())
    return host_list
