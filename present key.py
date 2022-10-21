dic1={'key1': 1, 'key2': 3, 'key3': 2}
dic2={'key1': 1, 'key2': 2}
for x in dic1:
        if x in dic2:
            print(x," is present in both dic1 and dic2")