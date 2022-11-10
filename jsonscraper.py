import datetime
import glob
import json

def get_results_files(server_results_path):
    ftype = r'\*json'
    files = glob.glob(server_results_path+ftype)
    return files

def scrape_results(result_files):
    guid_list = []
    with open("json/entries.json", "r") as entries:
        drivers = json.load(entries)
        for d in drivers:
            if d['guid']:
                guid_list.append(d['guid'])
    for f in result_files:
        with open (f, 'r') as result:
            r = json.load(result)
            for g in guid_list:
                for l in r['Laps']:
                    if int(l['DriverGuid']) == g:
                        if l['Cuts'] == 0:
                            laptime = datetime.datetime.strptime(str(datetime.timedelta(milliseconds=int(l['LapTime']))),"%H:%M:%S.%f").strftime("%M:%S.%f")[:-3]
                            s1 = datetime.datetime.strptime(str(datetime.timedelta(milliseconds=int(l['Sectors'][0]))),"%H:%M:%S.%f").strftime("%M:%S.%f")[:-3]
                            s2 = datetime.datetime.strptime(str(datetime.timedelta(milliseconds=int(l['Sectors'][1]))),"%H:%M:%S.%f").strftime("%M:%S.%f")[:-3]
                            s3 = datetime.datetime.strptime(str(datetime.timedelta(milliseconds=int(l['Sectors'][2]))),"%H:%M:%S.%f").strftime("%M:%S.%f")[:-3]
                            print(l['DriverName'], "-", laptime ,"-", 'S1:', s1,"-", 'S2:', s2 ,"-", 'S3:', s3, 'Cuts:', l['Cuts'])