from pytube import YouTube
import csv
import srt
from datetime import timedelta
import pandas as pd



yt = YouTube('https://www.youtube.com/watch?v=4HgRQT6qDto')
en_captions = yt.captions.get_by_language_code('en')
subs = list(srt.parse(en_captions.generate_srt_captions())) # generate list of tuples




# find start and end index
start_index = 0
for i in range(len(subs)):
    if subs[i].start  < timedelta(minutes = 16, seconds = 35):
        continue
    else:
        start_index = i
        break
end_index = 0
for i in range(start_index,len(subs)):
    if subs[i].start > timedelta(hours = 1, minutes = 9):
        end_index = i
        break
# print(subs[start_index])
# print(subs[end_index])

content_dict = {'content':[]}
for i in range(start_index, end_index +1):
    content_dict['content'].append(subs[i].content)


df1 = pd.DataFrame(data = content_dict)
df1.to_csv('all_subs.csv', index = False)
# write func
def write_to_csv():
    with open('all_subs.csv','w') as outfile:
        spamwriter = csv.writer(outfile, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for i in range(start_index, end_index):
            spamwriter.writerow(subs[i].content)





