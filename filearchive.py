import os
from pathlib import Path
from datetime import datetime

appsPath = "/home/sample/Downloads/"
todayappsPath = os.path.join(appsPath,str(datetime.date(datetime.now()))+"/")

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
    },
    {
        "directory": 'compressed',
        "ext": ['.gz','.zip','.7z','.rar','.bz2']
    },
    {
        "directory": 'Selenium',
        "ext": ['.side']
    },
    {
        "directory": 'Python',
        "ext": ['.py']
    }
    ,
    {
        "directory": 'Emails',
        "ext": ['.msg','.eml']
    },
    {
        "directory": 'Excel',
        "ext": ['.xlsx']
    },
    {
        "directory": 'MS Word',
        "ext": ['.docx']
    },
    {
        "directory": 'csv',
        "ext": ['.csv']
    },
    {
        "directory": 'Images',
        "ext": ['.png','.jpg','.jpeg','.png']
    },
    {
       "directory": "Database",
       "ext": ['.sql']
    },
    {
      "directory": "TS",
      "ext": ['.ts']
    },
    {
     "directory":"Videos",
     "ext": ['.mkv']
    }

]

for filename in os.listdir(appsPath):
    if os.path.isfile(os.path.join(appsPath,filename)):
        for rule in Rules:
            if Path(filename).suffix.lower() in rule['ext']:
                if not os.path.exists(os.path.join(todayappsPath,rule['directory'])):
                    os.makedirs(os.path.join(todayappsPath,rule['directory']))
                    os.rename(os.path.join(appsPath,filename),os.path.join(todayappsPath,rule['directory']+'/',filename))
                else:
                    os.rename(os.path.join(appsPath,filename),os.path.join(todayappsPath,rule['directory']+'/',filename))
