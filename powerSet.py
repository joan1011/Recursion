#O(n*2^n) 
#def powerSet(array):
#    subsets = [[]]
#    for ele in array:
#        for i in range(len(subsets)):
#            currentSubset = subsets[i]
#            subsets.append(currentSubset+[ele])
#    return susbsets
#O(n*2^n)time |    O(n*2^n) space
def powerSet(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerSet(array,idx -1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset+[ele])
    return subsets
    
powerSet([1,2,3,4])
        
