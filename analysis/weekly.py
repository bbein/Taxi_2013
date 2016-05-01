import header

con = lite.connect('Taxi_Fare.db')

with con:
    
    cur = con.cursor()    
    #Find the fraction of the most common type and suprising event types
    cur.execute("SELECT payment_type, pickup_datetime, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount FROM Taxi_Fare WHERE total_amount != 0")
    row = cur.fetchone()
    data = {}
    while row:
        if row[3] == 0:
            print 'error total amount = 0'
            break
        time = convert_timestamp(row[1])
        if not(row[0] in data):
            data[row[0]] = [[0]*9 for x in range(7*24*60)]
        data[row[0]][time][0] += 1 #total number of transactions
        if row[6] != 0:
            data[row[0]][time][1] += 1 #total number of tipping transactions
            data[row[0]][time][2] += row[2] #tipped fares
        data[row[0]][time][3] += row[2]#total amount fares
        data[row[0]][time][4] += row[3]#total amount of surcharges
        data[row[0]][time][5] += row[4]#total amount of MTA Tax
        data[row[0]][time][6] += row[5]#total amount of tips
        data[row[0]][time][7] += row[6]#total amount of tolls
        data[row[0]][time][8] += row[7]#total amount of charges
        row = cur.fetchone()

path = 'data/weekly.dat'
file = open(path, 'w+')
json.dump(data, file)