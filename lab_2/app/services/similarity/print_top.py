def print_top(tops, data_1, data_2):
    print("*" * 100)
    for i in range(len(tops)):
        print(f"""name: {data_2['original_title'][i]}\ndiscription: {data_2['overview'][i]}""")
        for j in range(len(tops[i])):
            print(
                f"""\tname: {data_1['original_title'][tops[i][j][0]]}\n\tdiscription: {data_1['overview'][tops[i][j][0]]}"""
            )
    print("=" * 100)
