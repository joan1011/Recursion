def getPermutations(array):
    permutations = []
    permutationHelper(array,[],permutations)
    return permutations

def permutationHelper(array,currentPermutation,permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i]+array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray,newPermutation,permutations)

getPermutations([1,2,3,4])
