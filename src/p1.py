print "hello to Py..."

def f1(flag):
  if flag:
    k1()
  else:
    k2()
    print "in else"

  print "ending f1..."


def k1():
  print "in if..."

def k2():
  print "k2 else called"


f = True
f1(f)

