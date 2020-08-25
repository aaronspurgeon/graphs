from util import Stack, Queue


def get_parents(ancestors, child):
    results = list()
    for item in ancestors:
        if child == item[1]:
            results.append(item[0])
    return results


def earliest_ancestor(ancestors, starting_node):
    child_list = set()
    for item in ancestors:
        child_list.add(item[1])
    # if starting node doesn't have a parent return -1
    if starting_node not in child_list:
        return -1
    else:
        # make an empty stack
        s = Stack()
        # push the starting node into the stack
        s.push([starting_node])
        # keep track of which nodes you've visited
        visited = set()
        # while there is something in the stack
        while s.size() > 0:
            # remove the first item from the stack
            path = s.pop()
            # remove the first item from the path
            n = path[-1]
            # check if n has been visited
            if n not in visited:
                # if not... add it to the visited set
                visited.add(n)
            # get a list of parents for the current node
            for parent in get_parents(ancestors, n):
                # make a copy of the path
                path_copy = path.copy()
                # append that parent node to the path_copy
                path_copy.append(parent)
                # push the path copy into the stack
                s.push(path_copy)
                # print(path)
                # print(parent)
        # return earliest ancestor
        return path[-1]
