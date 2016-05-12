#!/usr/bin/env python
#encoding: utf-8
 
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
import hashlib
import json
#import pyDes
class prpcrypt():
    def __init__(self):
        self.key = base64.decodestring('VlEc5qsEDXWChrWJ0AzMXQ==')  
         
        self.mode = AES.MODE_CBC
        self.ak='df0b'
        self.sk='VlEc5qsEDXWChrWJ0AzMXQ=='
        self.iv='1111111111111111'
        self.uuid='e30b7d4982d68096eb2c543063ee1212ece165e0'
        self.iv_de=''

    def jiami_j2j(self,text):
        j1=json.dumps(text)
        dj=self.padAK(self.encrypt(j1))
        values2={'_':dj} 
        jdata2=json.dumps(values2)
        return jdata2

    def jiemi_j2j(self,text):
        j1=json.loads(text)
        s1=j1['data'][0]['_']
        s2=self.decrypt(self.unak(s1))
        return s2
    
    #aes加密
    def encrypt(self,text):
        
        cryptor = AES.new(self.key,self.mode,self.iv)
        length = 16
        count = len(text)    
        pad = text + (length - len(text) % length) * chr(length - len(text) % length)
        self.ciphertext = cryptor.encrypt(pad)        
        return b2a_hex(self.ciphertext)

    #aes解密 
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,self.iv_de)
        plain_text  = cryptor.decrypt(a2b_hex(text))
        unpad = plain_text[0:-ord(plain_text[-1])]
        return unpad

    
    #插入ak
    def padAK(self,text):
        ak1=self.ak+text[0:13]+b2a_hex(self.iv)+text[13:len(text)]
        ak2=a2b_hex(ak1)        
        baseak=base64.encodestring(ak2)
        return baseak

    #解除ak   
    def unak(self,text):
        baseak=base64.decodestring(text)
        ak1=b2a_hex(baseak)
        ak2=ak1[4:17]+ak1[49:len(ak1)]
        self.iv_de=a2b_hex(ak1[17:49])
        return ak2

    #获取devid
    def get_devid(self):
        part1=self.md5(self.uuid+self.key)
        part2=self.md5(part1+self.key)
        return part1+part2

    #md5加密
    def md5(self,test1):       
        m= hashlib.md5()   
        m.update(test1)
        return m.hexdigest()




if __name__ == '__main__':
    # a='{"code":200,"data":[{"_":"3wtaZIhaliALJI7xk32hvn6nU8SxTyXujQNKf7YoGKqDaTJU0VN7Q1w\/QRVA59GY\/Z4ry4FHyUOmt+joMRylHk7nS4DbCCWJk6LLsxeBneyLaX46FSRifWZJPTQvucaIWSFl8uifkmS65zETU\/WGyLZI5OuATtu6AvgmUJ8ORpi4hcu454OrWlVOzL+bQnhETg02q54YPNYBNMqcmEi6ctH0iiT7M6K0ScMxCnF\/3B6RmcYmzxbrFRnFph5zzGSs+Ojrwq6tzSDcBL8gJW3LNLlan1sHJp9Eokz9DfDNpPEmZMhtiV9oQGHSL8dJEZc2Bz5ptx\/HBIPPq6pIHpJQtS6CwJ4bl2juXV1dniqbaslBskdqfsgig7CGMIW5gGOjYcpTDZhuVfVi3nFXGzhnqgtYC6HVLBQnBhYFaa2a49OYWzGKZxjXjacurCiUS+Gjm5WsbBRFRs3DllfZ19pUDi\/+5vWvuRKmekJMpkBgCytAeRE8zyY\/gFiDsl2WNkpbxgOWcD4005SaU9gfG5ucvByg0jjEs2RCzc6jAayXJcFd2NMOTag4btO3y0earWP5GjQUHubDD61w1cSkuzm3V4abfzKox2x1gcOKGhTvwNe6V2oQlT\/8GOd\/vWFKJdTd3uUO3rUD\/JUyiKsNkucd4W52Abf+mo7wFyUFkYV7TuWUfb5rrHsqq+ybzm4CZfTb5KLpgogse7dMZQadPrEb45Ub7gxYVktyFU8NDXZ1TpJsyw5HQiwKlyzyzT1Kxakvl7c="}],"message":"","request_id":"-","request_time":1450939538.2255,"response_time":1450939538.2313}'
    pc = prpcrypt() 
    
    
    #print str_baseen('a')
    
    # b='371fc2b2-561c70820dc627-11626503-b5107457'    
    # j1=pc.encrypt(b)
    # j2=pc.padAK(j1)
    # print j2
    #a='3ws0WzBo7xRVVykc+16NfrHNINjRj5ypsaiOVGYTUSajSsiG3F2eYu7+HCEJvCBUIpdoQKr/T7E5bQpuT73D/YOC0aRQIBpNMD34VfKiKnZIANN86nqVfJgJ1qtYTql7kUQsajVutUC3ih/GeWPDxGLSF6OWUoZCLHBtyRaaKZykH6G7rPjpMrl3KR+UpezcRdE7ADiUygotr9CZnfpOUeoRT/UQY/VZo1nMPaZNLNYk55ckxrT6MEzduZRSfdD0YlM8uLPZtuQzDcT9ooGAhKTWkiqXPUqL5UaiEnIaOH1e4LhNSF99EngcK35SVoeuyqVrSBxTyBYI5WiolHLTIIutVu20SFkkFJ06mPv/nRGzS1wKg2guO8JeM3hDNAKnPmBD+wmKcElHCaE/rMF5ioQ0d+hASjGhYJzsFOq7KqAWq7POUydeKbA/jIlKquT5ZF4ox3LGM6zlrJ3IjjcZvbigcuqGQ7gqaDBhj32b6Rr66D0fJIapYDd/DDO8DIuFYRVn2IFPjiD8ewKkVP916SGz'
    a = '3wvRKW9MyXf2nZrZWXtEYNeHaVQLpAvNDb2YhYRU4T1W2Ca9bfILJ90jqNpa3sWKMpq/2crsVXMcPSg+AGIGUXWeNcF0sxSWY4LoLjFDuHvWfjZwMhdFAcZNgoLYVeEvD8MeUd7EM156JCd9CwuLm4Q2BTmn+74KaHDrXYOz2y2NEQ\u003d\u003d'
    a=unicode(a,'unicode-escape')
    s2=pc.decrypt(pc.unak(a))
    print s2
    print pc.get_devid()

