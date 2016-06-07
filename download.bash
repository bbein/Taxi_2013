#!/bin/bash
source1="https://storage.googleapis.com/tlc-trip-data/"
source2="https://nyctaxitrips.blob.core.windows.net/data/trip_fare_"
target="./raw_data/"

#make directory i it doesn't exists
mkdir -p -- "$target"
#download fare data for 2013
for month in {1..12}
do
	wget -O "${target}trip_fare_${month}.csv.zip" "${source2}${month}.csv.zip"
	unzip "${target}trip_fare_${month}.csv.zip" -d "${target}"
	rm "${target}trip_fare_${month}.csv.zip"
done
#download trip data for yellow and green cabs
for year in {2009..2015}
do
	for month in {01..12} 
	do
		wget -O "${target}yellow_tripdata_${year}-${month}.csv" "${source1}${year}/yellow_tripdata_${year}-${month}.csv"
		if (($year > 2013 )) || (( $year == 2013 && $((10#$month)) > 7 ))
		then
			wget -O "${target}green_tripdata_${year}-${month}.csv" "${source1}${year}/green_tripdata_${year}-${month}.csv"
		fi
	done
done
 
	
