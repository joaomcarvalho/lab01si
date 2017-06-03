def maximo(array):
        max = array[0]
        for i in range (len(array)):
                if (max < array[i]):
                        max = array[i]
        return max
