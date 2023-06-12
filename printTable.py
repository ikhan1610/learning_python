# Print list of items in well organized table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

newTableData = [[],[],[]]
def printTable(tableData):
    colWidths = [0] * len(tableData)

    #Find the maximum width of the column to pass to right justify
    for i in range(len(tableData)):
        longestString = tableData[i][0]
        for j in range(len(tableData[i])):
            if (j+1) < len(tableData[i]):
                if len(longestString) < len(tableData[i][j+1]):
                    longestString = tableData[i][j+1]
        colWidths[i] = len(longestString)
    maxColWidth = max(colWidths)

    #Filling the original table with right justified table values
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            tableData[i][j] = tableData[i][j].rjust(maxColWidth)

    #Printing the values in tabular format

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i],end='')
        print('\n')




printTable(tableData)
