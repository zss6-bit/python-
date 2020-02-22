def multiple_table():
    
    #1. 打印 9 行小星星
    row = 1

    while row <= 9:

        col = 1

        while col <= row:

            print("%d * %d = %d" % (col, row , col * row),end=" "  )

            col += 1

        #print("%d" % row)
        print("")

        row += 1