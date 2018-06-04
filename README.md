# Pomf.py
Pomf.se uploader made in Python3.5+.

This script makes it so you can upload to any pomf.se site, only requiring the url of the site. The script is also small enough to be taken wherever you need it to go, only taking up a single file. This script also needs `requests` but seeing as thats such a widely installed module, i dont think anyone DOESNT have it installed!

## Getting started
To get started with pomf.py first you must have Python 3.5 or higher as it makes use of asyncio. There is a non-async version you can download in the Github if you want to use it on anything below Python3.5. 

```py

import pomf
# select a host via get_host.
host = pomf.get_host('mixtape')

# you dont need anything other than a file
# to upload to the host
ret = host.upload(open('hearts.png', 'rb'))
# {'hash': 'f6bb5ef07fe63759ecfac1c81193c5912b96c45b', 'name': 'hearts.png', 'url': 'https://my.mixtape.moe/hsoali.png', 'size': 25553}

# if you want to add a host:
new_host = pomf.add_host('mixtape2', 'https://mixtape.moe')

```

### Asyncio Support
If you want to use pomf.py with asyncio, you can add a `_async` to the upload that will return a coroutine:
```py
await host.upload_async(open('hearts.png', 'rb'))
# {'hash': 'f6bb5ef07fe63759ecfac1c81193c5912b96c45b', 'name': 'hearts.png', 'url': 'https://my.mixtape.moe/hsoali.png', 'size': 25553}
```

### Pre-installed Hosts
Here are the hosts that are ready to be used with the script out of the box. 
```py
# mixtape - https://mixtape.moe
pomf.get_host('mixtape')
# safe - https://safe.moe
pomf.get_host('safe')
# void - https://void.cat
pomf.get_host('void')
```