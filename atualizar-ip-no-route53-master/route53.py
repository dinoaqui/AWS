# Modificado de https://markcaudill.me/blog/2012/07/dynamic-route53-dns-updating-with-python/

from area53 import route53
from boto.route53.exception import DNSServerError
import requests
import sys
from datetime import datetime

##################################
# Atualizado em 18/08/2021
# Author: Hernani Soares
# Linkedin : www.linkedin.com/in/soaresnetoh
#
#  Preencha aqui seu Dominio / SubDominio / IP-v4 
#  
#  OBS: Se o campo New_IPv4 continuar 'meu_ip' 
#  será cadastrado no Route53 com o IPv4 da rede
#  que está sendo executado este script 
domain = sys.argv[1]
subdomain = sys.argv[2]
New_IPv4 = sys.argv[3]

def get_public_ip():
    r = requests.get('https://v4.ident.me')
    return r.text.rstrip()

fqdn = '%s.%s' % (subdomain, domain)
zone = route53.get_zone(domain)
arec = zone.get_a(fqdn)

if New_IPv4 == 'meu_ip':
    New_IPv4 = get_public_ip()

print('Atualizando no Route53')
print(domain)
print(subdomain)
print(New_IPv4)

if arec:
        Old_IPv4 = arec.resource_records[0]

        if Old_IPv4 == New_IPv4:
                print ('%s atualizado. (%s)' % (fqdn, New_IPv4))
                sys.exit(0)

        print ('Atualizando %s: %s -> %s' % (fqdn, Old_IPv4, New_IPv4))

        try:
                zone.update_a(fqdn, New_IPv4, 900)

        except DNSServerError:
                # Isso pode acontecer se o registro ainda não existir.
                # Vamos tentar adicionar um, caso seja o caso.
                zone.add_a(fqdn, New_IPv4, 900)
else:
        zone.add_a(fqdn, New_IPv4, 900)