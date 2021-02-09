#!/usr/bin/python


from subprocess import call

#funciones
def cmd(cmd):
	call(cmd,shell=True);

def cmd_lb(aux):
	call("sudo lxc-attach --clear-env -n lb -- "+aux, shell=True);

def cmd_bash(maquina,aux):
	call("sudo lxc-attach --clear-env -n "+maquina+" -- bash -c \" " +aux+"\"", shell=True);

def cp(src,maquina,dst):
	cmd("sudo /lab/cdps/bin/cp2lxc "+src+" /var/lib/lxc/"+maquina+"/rootfs"+dst);
#------------------------------------------
#Configuracion del balanceador

#instalacionde haproxy
cmd_lb("apt-get update -y");
cmd_lb("apt-get upgrade -y");
cmd_lb("apt-get install haproxy -y");
print("\033[1;32m"+"HAPROXY INSTALADO"+"\033[m");

#configuracion
#paramos el servidor apache
cmd_lb("service apache2 stop");
#copiamos configuracion
cp("haproxy.cfg","lb","/etc/haproxy");

print("\033[1;32m"+"CONFIGURACION COPIADA EN LB"+"\033[m");
#------------------------------------------

#------------------------------------------
#modificar los htmls de cada sevevidor web
cmd_bash("s1","echo '<h2>Servido por el Server1<h2>' >> /quiz_2021/views/index.ejs");
cmd_bash("s2","echo '<h2>Servido por el Server2<h2>' >> /quiz_2021/views/index.ejs");
cmd_bash("s3","echo '<h2>Servido por el Server3<h2>' >> /quiz_2021/views/index.ejs");

print("\033[1;32m"+"INDEX DE LOS SERVIDORES MODIFICADOS"+"\033[m");
#------------------------------------------

#------------------------------------------
#restart de haproxy con la configuracion adecuada
cmd_lb("sudo service haproxy restart");
#------------------------------------------

print("\033[1;32m"+"BALANCEADOR DE CARGA CONFIGURADO"+"\033[m");
