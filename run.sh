#! /usr/bin/bash
cd backend_news/newsman

function scrap_data(){
    scrapy crawl newsman -O news.json
    python3 dataExtracter.py
}

now1=$(date +%s)
now1_1=$(date '+%Y-%m-%d %H:%M:%S')
echo $now1_1

scrap_data #intial run

now2=$(date +%s)
now2_1=$(date '+%Y-%m-%d %H:%M:%S')
echo $now2_1

let MPHR=60
MINUTES=$(( ($now2 - $now1) / $MPHR ))
echo "differece: $MINUTES"

while true
do
	sleep 1h 45m
    scrap_data
done