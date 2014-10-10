i=1

print type(i)

f=1.0

print type(f)

l=234123412341234123412341234234234234241234123412341234123412341324123412342134;

print type(l)

c=10+10j
cl=3+4j
print type(c)
print c+cl

s="SKKU"

print type(s)

if s == "SKKU":
	print "Equal"

if s is "SKKU":
	print "Equal"

s2 = "University"

print s+" "+s2

if "S" in s:
	print "right"

print s[0]
print s[1:]
print s[:2]

print s[-1]

date = "2014-09-19"

print date.split("-")
print date.find("1")


a = date.find("1")

print a + date[a+1:].find("1") + 1

input = int(raw_input())
for i in range(input,10):
	for j in range(1,10):
		print i,"*",j,"=",i*j