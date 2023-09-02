def findMaxSubArray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = findMaxSubArray(A, low, mid)
        (right_low, right_high, right_sum) = findMaxSubArray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = findMaxCrossingSubArray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)