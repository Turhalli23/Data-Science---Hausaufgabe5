import matplotlib.pyplot as plt # Import soll am Anfang für Lesbarkeit bleiben

def merge_sort(arr): # Name der Variable ist zu lang (1) und bessere Name für Methode (2)
    if (len(arr) > 1): # Wenn Lange der Liste größer als 1 ist, sind andere Voraussetzungen schon unnötig. (3)
        mid = len(arr) // 2
        left_arr = arr[:mid] # Bessere Name für Lesbarkeit (7)
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        l_index = 0 # Bessere Name für Lesbarkeit (5)
        r_index = 0
        i_index = 0

        length_rigth = len(right_arr) # Bei jedes Mal führen wir die selbe Funktion aus, um die Länge der Liste zu kriegen. Es ist besser nur einmal, sie auszuführen. (6)
        length_left = len(left_arr)

        while l_index < length_left and r_index < length_rigth:
            if left_arr[l_index] <= right_arr[r_index]:
                arr[i_index] = left_arr[l_index] # Nur für einige Zeile ist das nicht sinvoll, eine Methode zu definieren. Deswegen sieht komplizierter aus. (4)
                l_index += 1
            else:
                arr[i_index] = right_arr[r_index]  # Nur für einige Zeile ist das nicht sinvoll, eine Methode zu definieren. Deswegen sieht komplizierter aus.
                r_index += 1
            i_index += 1

        while l_index < length_left:
            arr[i_index] = left_arr[l_index]
            l_index += 1
            i_index += 1

        while r_index < length_rigth:
            arr[i_index] = right_arr[r_index]
            r_index += 1
            i_index += 1


def plot_sort(arr):
    length_arr = range(len(arr))
    plt.bar(length_arr, arr)
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.title("Vor dem Sortieren")
    plt.show()

    merge_sort(arr)

    plt.bar(length_arr, arr)
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.title("Nach dem Sortieren")
    plt.show()
    
def main(): # Ich habe main Methode für Lesbarkeit betont.(10)
 my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
 plot_sort(my_list)

main()