#!/usr/bin/python


from subprocess import call

#funciones
def cmd(cmd):
	call(cmd,shell=True);

def cmd_fw(aux):
	call("sudo lxc-attach --clear-env -n fw -- "+aux, shell=True);

def cp(src,maquina,dst):
	cmd("sudo /lab/cdps/bin/cp2lxc "+src+" /var/lib/lxc/"+maquina+"/rootfs"+dst);

#------------------------------------------
#cambiar la configuracion usando el archivo fw.fw
cp("fw.fw","fw","/root");
cmd_fw("chmod +x /root/fw.fw");
cmd_fw("/root/fw.fw");
cmd_fw("rm -f /root/fw.fw")
#------------------------------------------

print("\033[1;32m"+"FIREWALL CONFIGURADO"+"\033[m");
