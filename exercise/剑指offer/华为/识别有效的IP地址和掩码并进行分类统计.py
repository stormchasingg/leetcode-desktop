import sys

A = 0
B = 0
C = 0
D = 0
E = 0
error = 0
pri = 0
lookup = ['128', '192', '224', '240', '248', '252', '254','255', '0']
def checkMask(m):
    if len(m) != 4 or '' in m: return False
    if m[0] == '255' and m[1] == '255' and m[2] == '255' and m[3] == '255':
        return False
    if m[0] == '0' and m[1] == '0' and m[2] == '0' and m[3] == '0':
        return False
    if m[0] == '255' and m[1] == '255' and m[2] == '255' and m[3] in lookup:
        return True
    elif m[0] == '255' and m[1] == '255' and m[2] in lookup and m[3] == '0':
        return True
    elif m[0] == '255' and m[1] in lookup and m[2] == '0' and m[3] == '0':
        return True
    elif m[0] in lookup and m[1] == '0' and m[2] == '0' and m[3] == '0':
        return True
    else:
        return False

def checkIp(ip):
    if len(ip) != 4 or '' in ip: return False
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

while True:
    try:
        a = sys.stdin.readline().strip().split('~')
        ip, mask = a[0].split('.'), a[1].split('.')
        if checkMask(mask) and checkIp(ip):
                if 0 < int(ip[0]) < 127: A += 1
                elif 127 < int(ip[0]) < 192: B += 1
                elif 191 < int(ip[0]) < 224: C += 1
                elif 223 < int(ip[0]) < 240: D += 1
                elif 239 < int(ip[0]) < 256: E += 1
                if int(ip[0]) == 10: pri += 1
                if int(ip[0]) == 172 and 15 < int(ip[1]) < 32: pri += 1
                if int(ip[0]) == 192 and int(ip[1]) == 168: pri += 1
        else:
            error += 1
    except:
        break
print A, B, C, D, E, error, pri
