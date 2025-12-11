text = 'An apple a day keeps the doctor away'
arr = text.split()
#Liczba słów
def numofwords():
    words=0
    for i in arr:
        words+=1
    return words
print(f'Text: {text}')
print('Number of words: ',numofwords())
#Najdłuższe do najkrótszego
def longestword(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print('Words from the longest: ', longestword(arr))
#Alfabetyczna kolejność
def alfabetically(arr):
    sorted_arr = sorted(arr, key=str.lower)
    return sorted_arr
print('Words ordered alphabetically: ',alfabetically(arr))


