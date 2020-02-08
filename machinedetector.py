import subprocess
p=subprocess.Popen("lsb_release -a",stdout=subprocess.PIPE,shell=True)
(o,e)=p.communicate()
ap = o.decode("utf-8")
print(ap)
