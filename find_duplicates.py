def find_problems(given_list = ["12345678a", "12345678b", "12345678c", "abcdefghi1","123"],print_me=True):
    """
    Scans a list of strings to find any cases where the first 8 characters are matching
    :param given_list: A string or list of strings to scan (optional, will demo otherwise)
    :param print_me: Boolean to choose if matches should be printed (Optional, defaults to true)
    :return: List of all matches
    """
    #If given a string, convert to a list of strings
    if isinstance(given_list,str):
        #If it contains commas, split via commas
        if "," in given_list:
            given_list = given_list.split(",")
        #If is doesnt have commas, use spaces
        else:
            given_list= given_list.split()

    trim_first_spaces(given_list)

    #Populate a list of keys
    keys = []
    for curr in given_list:
        keys.append(curr[:8])

    matching_strings = []
    index1 = 0
    #Check for matches
    for curr3 in keys:
        index2 = 0
        for curr4 in given_list:
            #Ignore matching with itself
            if curr3 == curr4[0:8] and index1 != index2:
                #If not already found
                if not curr4 in matching_strings:
                    matching_strings.append(curr4)
            index2 += 1
        index1 += 1
    #Pass in False to make this be quiet
    if print_me:
        print "Given List: "
        print given_list
        print "Problematic values: "
        print matching_strings.__str__()
    return matching_strings


def trim_first_spaces(given_list):
    """
    Fixes case in which the infile was delimited with commas, but had a starting space
    :param given_list: List supplied
    :return: List without leading spaces
    """
    p = 0
    for current_item in given_list:
        if given_list[p].startswith(" "):
            given_list[p] = given_list[p][1:]
        p += 1


if __name__ == '__main__':
    find_problems("This,is, a, demo")


