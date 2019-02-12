#!/usr/bin/env python3

import base64

def a(o): #a(o):
	return xor(o, length('o'*92))

def b(o): #b(o):
	return xor(o, length('o'*222))

def c(o): #c(o):
	return xor(o, length('o'*26))

def d(o): #d(o):
	return xor(o, length('o'*183))

def e(o): #e(o):
	return xor(o, length('o'*245))

def f(o): #f(o):
	return xor(o, length('o'*254))

def g(o): #g(o):
	return xor(o, length('o'*161))

def h(o): #h(o):
	return xor(o, length('o'*196))

def i(o): #i(o):
	return xor(o, length('o'*38))

def j(o): #j(o):
	return xor(o, length('o'*200))

def k(o): #k(o):
	return xor(o, length('o'*194))

def l(o): #l(o):
	return xor(o, length('o'*170))

def m(o): #m(o):
	return xor(o, length('o'*43))

def n(o): #n(o):
	return xor(o, length('o'*104))

def q(o): #q(o):
	return xor(o, length('o'*103))

def r(o): #r(o):
	return xor(o, length('o'*253))

def s(o): #s(o):
	return xor(o, length('o'*152))

def t(o): #t(o):
	return xor(o, length('o'*183))

def u(o): #u(o):
	return xor(o, length('o'*215))

def v(o): #v(o):
	return xor(o, length('o'*221))

def w(o): #w(o):
	return xor(o, length('o'*97))

def x(o): #x(o):
	return xor(o, length('o'*60))

def y(o): #y(o):
	return xor(o, length('o'*197))

def z(o): #z(o):
	return xor(o, length('o'*145))

def aa(o): #aa(o):
	return xor(o, length('o'*74))

def xor(string, leng): #xor(o, oo):
    return [ charac(ordinal(curChar) ^ leng) for curChar in string ]

def ordinal(o): #ordinal(o):
    return ord(o)

def charac(o): #charac(o):
    return chr(o)

def encrypt(o): #encrypt(o):
    return ''.join(aa(z(y(x(w(v(u(t(s(r(q(n(m(l(k(j(i(h(g(f(e(d(c(b(a(o))))))))))))))))))))))))))

def length(o): #length(o):
    return len(o)

#eo = base64.b64encode(bytes(encrypt(open("flag.txt", "r").read().strip()), 'utf-8')).decode('utf-8')

#print("The flag has been protected: {}".format(eo))
#print("Can you recover it?")

#Do in reverse order!
encryptedVer = base64.b64decode("OTsxAxtMSkAbHRlJSR0ZSk0ZHUsZTR4eSksZHh1NGwU=")

def decode(o):
	return ''.join(a(b(c(d(e(f(g(h(i(j(k(l(m(n(q(r(s(t(u(v(w(x(y(z(aa(o))))))))))))))))))))))))))

print(decode(encryptedVer))
