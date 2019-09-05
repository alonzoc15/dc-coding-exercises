def de_dup(list_to_dedup):
    unique_items = []
    for item in list_to_dedup:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print(de_dup(['dog','cat','mouse','cat','car'])) 