def tabla():
    i = 1
    for i in range(1,10):
        j = 1
        print(f"\nTabla del {i}:\n")
        for j in range(1,12):
            print(f"{i} X {j} = {i*j}")
            j += 1
        i += 1

tabla()