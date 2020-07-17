import os
from pathlib import Path
from datetime import datetime

print(datetime.date(datetime.now()))

appsPath = "/home/wd3bbas/Downloads/"
todayappsPath = os.path.join(appsPath,str(datetime.date(datetime.now()))+"/")

print(todayappsPath)

Rules = [
    {
        "directory": 'Applications',
        "ext": ['.deb','.exe','.run']
    },
    {
        "directory": 'Sh',
        "ext": ['.sh']
    },
    {
        "directory": 'pdf',
        "ext": ['.pdf']
    },
    {
        "directory": 'data',
        "ext": ['.json']
    }
]

for filename in os.listdir(appsPath):
    if os.path.isfile(os.path.join(appsPath,filename)):
        for rule in Rules:
            if Path(filename).suffix in rule['ext']:
                if not os.path.exists(os.path.join(todayappsPath,rule['directory'])):
                    os.makedirs(os.path.join(todayappsPath,rule['directory']))
                    os.rename(os.path.join(appsPath,filename),os.path.join(todayappsPath,rule['directory']+'/',filename))
                else:
                    os.rename(os.path.join(appsPath,filename),os.path.join(todayappsPath,rule['directory']+'/',filename))