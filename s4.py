#!/usr/bin/python

from subprocess import call

def cmd(cmd):
	call(cmd,shell=True);

#escribimos el xml de s4 en pc2.xml
#creamos copia a leer
cmd("cp pc2/pc2.xml copia.xml")
x=False;
fin=open("copia.xml","r");
fout=open("pc2/pc2.xml","w");
for line in fin:
	if "name=\"s3\"" in line:
		x=True;
		fout.write(line);
	elif x and "</vm>" in line:
		fout.write(line+"\n");
		fout.write("");
		#contenido de s4
		fout.write("  <vm name=\"s4\" type=\"lxc\" arch=\"x86_64\">"+"\n");
		fout.write("    <filesystem type=\"cow\">filesystems/rootfs_lxc64-cdps</filesystem>"+"\n");
		fout.write("    <if id=\"1\" net=\"LAN3\"><ipv4>20.20.3.14/24</ipv4></if>"+"\n");
		fout.write("    <if id=\"2\" net=\"LAN4\"><ipv4>20.20.4.14/24</ipv4></if>"+"\n");
		fout.write("    <if id=\"9\" net=\"virbr0\"><ipv4>dhcp</ipv4></if>"+"\n");
		fout.write("    <route type=\"ipv4\" gw=\"20.20.3.1\">20.20.0.0/16</route> "+"\n");
		fout.write("    <exec seq=\"on_boot\" type=\"verbatim\">"+"\n");
		fout.write("        mknod -m 666 /dev/fuse c 10 229;"+"\n");
		fout.write("    </exec>"+"\n");
		fout.write("    <filetree seq=\"on_boot\" root=\"/root/\">conf/hosts</filetree>"+"\n");
		fout.write("    <exec seq=\"on_boot\" type=\"verbatim\">"+"\n");
		fout.write("        cat /root/hosts >> /etc/hosts"+"\n");
		fout.write("        rm /root/hosts"+"\n");
		fout.write("        dhclient eth9"+"\n");
		fout.write("    </exec>"+"\n");
		fout.write("  </vm>"+"\n");
		#separacion
		fout.write("");
		
		x=False;
	else:
		fout.write(line);
fin.close();
fout.close();

cmd("rm -f copia.xml");

#aniadimos s4 a la conf/hosts
f=open("pc2/conf/hosts","a");
f.write("");
f.write("20.20.3.14   s4 s4-ext"+"\n");
f.write("20.20.4.14   s4-int"+"\n");
f.close();

print("\033[1;32m"+"S4 ANIADIDO AL ESCENARIO"+"\033[m");
