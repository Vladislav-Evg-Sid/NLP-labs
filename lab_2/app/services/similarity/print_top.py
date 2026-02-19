def print_top(tops, data_1, data_2):
    print("*" * 100)
    for i in range(len(tops)):
        print(f"name: {data_2.iloc[i][0]}\ndiscription: {data_2.iloc[i][1]}")
        for j in range(len(tops[i])):
            print(
                f"\tname: {data_1.iloc[tops[i][j][0]][0]}\n\tdiscription: {data_1.iloc[tops[i][j][0]][1]}"
            )
    print("=" * 100)
