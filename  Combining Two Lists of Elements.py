def combine_element_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    for elem in combined:
        if not result:
            result.append(elem)
            continue

        prev = result[-1]
        l1, r1 = prev['positions']
        l2, r2 = elem['positions']

        overlap = min(r1, r2) - max(l1, l2)
        len2 = r2 - l2

        if overlap > 0 and overlap >= len2 / 2:
            merged_values = prev['values'] + elem['values']
            result[-1] = {
                'positions': prev['positions'],
                'values': merged_values
            }
        else:
            result.append(elem)

    return result

list1 = [{"positions": [0, 5], "values": [1, 2]}]
list2 = [{"positions": [3, 8], "values": [3, 4]}]
merged = combine_element_lists(list1, list2)
print("Merged List:", merged)
