def insertionSort(listku):
    for index in range(1,len(listku)):
        current_element = listku[index]
        i = index
        while current_element < listku[i-1] and i > 0:
            listku[i] = listku[i-1]
            i = i-1
        listku[i] = current_element
 
jumlah = int(input("Berapa banyak element yang diinginkan : "))
list1 = [int(input()) for i in range (jumlah)]
insertionSort(list1)
print (list1)
