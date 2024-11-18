def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[len(arr) // 2] # Escolhendo pivô como elemento do meio
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)

# Exemplos de uso

# Lista de números

numeros = [12, 7, 8, 9, 3, 5]

print("Original:", numeros)

print("Ordenado:", quicksort(numeros))