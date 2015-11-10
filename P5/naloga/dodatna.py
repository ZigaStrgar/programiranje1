import re
import urllib.request


def get_data(url):
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "text/html; charset=utf-8")
    req.add_header('Accept-Encoding', 'utf-8')
    resp = urllib.request.urlopen(req)
    respdata = resp.read().decode("windows-1250")
    return re.findall('<TR class=r0>(.*?)</TR>', str(respdata))


def file_name(url):
    name = url.split("/")
    name = name[-1]
    name = name.split(".")
    return name[0].lower() + ".txt"


def correct_data(row):
    row = row.replace("<TD>", "<td>")
    row = row.replace("</TD>", "</td>")
    row = row.replace("<td>", "")
    row = row.split("</td>")
    return row


def dodatna(url):
    data = get_data(url)  # Create and send request
    file = open(file_name(url), 'w+')  # Trying to create a new file or open one

    for row in data:
        row = correct_data(row)  # Correctly split and replace data in table
        count = 0
        line = []
        while count < len(row) - 2:
            line.append(row[count])
            count += 1
        string = "\t".join(line)
        file.write(string + "\n")
    file.close()


dodatna("http://timingljubljana.si/lm/42M.asp")  # Moški 42km
dodatna("http://timingljubljana.si/lm/42Z.asp")  # Ženske 42km
dodatna("http://timingljubljana.si/lm/21M.asp")  # Moški 21km
dodatna("http://timingljubljana.si/lm/21Z.asp")  # Ženske 21km
dodatna("http://timingljubljana.si/lm/10M.asp")  # Moški 10km
# dodatna("http://timingljubljana.si/lm/10Z.asp")  # Ženske 10km  #  Že imamo :)
dodatna("http://timingljubljana.si/lm/HM.asp")  # Handbike moški 21km
dodatna("http://timingljubljana.si/lm/HZ.asp")  # Handbike ženske 21km
dodatna("http://timingljubljana.si/lm/DPMC.asp")  # Državno prvenstvo moški 42km
dodatna("http://timingljubljana.si/lm/DPZC.asp")  # Državno prvenstvo ženske 42km
dodatna("http://timingljubljana.si/lm/RZ.asp")  # Rolerji moški
dodatna("http://timingljubljana.si/lm/RM.asp")  # Rolerji ženske
