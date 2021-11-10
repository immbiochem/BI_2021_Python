#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_file = input("Enter path to fastq file: ")
output_prefix = input("Enter file output prefix: ")
gc = [i for i in input("Enter GC threshold: ").split()]
length = [i for i in input("Enter length threshold: ").split()]
quality = [i for i in input("Enter quality threshold: ").split()]
save = input("Do you want to save failed reads (True/False)?: ")


def get_fastq_dictionary(path):
    with open(path, 'r') as f:
        fastq_list = []
        for line in f:
            fastq_list += [line.strip()]
    # LET'S SEPARATE THE TEXT INTO 4 GROUPS
    ind = []  # index
    seq = []  # the sequence
    third = []  # the third thing
    qual = []  # the sequence quality
    for i in fastq_list:
        if len(ind) == 0:
            ind += [i]
            continue
        elif len(ind) > len(seq):
            seq += [i]
            continue
        elif len(seq) > len(third):
            third += [i]
            continue
        elif len(third) > len(qual):
            qual += [i]
            continue
        else:
            ind += [i]
            continue
    fastq_dict = {}  # create a dictionary
    for i in range(len(ind)):
        fastq_dict[ind[i]] = [seq[i], third[i], qual[i]]  # key - index, everything else in the list by key
    return fastq_dict, ind


def gc_bounds_function(fastq_dict, fastq_keys, up=100, lo=0):
    if up > lo:
        up_broad = up  # upper bound
        low_broad = lo  # нижняя граница
    else:
        up_broad = lo  # upper bound
        low_broad = up  # нижняя граница
    gc_filtered_keys = []  # список фильтрованных ключей
    for i in fastq_keys:
        number_of_gc = (fastq_dict[i][0].count("G") + fastq_dict[i][0].count("C")) * 100 / len(
            fastq_dict[i][0])  # подсчет количества GC% для строки
        if low_broad < number_of_gc < up_broad:  # условия фильтрации по границам
            gc_filtered_keys.append(i)
    return gc_filtered_keys


def length_bounds_function(fastq_dict, keys, up=2 ** 32, lo=0):
    if up > lo:
        up_broad = up  # upper bound
        low_broad = lo  # lower bound
    else:
        up_broad = lo  # upper bound
        low_broad = up  # lower bound
    length_filter = []
    for i in keys:
        if up_broad > len(fastq_dict[i][0]) > low_broad:  # boundary filtering conditions
            length_filter += [i]
    return length_filter


def quality_threshold_function(fastq_dict, keys, n=0):
    filter_qual = []
    for i in keys:
        mean = 0
        for j in fastq_dict[i][2]:
            mean += ord(j) - 33  # amount for string
        if int(mean / len(fastq_dict[i][2])) > n:  # average for a row as a filtering condition
            filter_qual += [i]
    return filter_qual


def writer(output_file_prefix, prefix_filtered, fastq_dict, keys):
    with open(output_file_prefix + prefix_filtered, 'w') as ouf:
        for i in keys:
            ouf.write(i + '\n')
            for j in fastq_dict[i]:
                ouf.write(j + '\n')


def dop(output_file_prefix, prefix_failure, fastq_dict, keys):
    for i in keys:
        del fastq_dict[i]
    keys_resid = [i for i in fastq_dict.keys()]
    writer(output_file_prefix, prefix_failure, fastq_dict, keys_resid)


def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered="False"):
    # create dictionary and list of keys
    fast_dict, fast_keys = get_fastq_dictionary(input_fastq)
    print("Total number of reads: ", len(fast_keys))

    # filter by GC
    if len(gc_bounds) == 0:
        gc_keys = gc_bounds_function(fast_dict, fast_keys)
    elif len(gc_bounds) == 1:
        gc_keys = gc_bounds_function(fast_dict, fast_keys, up=int(gc_bounds[0]))
    else:
        gc_keys = gc_bounds_function(fast_dict, fast_keys, up=int(gc_bounds[0]), lo=int(gc_bounds[1]))
    print("The number of reads filtered by GC: ", len(gc_keys))

    # filter by length    
    if len(length_bounds) == 0:
        len_keys = length_bounds_function(fast_dict, gc_keys)
    elif len(length_bounds) == 1:
        len_keys = length_bounds_function(fast_dict, gc_keys, up=int(length_bounds[0]))
    else:
        len_keys = length_bounds_function(fast_dict, gc_keys, up=int(length_bounds[0]), lo=int(length_bounds[1]))
    print("Number of reads filtered by length: ", len(len_keys))

    # filter by quality
    if len(quality_threshold) == 0:
        qual_keys = quality_threshold_function(fast_dict, len_keys)
    else:
        qual_keys = quality_threshold_function(fast_dict, len_keys, n=int(quality_threshold[0]))
    print("Number of reads filtered by quality: ", len(qual_keys))

    # write the results to a file                                       
    writer(output_file_prefix, "_passed.fastq", fast_dict, qual_keys)
    print("Passed file is written")

    # additional option                                      
    if save_filtered == "True":
        dop(output_file_prefix, "_failed.fastq", fast_dict, qual_keys)
        print("Failed file is written")

    # successful completion of work                                      
    print("Work done")


main(input_file, output_prefix, gc, length, quality, save)

# In[ ]:
