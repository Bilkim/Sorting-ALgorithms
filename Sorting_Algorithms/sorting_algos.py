import csv
import time
import json
import pandas as pd
from operator import itemgetter

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']


#############################################################################################################
# Data Filtering
#############################################################################################################
def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    df = pd.read_csv("imdb_dataset.csv")# Load the imdb_dataset.csv dataset
    df['primaryTitle'] = df['primaryTitle'].apply(str.strip)
    if(num==1):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        filter = (df['startYear'] >= 1941) & (df['startYear'] <= 1955)
        df_year = df.loc[filter]#Store your filtered dataframe here
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)

    if(num==2):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on genres (genres are either ‘Adventure’ or ‘Drama’)
        df_genres = df.loc[df['genres'].isin(['Adventure', 'Drama'])]#Store your filtered dataframe here
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
    if(num==3):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primaryProfession (if primaryProfession column contains
        #substrings {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        substrings = ['assistant_director', 'casting_director', 'art_director', 'cinematographer']
        df_professions = df.loc[df['primaryProfession'].str.contains("|".join(substrings))]#Store your filtered dataframe here
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
    if(num==4):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primary Names which start with vowel character.
        vow = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        df_vowels = df[df['primaryName'].str.startswith(tuple(vow))]#Store your filtered dataframe here
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)


#############################################################################################################
#Quick Sort
#############################################################################################################
def pivot_element(arr):
    #CODE For identifiying the pivot element
    pivot = arr[len(arr)//2] # Middle element array as pivot
    return pivot
def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the sorted_res of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        return arr
    pivot = pivot_element(arr)
    pivot = tuple(pivot[i] for i in columns)

    # Split the array into three parts
    left = []
    middle = []
    right = []
    for row in arr:
        row_tuple = tuple(row[i] for i in columns)
        if row_tuple < pivot:
            left.append(row)
        elif row_tuple == pivot:
            middle.append(row)
        else:
            right.append(row)

    # Recursively sort the left and right subarrays
    sorted_left = quicksort(left, columns)
    sorted_right = quicksort(right, columns)
    
    arr = sorted_left + middle + sorted_right
    #Implement Quick Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            for idx in columns:
                if arr[j][idx] < arr[min][idx]:
                    min = j
                    break
                elif arr[j][idx] > arr[min][idx]:
                    break
        arr[i], arr[min] = arr[min], arr[i]
    #Implement Selection Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Heap Sort
#############################################################################################################
def max_heapify(arr, n, i, columns):
    """
    arr: the input array that represents the binary heap
    n: The number of elements in the array
    i: i is the index of the node to be processed
    columns: The columns to be used for comparison

    The max_heapify function is used to maintain the max heap property
    in a binary heap. It takes as input a binary heap stored in an array,
    and an index i in the array, and ensures that the subtree rooted at
    index i is a max heap.
    """
    L = 2 * i + 1
    R = 2 * i + 2
    columns_tuple = tuple(columns)
    idx_val = i

    for idx, child in enumerate([L, R]):
        if child < n and tuple(arr[child][col] for col in columns_tuple) > tuple(arr[idx_val][col] for col in columns_tuple):
            idx_val = child

    if idx_val != i:
        arr[i], arr[idx_val] = arr[idx_val], arr[i]
        max_heapify(arr, n, idx_val, columns)


def build_max_heap(arr, columns):
    """
    arr: The input array to be transformed into a max heap
    n: The number of elements in the array
    i: The current index in the array being processed
    columns: The columns to be used for comparison

    The build_max_heap function is used to construct a max heap
    from an input array.
    """
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i, columns)
    #Implement heapify algorithm here

def heap_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    build_max_heap(arr, columns)
    length = len(arr)
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0, columns)
    #Implement Heap Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Shell Sort
#############################################################################################################
def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    array_length = len(arr)
    gap = array_length // 2
    key_function = itemgetter(*columns)
    while gap > 0:
        for i in range(gap, array_length):
            temp = arr[i]
            j = i
            while j >= gap and key_function(arr[j - gap]) > key_function(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    #Implement Shell Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Merge Sort
#############################################################################################################
def merge(left, right, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the sorted_res
    with the remaining elements of the other sub-array and returns the sorted_res as the final
    sorted 2D array.
    """
    sorted_res = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        left_val = tuple(left[i][c] for c in columns)
        right_val = tuple(right[j][c] for c in columns)
        if left_val <= right_val:
            sorted_res[k] = left[i]
            i += 1
        else:
            sorted_res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sorted_res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_res[k] = right[j]
        j += 1
        k += 1
        
    return sorted_res
    #Implement merge Logic
    #return Sorted array

def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the sorted_res of the merge operation as the final sorted 2D array.
    """
    #NEED TO CODE
    if len(data) <= 1:
        return data
    mid = len(data) // 2 #Mid value
    left = merge_sort(data[:mid], columns)
    right = merge_sort(data[mid:], columns)
    #Implement Merge Sort Algorithm
    #return Sorted array
    return merge(left, right, columns)
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    def is_less_than(arr1, arr2, columns):
        for col in columns:
            if arr1[col] < arr2[col]:
                return True
            elif arr1[col] > arr2[col]:
                return False
        return False
    
    for i in range(1, len(arr)):
        j = i
        while j > 0 and is_less_than(arr[j], arr[j-1], columns):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    #Insertion Sort Implementation
    #Return : List of tconst values which are obtained after sorting the dataset.
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    """
    # file_path: a string representing the path to the CSV file
    # columns: a list of strings representing the columns to sort the 2D array on
    # select: an integer representing the sorting algorithm to be used

    # colum_vals: is a list of integers representing the indices of the specified columns to be sorted.

    # data: is a 2D array of values representing the contents of the CSV file, with each row in
    the array corresponding to a row in the CSV file and each element in a row corresponding to a value
    in a specific column.

    More Detailed Description:

    df= #read imdb_dataset.csv data set using pandas library

    column_vals = #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).
    """
    #NEED TO CODE
    #Read imdb_dataset.csv
    #write code here Inorder to read imdb_dataset
    df= pd.read_csv(file_path)#read imdb_dataset.csv data set using pandas library
    df['primaryTitle'] = df['primaryTitle'].apply(str.strip)
    
    vals = []
    for c in columns:
        index = column_names.index(c)
        vals.append(index)

    column_vals = vals#convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = df.values.tolist()#convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).

#############################################################################################################
# Donot Modify Below Code
#############################################################################################################
    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
