import sys
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
from django.db import connection


class apriori():

    def __init__(self):
        try:
            subsets =  chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])
        except Exception as e:
            logging.error('Algorithm failed during creation of non empty subsets')
        return subsets
    
    def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
            """calculates the support for items in the itemSet and returns a subset
           of the itemSet each of whose elements satisfies the minimum support"""
            _itemSet = set()
            localSet = defaultdict(int)

            for item in itemSet:
                    for transaction in transactionList:
                            if item.issubset(transaction):
                                    freqSet[item] += 1
                                    localSet[item] += 1

            for item, count in localSet.items():
                    support = float(count)/len(transactionList)

                    if support >= minSupport:
                            _itemSet.add(item)

            return _itemSet


    def joinSet(itemSet, length):
            """Join a set with itself and returns the n-element itemsets"""
            return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


    def getItemSetTransactionList(data_iterator):
        transactionList = list()
        itemSet = set()
        for record in data_iterator:
            transaction = frozenset(record)
            transactionList.append(transaction)
            for item in transaction:
                itemSet.add(frozenset([item]))              # Generate 1-itemSets
        return itemSet, transactionList


    def runApriori(data_iter, minSupport, minConfidence):
        """
        run the apriori algorithm. data_iter is a record iterator
        Return both:
         - items (tuple, support)
         - rules ((pretuple, posttuple), confidence)
        """
        itemSet, transactionList = getItemSetTransactionList(data_iter)

        freqSet = defaultdict(int)
        largeSet = dict()
        # Global dictionary which stores (key=n-itemSets,value=support)
        # which satisfy minSupport

        assocRules = dict()
        # Dictionary which stores Association Rules

        oneCSet = returnItemsWithMinSupport(itemSet,
                                            transactionList,
                                            minSupport,
                                            freqSet)

        currentLSet = oneCSet
        k = 2
        while(currentLSet != set([])):
            largeSet[k-1] = currentLSet
            currentLSet = joinSet(currentLSet, k)
            currentCSet = returnItemsWithMinSupport(currentLSet,
                                                    transactionList,
                                                    minSupport,
                                                    freqSet)
            currentLSet = currentCSet
            k = k + 1

        toRetItems = []
        for key, value in largeSet.items():
            toRetItems.extend([(tuple(item), getSupport(item))
                               for item in value])

        toRetRules = []
        for key, value in largeSet.items()[1:]:
            for item in value:
                _subsets = map(frozenset, [x for x in subsets(item)])
                for element in _subsets:
                    remain = item.difference(element)
                    if len(remain) > 0:
                        confidence = getSupport(item)/getSupport(element)
                        if confidence >= minConfidence:
                            toRetRules.append(((tuple(element), tuple(remain)),
                                               confidence))
        return toRetItems, toRetRules

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)
            
    def generateResults(items, rules):
        """returns the generated itemsets sorted by support and the confidence rules sorted by confidence"""
        for item, support in sorted(items, key=lambda (item, support): support):
            for rule, confidence in sorted(rules, key=lambda (rule, confidence): confidence):
                pre, post = rule
        return pre, post, support


    def dataFromFile(fname):
            """Function which reads from the file and yields a generator"""
            file_iter = open(fname, 'rU')
            for line in file_iter:
                    line = line.strip().rstrip(',')                         # Remove trailing comma
                    record = frozenset(line.split(','))
                    yield record


    if __name__ == "__main__":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from submissions")
            submissions_df = cursor.fetchall()

        inFile = None
        if submissions_df.input is None:
                inFile = sys.stdin
        elif submissions_df.input is not None:
                inFile = dataFromFile(submissions_df.input)
        else:
                print 'No dataset filename specified, system with exit\n'
                sys.exit('System will exit')

        minSupport = submissions_df.minS
        minConfidence = submissions_df.minC

        items, rules = runApriori(inFile, minSupport, minConfidence)

        generateResults(items, rules)