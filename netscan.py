import os
from pathlib import Path

appsPath = "/home/wd3bbas/Downloads/"

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
                if not os.path.exists(appsPath+rule['directory']):
                    os.makedirs(appsPath+rule['directory'])
                    os.rename(appsPath+filename,appsPath+rule['directory']+'/'+filename)
                else:
                    os.rename(appsPath+filename,appsPath+rule['directory']+'/'+filename)
            else:
                print("File without Rule")