def pick_peaks(arr):
    
    pos = []
    peaks = []
    curr = 0
    prev = 0
    
    for next in range(1, len(arr)):
        if arr[next] > arr[curr]:
            prev = curr
            curr = next
        else:
            if arr[next] < arr[curr]:
                if arr[prev] < arr[curr]:
                    pos.append(curr)
                    peaks.append(arr[curr])
                prev = curr
                curr = next
    return {"pos": pos, "peaks": peaks}