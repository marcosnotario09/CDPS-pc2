#!/usr/bin/python


from subprocess import call
import time


#funciones
def cmd_bd(aux):
	call("sudo lxc-attach --clear-env -n bbdd -- "+aux, shell=True);

#------------------------------------------
#Creacion de la base de datos para los quizzes

#Instalacion de mariadb-server
cmd_bd("apt update");
cmd_bd("apt -y install mariadb-server");
print("\033[1;32m"+"MARIADB INSTALADA"+"\033[m");

#damos algo de tiempo para que acabe bien todo
time.sleep(2);

#Creacion de la tabla de datos quiz
cmd_bd("sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf");
cmd_bd("systemctl restart mysql");
cmd_bd("mysqladmin -u root password xxxx");
cmd_bd("mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"");
cmd_bd("mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"");
cmd_bd("mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to'quiz'@'localhost' IDENTIFIED by 'xxxx';\"");
cmd_bd("mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"");
cmd_bd("mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"");
print("\033[1;32m"+"TABLA QUIZ CREADA Y CONFIGURADA/"+"\033[m");
#------------------------------------------



print("\033[1;32m"+"BASE DE DATOS CONFIGURADA"+"\033[m");
