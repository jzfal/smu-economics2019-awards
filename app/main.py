from pytube import YouTube
import csv
import srt
from datetime import timedelta
import pandas as pd


def extract_to_csv(URL = 'https://www.youtube.com/watch?v=4HgRQT6qDto', start = (0, 16,35) , end = (1,9,0) , filename = 'all_subs1.csv'):

    """
    default url is commencement for econs 
    """
    yt = YouTube(URL)
    en_captions = yt.captions.get_by_language_code('en')
    subs = list(srt.parse(en_captions.generate_srt_captions())) # generate list of tuples

    # find start and end index
    start_index = 0
    for i in range(len(subs)):
        if subs[i].start  < timedelta(hours = start[0],minutes = start[1], seconds = start[2]):
            continue
        else:
            start_index = i
            break
    end_index = 0
    for i in range(start_index,len(subs)):
        if subs[i].start > timedelta(hours = end[0], minutes = end[1],
        seconds= end[2]):
            end_index = i
            break
    content_dict = {'content':[]}
    for i in range(start_index, end_index +1):
        content_dict['content'].append(subs[i].content)

    df1 = pd.DataFrame(data = content_dict)
    df1.to_csv(filename, index = False)


if __name__ == "__main__":
    # to find data for law commencement 
    extract_to_csv(URL = 'https://www.youtube.com/watch?v=jTk1yuiUnvE',
    start = (0, 46, 25), end=(1,15,48), filename= 'law_commencement_2019.csv')