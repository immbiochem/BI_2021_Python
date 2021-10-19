#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#MAIN


input_fastq = str(input("Введите аргумент input_fastq: "))
output_file_prefix = str(input("Введите аргумент output_file_prefix: "))
prefix_filtered = "_passed.fastq"
prefix_failure = "_failed.fastq"
quality_threshold = int(input("Введите аргумент quality_threshold: "))
gc_bounds = [int(i) for i in input("Введите аргумент gc_bounds: ").split()]
length_bounds = [int(i) for i in input("Введите аргумент length_bounds: ").split()]
save_filtered = input("Введите аргумент save_filtered: ")


def gc_bounds1(up=100, lo=0):
    if up > lo:
        up_broad = up  # верхняя граница
        low_broad = lo  # нижняя граница
    else:
        up_broad = lo  # верхняя граница
        low_broad = up  # нижняя граница
    numbers_of_reads = []  
    counter = 0
    for i in SEQ[0::2]:  # ЗДЕСЬ ИСХОДНЫЕ ДАННЫЕ УЖЕ ПЕРЕПИСАНЫ КАК k
        counter += 1
        num = (i.count("G") + i.count("C")) * 100 / len(i)  # подсчет количества GC% для строки
        if num < up_broad and num > low_broad:  # условия фильтрации по границам
            numbers_of_reads += [counter]
    return (numbers_of_reads)


def length_bounds1(up=2 ** 32, lo=0):
    if up > lo:
        up_broad = up  # верхняя граница
        low_broad = lo  # нижняя граница
    else:
        up_broad = lo  # верхняя граница
        low_broad = up  # нижняя граница
    length_filter = []
    for i in gc_filter:
        if len(seq_and_numbers[i]) < up_broad and len(seq_and_numbers[i]) > low_broad:  # условия фильтрации по границам
            length_filter += [i]
    return (length_filter)


def SEQ_f(input_fastq):
    # 1 STEP
    with open(input_fastq, 'r') as f:
        SEQ = []
        count = 0
        for line in f:
            count += 1
            if count % 2 == 0:  # создаем список где последовательность-качество последовательности чередуются
                SEQ += [line.strip()]
    return (SEQ)


def SAN_f(SEQ):
    # ПРЕДПОДГОТОВКА 1
    # получаем срезы последовательностей с помощью шагов - у последовательностей код n = 0, у качества n = 1
    seq_and_numbers = {}  # создаем словарик, где номеру последовательности соответствует строка с буквами
    counter = 0
    for i in SEQ[0::2]:
        counter += 1
        seq_and_numbers[counter] = i
    return (seq_and_numbers)


def SANQ_f(SEQ):
    # ПРЕДПОДГОТОВКА 2
    # получаем срезы последовательностей с помощью шагов - у последовательностей код = 0, у качества = 1
    seq_and_numbers_qual = {}  # создаем словарик, где номеру последовательности соответствует строка с качеством
    counter = 0
    for i in SEQ[1::2]:
        counter += 1
        seq_and_numbers_qual[counter] = i
    return (seq_and_numbers_qual)


def quality_threshold1(n=0):
    # filtered_reads_quality_threshold = []
    filter_qual = []
    for i in length_filter:  # выбираем строки с предыдущих фильтраций
        mean = 0
        for j in seq_and_numbers_qual[i]:
            mean += ord(j) - 33  # сумма для строки
        if mean / len(seq_and_numbers_qual[i]) > n:  # среднее для строки как условие фильтрации
            # filtered_reads_quality_threshold += [i]
            filter_qual += [i]
            # return(filtered_reads_quality_threshold)
    return (filter_qual)


def FILTRED_FASTQ1(input_fastq, list_of_numbers_for_filtered_reads):
    # ПРЕДПОДГОТОВКА 3
    # ПОЛНОСТЬЮ СНОВА ИСПОЛЬЗУЕМ ВЕСЬ ФАЙЛ
    with open(input_fastq, 'r') as f:
        k0 = []
        count = 0
        for line in f:
            k0 += [line.strip()]
            # РАЗОБЪЕМ ТЕКСТ НА 4 ГРУППЫ
    ind = []  # индекс
    seq = []  # сама последовательность
    third = []  # третья штука, служебная которая
    qual = []  # качество последовательности
    for i in k0:
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
    # СОЕДИНИМ ВСЕ ФИЛЬТРОВАННЫЕ РИДЫ:
    FILTRED_FASTQ = []
    for i in list_of_numbers_for_filtered_reads:
        FILTRED_FASTQ += [ind[i]]
        FILTRED_FASTQ += [seq[i]]
        FILTRED_FASTQ += [third[i]]
        FILTRED_FASTQ += [qual[i]]
    return (FILTRED_FASTQ)


def writer(output_file_prefix, prefix_filtered, FILTRED_FASTQ):
    # ЗАПИСЫВАЕМ В ФАЙЛ _passed.fastq
    with open(output_file_prefix + prefix_filtered, 'w') as ouf:
        for line in FILTRED_FASTQ:
            ouf.write(line + '\n')


def dop(save_filtered, list_of_numbers_for_filtered_reads, output_file_prefix, prefix_failure, input_fastq):
    # ДОПОЛНИТЕЛЬНАЯ ОПЦИЯ
    if save_filtered == True:
        # ПОЛНОСТЬЮ СНОВА ИСПОЛЬЗУЕМ ВЕСЬ ФАЙЛ
        with open(input_fastq, 'r') as f:
            k0 = []
            count = 0
            for line in f:
                k0 += [line.strip()]
                # РАЗОБЪЕМ ТЕКСТ НА 4 ГРУППЫ
        ind = []  # индекс
        seq = []  # сама последовательность
        third = []  # третья штука, служебная которая
        qual = []  # качество последовательности
        for i in k0:
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
        # НЕПРОШЕДШИЕ РИДЫ
        for i in list_of_numbers_for_filtered_reads:  # удалим прошедшие
            ind.remove(ind[i])
            seq.remove(seq[i])
            third.remove(third[i])
            qual.remove(qual[i])
        FAILED_READS = []  # соединим непрошедшие
        for i in range(len(ind)):
            FAILED_READS += [ind[i]]
            FAILED_READS += [seq[i]]
            FAILED_READS += [third[i]]
            FAILED_READS += [qual[i]]
        # ЗАПИШЕМ В ФАЙЛ _failed.fastq    
        with open(output_file_prefix + prefix_failure, 'w') as ouf:
            for line in FAILED_READS:
                ouf.write(line + '\n')


def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold=0, save_filtered=False):
    # 1 STEP создаем последовательность
    SEQ = SEQ_f(input_fastq)
    seq_and_numbers = SAN_f(
        SEQ)  # ПРЕДПОДГОТОВКА 1 получаем срезы последовательностей с помощью шагов - у последовательностей код n = 0, у качества n = 1
    seq_and_numbers_qual = SANQ_f(
        SEQ)  # ПРЕДПОДГОТОВКА 2 получаем срезы последовательностей с помощью шагов - у последовательностей код = 0, у качества = 1

    # 2 STEP >> gc_bounds
    if len(gc_bounds) == 2:
        up_gc = gc_bounds[0]
        lo_gc = gc_bounds[1]
    elif len(gc_bounds) == 1:
        up_gc = gc_bounds[0]
        lo_gc = 0
    else:
        up_gc = 100
        lo_gc = 0
    # переменная
    gc_filter = gc_bounds1(up_gc, lo_gc)

    # 3 STEP >>> length_bounds
    if len(length_bounds) == 2:
        up_lb = length_bounds[0]
        lo_lb = length_bounds[1]
    elif len(length_bounds) == 1:
        up_lb = length_bounds[0]
        lo_lb = 0
    else:
        up_lb = 100
        lo_lb = 0
    # переменная
    length_filter = length_bounds1(up_lb, lo_lb)

    # 4 STEP >>>> quality_threshold
    list_of_numbers_for_filtered_reads = quality_threshold1(quality_threshold)  # масло масленное -_-

    # 5 STEP ЗАПИСЬ В ФАЙЛ
    FILTRED_FASTQ = FILTRED_FASTQ1(input_fastq, list_of_numbers_for_filtered_reads)
    writer(output_file_prefix, prefix_filtered, FILTRED_FASTQ)

    # 6 STEP ДОПОЛНИТЕЛЬНАЯ ОПЦИЯ
    dop(save_filtered, list_of_numbers_for_filtered_reads, output_file_prefix, prefix_failure, input_fastq)

    # 7 STEP
    print("Good job!")
