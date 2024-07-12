# ----------------
# Fonctions d'aide
# ----------------

def swap(tab, i, j) :
    """Échange la place des éléments aux indices i et j du tableau"""
    
    tab[i], tab[j] = tab[j], tab[i]
    
    return tab
    
# ---------------
# Tris classiques
# ---------------

def bubble_sort(tab) :
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""

    for i in range(len(tab) - 1, 0, -1) :
        for j in range(0, i) :
            if tab[j + 1] < tab[j] :
                swap(tab, j, j + 1)

    return tab

def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""

    for i in range(1, len(tab)) :
        x = tab[i]
        j = i
        while j > 0 and tab[j - 1] > x :
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = x

    return tab  

def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
  
    for i in range(0, len(tab) - 1) :
        min = i
        for j in range(i + 1, len(tab)) :
            if tab[j] < tab[min] :
                min = j
        if min != i :
                swap(tab, i, min)
    return tab

# --------------
# Tris récursifs
# --------------

def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""

    merge_sort_r(tab, 0, len(tab)) 

    return tab

def merge_sort_r(tab, start, end):
    
    if start < end - 1:  # To check if tab has more than 1 element.
        m = (start + end) // 2
        merge_sort_r(tab, start, m)
        merge_sort_r(tab, m, end)
        merge(tab, start, m, end)

def merge(tab, start, middle, end):
    i = start
    j = middle
    temp = [None] * (end - start)
    k = 0

    while i < middle and j < end:
        if tab[i] <= tab[j]:
            temp[k] = tab[i]
            i += 1
        else:
            temp[k] = tab[j]
            j += 1
        k += 1

    while i < middle:
        temp[k] = tab[i]
        i += 1
        k += 1

    while j < end:
        temp[k] = tab[j]
        j += 1
        k += 1

    for k in range(end - start):
        tab[start + k] = temp[k]

    return tab

def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""

    quick_sort_r(tab, 0, len(tab)-1)

    return tab
    

def partitionner (tab, first, last) :
    
    pivot = tab[last]
    i = first - 1

    for j in range(first, last) :
        if tab[j] <= pivot :
            i = i + 1
            swap(tab, i, j)

    swap(tab, i + 1, last)

    return i + 1
            
def quick_sort_r(tab, first, last):

    if first < last :

        pivot = partitionner(tab, first, last)
        quick_sort_r(tab, first, pivot - 1)
        quick_sort_r(tab, pivot + 1, last)

    return tab
