from header import *

#load the data
f = open('../data/weekly.dat','r')
data = json.load(f)
f.close()

#Constants
averaging = 60 #this is used to average the minute data to hourly data
tix_lables=('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', '')


###############################
# Number of transactions plot #
###############################

fig = plt.figure(figsize=(14,9), dpi=100) #create a figure
#add an axes to your figure
axes = fig.add_axes([0.18, 0.11, 0.65, 0.78]) # left, bottom, width, height (range 0 to 1)
#plot something in your axes
for key in data.iterkeys():
    if key == 'CSH':
        label = 'Cash'
    elif key == 'CRD':
        label = 'Credit Card'
    else:
        continue
    y = []
    ys = 0
    count = 0
    for x in data[key]:
        count += 1
        ys +=float(x[0])
        if count == averaging:
            y.append(ys/52)
            count = 0
            ys = 0
    axes.plot([float(x)/(24*60)*averaging for x in range(len(y))],y,label = label,ls='-', lw=7) #list of x values, list of y values


axes.set_xlabel('', fontsize=45) #define the x label
axes.set_ylabel('# of Transactions per hour', fontsize=45) #define the y label
axes.set_title('', fontsize=55) #define title
axes.set_xlim(0,7)
axes.grid(True) #add grid lines to guide the eye
axes.legend(bbox_to_anchor=(1.28, 0.97), fontsize=40, numpoints=1,markerscale=3)# add the legend
#reset tix
tix=axes.get_xticks().tolist()
for i in range(len(tix)):
    tix[i] = tix_lables[i]
axes.set_xticklabels(tix)

#increase the tick label font size
for tick in axes.xaxis.get_major_ticks():
    tick.label.set_fontsize(40)
for tick in axes.yaxis.get_major_ticks():
    tick.label.set_fontsize(40)
#Use the show command to show the plot    
#plt.show()

#Use the save command to save the plot
plt.savefig('transactions.png')

######################
# Tip % of fare plot #
######################

fig = plt.figure(figsize=(14,8), dpi=100) #create a figure
#add an axes to your figure
axes = fig.add_axes([0.1, 0.1, 0.85, 0.8]) # left, bottom, width, height (range 0 to 1)
#plot something in your axes
for key in data.iterkeys():
    if key == 'CRD':
        label = 'Credit Card'
    else:
        continue
    y = []
    ys = 0
    ys2 = 0
    count = 0
    for x in data[key]:
        count += 1
        if x[2] > 0:
            ys +=float(x[6])
            ys2 += float(x[2])
        if count == averaging:
            y.append(ys/ys2*100)
            count = 0
            ys = 0
            ys2 = 0
    axes.plot([float(x)/(24*60)*averaging for x in range(len(y))],y,label = label,ls='-', lw=7) #list of x values, list of y values


axes.set_xlabel('', fontsize=45) #define the x label
axes.set_ylabel('int[%]', fontsize=45) #define the y label
axes.set_title('', fontsize=55) #define title
axes.set_xlim(0,7)
axes.set_ylim(18,21.5)
axes.grid(True) #add grid lines to guide the eye
axes.legend(loc = 4, fontsize=40, numpoints=1,markerscale=3)# add the legend
#reset tix
tix=axes.get_xticks().tolist()
for i in range(len(tix)):
    tix[i] = tix_lables[i]
axes.set_xticklabels(tix)

#increase the tick label font size
for tick in axes.xaxis.get_major_ticks():
    tick.label.set_fontsize(40)
for tick in axes.yaxis.get_major_ticks():
    tick.label.set_fontsize(40)
    
#Use the show command to show the plot    
#plt.show()

#Use the save command to save the plot
plt.savefig('tip.png')

#############################
# % of tipping transactions #
#############################

fig = plt.figure(figsize=(14,8), dpi=100) #create a figure
#add an axes to your figure
axes = fig.add_axes([0.1, 0.1, 0.85, 0.8]) # left, bottom, width, height (range 0 to 1)
#plot something in your axes
for key in data.iterkeys():
    if key == 'CRD':
        label = 'Credit Card'
    else:
        continue
    y = []
    ys = 0
    count = 0
    for x in data[key]:
        count += 1
        if x[0] > 0:
            ys +=float(x[1])/x[0]
        if count == averaging:
            y.append(ys/averaging*100)
            count = 0
            ys = 0
    axes.plot([float(x)/(24*60)*averaging for x in range(len(y))],y,label = label,ls='-', lw=7) #list of x values, list of y values


axes.set_xlabel('', fontsize=45) #define the x label
axes.set_ylabel('% of costumers who tip', fontsize=45) #define the y label
axes.set_title('', fontsize=55) #define title
axes.set_xlim(0,7)
axes.grid(True) #add grid lines to guide the eye
axes.legend(loc = 3, fontsize=40, numpoints=1,markerscale=3)# add the legend
#reset tix
tix=axes.get_xticks().tolist()
for i in range(len(tix)):
    tix[i] = tix_lables[i]
axes.set_xticklabels(tix)

#increase the tick label font size
for tick in axes.xaxis.get_major_ticks():
    tick.label.set_fontsize(40)
for tick in axes.yaxis.get_major_ticks():
    tick.label.set_fontsize(40)
    
#Use the show command to show the plot    
#plt.show()

#Use the save command to save the plot
plt.savefig('tiping.png')

################
# Some numbers #
################

total_trips = [0,0,0,0,0]
total_tiped_trips = [0,0,0,0,0]
total_fare = [0]*5
total_tipped_fare = [0]*5
total_surcharges = [0]*5
total_tax = [0]*5
total_tips = [0]*5
total_tolls = [0]*5
total_charges = [0]*5
for i in range(len(data['CSH'])):
    for j,key in enumerate(data.iterkeys()):
        total_trips[j] += data[key][i][0]
        total_tiped_trips[j] += data[key][i][1]
        total_tipped_fare[j] += data[key][i][2]
        total_fare[j] += data[key][i][3]
        total_surcharges[j] += data[key][i][4]
        total_tax[j] += data[key][i][5]
        total_tips[j] += data[key][i][6]
        total_tolls[j] += data[key][i][7]
        total_charges[j] += data[key][i][8]

print 'total trips:'+str(sum(total_trips))
print 'total tipped trips:'+str(sum(total_tiped_trips))
print 'total fare:'+str(sum(total_fare))
print 'total surcharges:'+str(sum(total_surcharges))
print 'total tax:'+str(sum(total_tax))
print 'total tips:'+str(sum(total_tips))
print 'total tolls:'+str(sum(total_tolls))
print 'total charges:'+str(sum(total_charges))

print '% of tipped trips: ' +str(sum(total_tiped_trips)/float(sum(total_trips)))
print '% of credit card trips: ' +str(total_trips[3]/float(sum(total_trips)))
print '% of cash trips: ' +str(total_trips[2]/float(sum(total_trips)))
print '% of tipped credit card trips: ' +str((total_tiped_trips[3])/float((total_trips[3])))
print '% of tipped cash trips: ' +str((total_tiped_trips[2])/float((total_trips[2])))

print 'tip % of fare of credit card trips that where tipped: ' + str(total_tips[3]/total_tipped_fare[3])
