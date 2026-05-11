#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
from urllib import error

try:
    site= urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O Youtube não está acessível no momento.')
else:
    print('Consegui acessar o Youtube com sucesso!!')
