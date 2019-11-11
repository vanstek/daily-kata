# Length of missing array
# Level: 6kyu
'''
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.
'''

def get_length_of_missing_array(array_of_arrays):

    if array_of_arrays is None:
        return 0
    elif len(array_of_arrays) == 0:
        return 0
    else:
        for i in array_of_arrays:
            if i is None or len(i) == 0:
                return 0
                
    array_lengths = []
    for i in array_of_arrays:
        array_lengths.append(len(i))
    array_lengths = sorted(array_lengths)
    print(array_lengths)

    diff = 0;
    for i, val in enumerate(array_lengths[:-1]):
        diff = array_lengths[i+1] - array_lengths[i]
        if diff > 1:
            return array_lengths[i] + 1
    
