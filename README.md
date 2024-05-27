# passwordalchemy  
(cryptographically insecure) toy password manage I wrote cos I was bored  
![image](https://github.com/witchdocsec/passwordalchemy/assets/107813117/05ee3c0c-80fa-4076-9311-0f79bdd1656c)
![image](https://github.com/witchdocsec/passwordalchemy/assets/107813117/8929a4d8-c8c1-4f8a-8614-795ea3c20298)

# useage  

## genkeys  
```
usage: passwordalchemy.py genkeys [-h] [-pk PRIVATEKEY] [-opk OLDPRIVATEKEY]

options:
  -h, --help            show this help message and exit
  -pk PRIVATEKEY, --privatekey PRIVATEKEY
  -opk OLDPRIVATEKEY, --oldprivatekey OLDPRIVATEKEY
```

## store
```
usage: passwordalchemy.py store [-h] -d DOMAIN -p PASSWORD

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
  -p PASSWORD, --password PASSWORD
```

## fetch
```
usage: passwordalchemy.py fetch [-h] -pk PRIVATEKEY -d DOMAIN

options:
  -h, --help            show this help message and exit
  -pk PRIVATEKEY, --privatekey PRIVATEKEY
                        path to private key pem file
  -d DOMAIN, --domain DOMAIN
```

## update
```
usage: passwordalchemy.py update [-h] -d DOMAIN -p PASSWORD

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
  -p PASSWORD, --password PASSWORD
```
