#!/usr/bin/python


from subprocess import call
import time

#funciones
def cmd_g(maquina,aux):
	call("sudo lxc-attach --clear-env -n "+maquina+" -- "+aux, shell=True);

#------------------------------------------
#montaje de nas y configuracion en servidores web

#emparejamiento de servidores nas
cmd_g("nas1","gluster peer probe 20.20.4.22");
cmd_g("nas1","gluster peer probe 20.20.4.23");
print("\033[1;32m"+"SERVIDORES NAS ASOCIADOS"+"\033[m");

#hacemos tiempo para que se unan los nas
time.sleep(2);
#cmd_g("nas1","gluster peer status")

#creacion del volumen
cmd_g("nas1","gluster volume create uploads replica 3 20.20.4.21:/uploads 20.20.4.22:/uploads 20.20.4.23:/uploads force");
cmd_g("nas1","gluster volume start uploads");
print("\033[1;32m"+"VOLUMEN CREADO Y ARRANCADO"+"\033[m");

#recuperacion ante caidas
cmd_g("nas1","gluster volume set uploads network.ping-timeout 5");
cmd_g("nas2","gluster volume set uploads network.ping-timeout 5");
cmd_g("nas3","gluster volume set uploads network.ping-timeout 5");
print("\033[1;32m"+"RECUPERACION ANTE CAIDAS CONFIGURADA"+"\033[m");

#montamos los nas en los servidores web en /mnt/nas
cmd_g("s1","mkdir /mnt/uploads");
cmd_g("s2","mkdir /mnt/uploads");
cmd_g("s3","mkdir /mnt/uploads");
cmd_g("s4","mkdir /mnt/uploads");
cmd_g("s1","mount -t glusterfs 20.20.4.21:/uploads /mnt/uploads");
cmd_g("s2","mount -t glusterfs 20.20.4.22:/uploads /mnt/uploads");
cmd_g("s3","mount -t glusterfs 20.20.4.23:/uploads /mnt/uploads");


print("\033[1;32m"+"PUNTOS DE MONTAJE EN SERVIDORES WEB REALIZADOS"+"\033[m");
#------------------------------------------
print("\033[1;32m"+"SERVIDORES NAS CONFIGURADOS"+"\033[m");

