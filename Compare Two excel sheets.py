from itertools import zip_longest
import xlrd

rb1 = xlrd.open_workbook('excel1.xlsx')
rb2 = xlrd.open_workbook('excel2.xlsx')
sheet_names = rb1.sheet_names()
print('Sheet Names', sheet_names)
for i in range(len(sheet_names)):
    print()
    print('<--------------->','Excel Sheet Name:',sheet_names[i],'<------------------>')
    print()
    she1 = rb1.sheet_by_index(i)
    she2 = rb2.sheet_by_index(i)

    for rownum in range(max(she1.nrows, she2.nrows)):
        if rownum < she1.nrows:
            row_rb1 = she1.row_values(rownum)
            row_rb2 = she2.row_values(rownum)

            for colnum, (c1, c2) in enumerate(zip_longest(row_rb1, row_rb2)):
                if c1 != c2:
                    print("Row {} Col {} - {} != {}".format(rownum+1, colnum+1, c1, c2))
   
        else:
            print("Row {} missing".format(rownum+1))
    print()
