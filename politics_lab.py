voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting = dict()
    for row in voting_data:
        cols = row.split()#for cols in row.split(' '):
        #print(cols)
        voting[cols[0]] = [ int(cols[i]) for i in range(3, len(cols)) ]
    return voting 
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    sum = 0
    for i in range(len(voting_dict[sen_a])):
        sum += voting_dict[sen_a][i] * voting_dict[sen_b][i]
    return sum


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    comp = [(policy_compare(sen, x, voting_dict), x) for x in voting_dict if x != sen]
    comp.sort()
    comp.reverse()
    return comp[0][1]
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    comp = [(policy_compare(sen, x, voting_dict), x) for x in voting_dict if x != sen]
    comp.sort()
    return comp[0][1]
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return sum([policy_compare(sen, i, voting_dict) for i in sen_set])/len(sen_set)

def avg_dem():
    vd = create_voting_dict()
    names = {row.split()[0] for row in voting_data if row.split()[1] == 'D'}
    avgs = []
    for name in names:
        names_cop = names.copy()
        names_cop.remove(name)
        avgs.append((find_average_similarity(name, names_cop, vd),name))
    avg = sum([ avgs[i][0] for i in range(len(avgs)) ])/len(avgs)
    avgs = [ (abs(avg - sim), name) for (sim, name) in avgs ]
    avgs.sort()
    return avgs[0][1]
    #avgs = [(find_average_similarity(sen, names))]
    #print(len(names))
# 'Schumer', 'Feinstein', 'Kerry'
most_average_Democrat = avg_dem() #"Bayh" # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    #length = len(list(voting_dict.values())[0])
    #v = []
    #for i in range(length):
    #    v.append(sum([voting_dict[sen][i] for sen in sen_set])/ (len(sen_set)) )    
    #return v
    sen_set_votes = [ voting_dict[senator] for senator in voting_dict if senator in sen_set]
    return [ sum(votes)/len(votes) for votes in zip(*sen_set_votes) ]

raw_list = [line.split() for line in voting_data]
demograts = {line[0] for line in raw_list if line[1] == 'D'}
average_Democrat_record = find_average_record(demograts, create_voting_dict()) # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    comb = combinations(voting_dict, 2)
    diff = {policy_compare(sen1, sen2, voting_dict): (sen1, sen2) for sen1, sen2 in comb}
    return diff[min(diff)]

