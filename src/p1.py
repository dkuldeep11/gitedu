print "hello to Py..."

def f1(flag):
  print "in f1() ..."
  if flag:
    k1()
    print "in if..."
  else:
    k2()
    print "in else"

  print "ending f1..."


def k1():
  print "k1 is called in if..."

def k2():
  print "k2 else called"


f = True
f1(f)

