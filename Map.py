import math
import matplotlib.pyplot as plt
#plt.use('tkagg')

if __name__ == "__main__":

  file = open("route.csv")
  data1 = file.read()
  file.close
  data1 = data1.split("\n")
  pos = [0,0]
  print(data1)
  print(pos)
  c_deg = 0
  f = open("write.csv","w")
  f.write("x,y\n")
  f.write(str(0)+","+str(0)+"\n")

  x=[]
  y=[]

  for d in data1:
    #print(d)
    if "s" in d:
      st = d.split(",")[1]
      pos[0] = pos[0] + float(st)*math.cos(math.pi*(c_deg/180))
      pos[1] = pos[1] + float(st)*math.sin(math.pi*(c_deg/180))
      x.append(pos[0])
      y.append(pos[1])
      print("##",pos)
      f.write(str(pos[0])+","+str(pos[1])+"\n")
    if "c" in d:
      print(d.split(","))
      c_deg = c_deg + int(d.split(",")[1])
    #print(c_deg)
  f.close

  """
  file = open("write.csv")
  data2 = file.read()
  file.close
  
  data2 = data2[4:]
  print(data2)
  data2 = data2.split("\n")
  for d2 in data2:
    st2 = d2.split(",")
    print(st2[0][:-5])
    x.append(float(st2[0]))
    y.append(float(st2[1]))
  """
  print(x)
  print(y)
  plt.plot(x,y,'o')
  plt.show()
