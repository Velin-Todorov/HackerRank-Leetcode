#!/usr/bin/python3


def toh(N, fromm, to, aux):
    """
    
    fromm - the rod from which we move
    to - to which rod we move
    aux - helper rod


    """
    print(N) 
    if N == 1:
        print(f'Move disk {N} from {fromm} to {to}')
        return

    else:
        toh(N-1, fromm, aux, to)
        print(f'Move disk {N} from {fromm} to {to}')
        toh(N-1, aux, to, fromm)
 
toh(2, 1, 3, 2)
