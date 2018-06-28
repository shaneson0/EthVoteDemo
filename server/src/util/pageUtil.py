# coding=utf-8
import math

def pageing(maxnum, pagesize, currentpage):
    pagenum = math.ceil(maxnum/pagesize)
    if currentpage < 1 or currentpage > pagenum:
        return False, -1, -1
    ffrom = pagesize * ( currentpage - 1 )
    return True, ffrom, pagesize



