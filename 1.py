def rainfall(year):
    centimeter=[]
    count=0
    for i in range (year):
        for j in range(1,13):
            print('Enter the rainfall amount for the month{}: '.format(j))
            count +=1
            last= float(input())
            centimeter.append(last)
    totalrainfall= sum(centimeter)
    totalmonths=count
    return totalmonths, totalrainfall
year=int(input('Enter the number of years:'))
print('For Year-',year)
while year <= 0:
    year=int(input('Enter the number or years'))
totalmonths, totalrainfall = rainfall(year)
average= totalrainfall/totalmonths
print ('For {} Months'.format(totalmonths))
print ('Total rainfall:',totalrainfall ,'Centimeter')
print('Average Monthly rainfall:', totalrainfall/totalmonths ,'Centimeter')
    