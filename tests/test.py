# import ctypes
#
# dll = ctypes.windll.LoadLibrary('libs/sign5.3.0.dll')
# test  = dll.login
# test.restypes = ctypes.c_char_p
#
# cookie = test('18445755374','6a97an')
# a=ctypes.c_char_p(cookie)
# print a.value

# st=ctypes.create_string_buffer('0'*13)
# test  = dll.jd_sign
# test.rest

# sBuf = b'0'
# pStr = ctypes.c_char_p()
# pStr.value = sBuf
#
# test = dll.jd_sign
# # test.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
# sign = test('newUserInfo', 'dsfdsfdsfdsfdsfds', '{"flag":"nickname"}', pStr)
# print st.value
# print sign

# a='cheCi=G5&seatType=edz&seatPrice=55300&fromStationCode=VNP&fromStationName=%E5%8C%97%E4%BA%AC%E5%8D%97&toStationCode=AOH&toStationName=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&trainDate=1480435200000&passengerIds=1204607&contact=%E5%90%B4%E5%8B%87%E5%88%9A&phone=13978632546&realBook=1&account=&password='
# a_ = a.split('&')
# data = {}
# for t in a_:
#     _t = t.split('=')
#     data[_t[0]]=_t[1]
#
# print data

# import re
#
# file_object = open('order_submit_response')
# try:
#      all_the_text = file_object.read( )
#      onlinePayFee = re.findall(r'<input type="hidden" name="onlinePayFee" value="(.*)"/>', all_the_text)
#
#      print onlinePayFee
# finally:
#      file_object.close( )
a= '8.00000'
print float(a)

