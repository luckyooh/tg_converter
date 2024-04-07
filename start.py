from TGConvertor import SessionManager
from pathlib import Path
import asyncio
import os


m = '''
1. tdata to pyrogram
2. pyrogram to tdata
3. tdata to telethon
4. telethon to tdata
5. telethon to pyrogram
6. pyrogram to telethon
7. pyrogram to strings
'''

def save_file(text):
    f = open("strings.txt", "wt")
    f.write(text)
    f.close()


while True:
    tdatas = os.listdir('tdatas')
    pyro = os.listdir('pyro')
    telethon = os.listdir('telethon')
    print(m)
    try:
        c = int(input())
    except:
        break
    if c == 1:
        x = 1
        for t in tdatas:
            name = t.split(".")[0]
            print(f'[{x}/{len(tdatas)}] Converting {name}' )
            session = SessionManager.from_tdata_folder(Path(f'tdatas/{name}/tdata'))
            asyncio.run(session.to_pyrogram_file(path=f'pyro/{name}.session'))
            x += 1
    if c == 2:
        x = 1
        for p in pyro:
            name = p.split(".")[0]
            print(f'[{x}/{len(pyro)}] Converting {name}' )
            session = asyncio.run(SessionManager.from_pyrogram_file(Path(f'pyro/{p}')))
            path = Path(f'tdatas/{name}')
            asyncio.run(session.to_tdata_folder(path=path))
            x += 1

    if c == 3:
        x = 1
        for t in tdatas:
            name = t.split(".")[0]
            print(f'[{x}/{len(tdatas)}] Converting {name}' )
            session = SessionManager.from_tdata_folder(Path(f'tdatas/{name}/tdata'))
            asyncio.run(session.to_telethon_file(path=f'telethon/{name}.session'))
            x += 1

    if c == 4:
        x = 1
        for th in telethon:
            name = th.split(".")[0]
            print(f'[{x}/{len(telethon)}] Converting {name}' )
            session = asyncio.run(SessionManager.from_telethon_file(Path(f'telethon/{th}')))
            path = Path(f'tdatas/{name}')
            asyncio.run(session.to_tdata_folder(path=path))
            x += 1
    if c == 5:
        x = 1
        for th in telethon:
            name = th.split(".")[0]
            print(f'[{x}/{len(telethon)}] Converting {name}' )
            session = asyncio.run(SessionManager.from_telethon_file(Path(f'telethon/{th}')))
            asyncio.run(session.to_pyrogram_file(path=f'pyro/{th}'))
            x += 1
    if c == 6:
        x = 1
        for p in pyro:
            name = p.split(".")[0]
            print(f'[{x}/{len(pyro)}] Converting {name}' )
            session = asyncio.run(SessionManager.from_pyrogram_file(Path(f'pyro/{p}')))
            asyncio.run(session.to_telethon_file(path=f'telethon/{p}'))
            x += 1
    if c == 7:
        x = 1
        t = input('1.Telethon Strings\n2.Pyrogram Strings\n')
        strings = ""
        for p in pyro:
            name = p.split(".")[0]
            print(f'[{x}/{len(pyro)}] Converting {name}' )
            session = asyncio.run(SessionManager.from_pyrogram_file(Path(f'pyro/{p}')))
            if t == '1':
                strings += session.to_pyrogram_string()+"\n"
            elif t == '2':
                strings += session.to_telethon_string()+"\n"
            x += 1
        save_file(strings)
        

    print('All is ready!')
