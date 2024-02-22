def double_hashing(keys, hashtable_size, double_hash_value):
    hashtable_list = [None] * hashtable_size
    
    for i in range(len(keys)):
        hashkey = keys[i] % hashtable_size
        if hashtable_list[hashkey] is None:
            hashtable_list[hashkey] = keys[i]
        else:
            new_hashkey = hashkey
            while hashtable_list[new_hashkey] is not None:
                steps = double_hash_value - (keys[i] % double_hash_value)
                new_hashkey = (new_hashkey + steps) % hashtable_size
            hashtable_list[new_hashkey] = keys[i]
    return hashtable_list


values = [26, 22, 45, 54, 94, 17, 31, 77, 44, 51]
print( double_hashing(values, 13, 5) )