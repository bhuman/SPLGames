import csv
import os 



def no_break(s):
    return s.replace(' ',u'\u00A0')
            .replace('-',u"\u2011")
            .encode().decode('unicode-escape').encode('latin1').decode('utf-8')

def link(name, url):
    if url is None or len(url) == 0:
        return ""
    else:
        return f"[{name}]({url}) "

with open('videos_and_logs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    with open('README.md', 'w', encoding='utf8') as readme:
        
        readme.write("| Event | Time | F | ½ | # | Team A | Team B | Video | GC Log | TCM Log |\n")
        readme.write("|:--|:--|:--:|:--:|:--:|:--|:--|:--:|:--:|:--:|\n")
        
        for row in reader:
        
            event    = no_break(row['Event'])
            time     = no_break(row['Time'])
            field    = row['Field'] 
            half     = row['Half']
            part     = row['Part']
            
            teamA    = no_break(row['Team A'])
            teamB    = no_break(row['Team B'])
            
            video    = link("video", row['Video'])
            gc       = link("GC", row['GC Log'])
            tcm      = link("TCM", row['TCM Log'])
            
            readme.write(f"| {event} | {time} | {field} | {half} | {part} | {teamA} | {teamB} | {video}| {gc}| {tcm}|\n")