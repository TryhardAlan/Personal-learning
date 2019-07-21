# 9*9 table
line = 1    # 9 lines
while line <= 10:
    row = 1
    while row <= line:
        print("%d * %d = %d" % (row, line, row*line), end="\t\t")
        row += 1
    print("")
    line += 1