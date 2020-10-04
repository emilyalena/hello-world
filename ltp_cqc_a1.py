def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(50)
    1
    >>> num_buses(0)
    0
    >>> num_buses(51)
    2
    """
    if n % 50 > 0:
        min_required_buses = n // 50 + 1
    else:
        min_required_buses = n // 50
    
    return min_required_buses

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0])
    (0, 0)
    >>> stock_price_summary([.1,.03,.04])
    (0.17, 0)
    >>> stock_price_summary([-0.1,-.43,-.001])
    (0, -0.531)
    """
    gains = 0
    losses = 0
    for i in price_changes:
        if i > 0:
            gains = gains + i
        elif i < 0:
            losses = losses + i
    return (gains, losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    if k == 0:
        L = L
    else:
        L[:] = L[len(L)-k:]+L[k:-k]+L[:k]
                   
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
