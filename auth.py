import ctypes
import hashlib
import ctypes
import base64

d_encrypt_dll = ctypes.windll.LoadLibrary( 'libs/login.dll' )
KEY = "47 44 50 64 46 53 61 6D 74 61 6B 53 67 78 52 64"

def hex_format_space(data):
    return ' '.join(data[i:i + 2] for i in range(0, len(data), 2))

def get_req_data(username,password, cmd1=2, cmd2=6):
    jd_uuid = '867323020350896-a086c68dae09'
    account = '00%s%s0020%s' % (hex(len(username)).replace('0x', ''), username.encode('hex'), str(
        hashlib.md5(password).hexdigest().encode('hex')))
    account = '000200' + hex(len(account) / 2).replace('0x', '') + account
    device_finger_print = '00040034' + (
    '000a0001000402020020' + hashlib.md5('a086c68dae09###ss').hexdigest().upper()).encode('hex')
    device = '0008005d000200640007616e64726f69640005342e342e320005352e312e300008313238302a37323000056a64617070000' \
             '4776966690000001c%s000000010005312e342e320048001100036e6f7800034d693400034d49340000' % (
             jd_uuid.encode('hex'))
    header = '0YXX0000000000000001000000010000000100000000000%d000%d0064011100' % (cmd1, cmd2)

    data = (header + account + device_finger_print + device).upper()
    length = hex(len(data) / 2).replace('0x', '')

    if length <= 256:
        data = data.replace('Y', '0').replace('XX', length)
    else:
        data = data.replace('Y', length[0]).replace('XX', length[1:3])

    encrypt_addr = d_encrypt_dll.Teaencryption(KEY, data)
    encrypt_p = ctypes.c_char_p(encrypt_addr)

    req_data = KEY + ' ' + encrypt_p.value
    req_data_array = map(lambda x: int(x, 16), req_data.split(' '))
    return base64.b64encode(bytearray(req_data_array))


def to_hex_str(s):
    byte = str(hex(ord(s))).replace('0x', '')
    if len(byte) == 1:
        byte = '0' + byte
    return byte


def get_resp_data(resp_data):
    resp_data_array = map(to_hex_str, base64.b64decode(resp_data))
    resp_data_hex = ' '.join(resp_data_array)
    decrypt_addr = d_encrypt_dll.TeaDecrypt(KEY, resp_data_hex)
    decrypt_p = ctypes.c_char_p(decrypt_addr)

    return decrypt_p.value.replace(' ', '')

def get_cookie(resp_data):
    pin_index = resp_data.find('C00010') + 10
    if pin_index == 1:
        print 'NOT FOUND'
    pin_hex = resp_data[pin_index:]
    pin = ''.join(map(lambda x: chr(int(x, 16)), hex_format_space(pin_hex).split(' ')))

    whwswswws = ''
    wssl_start = resp_data.find('1100003700')
    if wssl_start == -1:
        print 'whwswswws start index not found'
    else:
        wssl_stop = resp_data.find('000A0048')
        if wssl_stop == -1:
            wssl_stop = resp_data.find('000A0058')
            print 'whwswswws stop index not found'
        else:
            whwswswws = resp_data[wssl_start + 10:wssl_stop]

    whwswswws = ''.join(map(lambda x: chr(int(x, 16)), hex_format_space(whwswswws).split(' ')))

    wskey_hex = ''
    wskey_start = resp_data.find('000A0048')
    wskey_stop = resp_data.find('000E')
    if wskey_start == -1:
        wskey = resp_data.find('000A0058')
    if wskey_start == -1:
        wskey_start = resp_data.find('4163636')
        wskey_hex = resp_data[wskey_start:]
    if wskey_start == -1:
        wskey_start = resp_data.find('080019')
        wskey_hex = resp_data[wskey_start + 6:]

    wskey_hex = resp_data[wskey_start + 8:wskey_stop]
    wskey_array = map(lambda x: int(x, 16), hex_format_space(wskey_hex).split(' '))
    wskey = base64.b64encode(bytearray(wskey_array)).replace('+', '-').replace('==', '').replace('/', '_')
    return 'pin=%s; wskey=%s; whwswswws=%s' % (pin, wskey, whwswswws)

if __name__=="__main__":
    req_data = get_req_data('jd_60aaf2f598861', 'e4e333')
    print  req_data

    resp = 'aHLnhbKM9oBtKHz0nVBtCtRI5vdKL0kEJSj85AR8sXiImjeOMj8xF+UhTWTXBgO4XV2QitZNleNzLP34rB0uAFK09+lzAsyuAhgCwXGz5YwkQ4hpnbx8vqwX1ZGaRkE590kX4nsrDFtOFqNklC1FStEKZBNQNrTd1J1hlDqudi7sxmZgh48TLno39B+dPuhP7PpKIkO9JAdoHP9KuVyoWA=='
    resp_data = get_resp_data(resp)
    cookie = get_cookie(resp_data)
    print  cookie

