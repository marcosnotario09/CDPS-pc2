#!/usr/bin/python


from subprocess import call

#funciones
def cmd(cmd):
	call(cmd,shell=True);

def cmd_app(maquina,aux):
	call("sudo lxc-attach --clear-env -n "+maquina+" -- "+aux, shell=True);

def cmd_bash(maquina,aux):
	call("sudo lxc-attach --clear-env -n "+maquina+" -- bash -c \" " +aux+"\"", shell=True);

def cp(src,maquina,dst):
	cmd("sudo cp "+src+" /var/lib/lxc/"+maquina+"/rootfs"+dst);
#------------------------------------------

#Instalacion de la applicacion quiz en cada servidor

#clonacion del repositorio
cmd_app("s1","git clone https://github.com/CORE-UPM/quiz_2021.git");
cmd_app("s1","sed -i '29d' quiz_2021/app.js");
print("\033[1;32m"+"REPOSITORIO CLONADO EN S1"+"\033[m");

cmd_app("s2","git clone https://github.com/CORE-UPM/quiz_2021.git");
cmd_app("s2","sed -i '29d' quiz_2021/app.js");
print("\033[1;32m"+"REPOSITORIO CLONADO EN S2"+"\033[m");
cmd_app("s3","git clone https://github.com/CORE-UPM/quiz_2021.git");
cmd_app("s3","sed -i '29d' quiz_2021/app.js");
print("\033[1;32m"+"REPOSITORIO CLONADO EN S3"+"\033[m");

#cmd_app("s4","git clone https://github.com/CORE-UPM/quiz_2021.git");
#cmd_app("s4","sed -i '29d' quiz_2021/app.js");
#print("\033[1;32m"+"REPOSITORIO CLONADO EN S4"+"\033[m");

#instalacion del repositorio
#s1
cmd_bash("s1","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; npm run-script migrate_env; npm run-script seed_env; ./node_modules/forever/bin/forever start ./bin/www");
print("\033[1;32m"+"APP INSTALADA EN S1"+"\033[m");

#s2
cmd_bash("s2","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www");
print("\033[1;32m"+"APP INSTALADA EN S2"+"\033[m");

#s3
cmd_bash("s3","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www");
print("\033[1;32m"+"APP INSTALADA EN S3"+"\033[m");

#s4
cmd_bash("s4","cd /quiz_2021; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export #DATABASE_URL=mysql://quiz:xxxx@20.20.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www");
print("\033[1;32m"+"APP INSTALADA EN S4"+"\033[m");

#enlace simbolico al punto de montaje del nas
cmd_bash("s1","cd /quiz_2021/public; rm -rfv uploads");
cmd_app("s1","ln -s /mnt/uploads /quiz_2021/public");
cmd_bash("s2","cd /quiz_2021/public; rm -rfv uploads"); 
cmd_app("s2","ln -s /mnt/uploads /quiz_2021/public");
cmd_bash("s3","cd /quiz_2021/public; rm -rfv uploads");
cmd_app("s3","ln -s /mnt/uploads /quiz_2021/public");
cmd_bash("s4","cd /quiz_2021/public; rm -rfv uploads");
cmd_app("s4","ln -s /mnt/nas /quiz_2021/public/uploads");
print("\033[1;32m"+"ENLACES SIMBOLICOS AL NAS CONFIGURADOS"+"\033[m");
#------------------------------------------

print("\033[1;32m"+"APLICACION QUIZ INSTALADA Y CONFIGURADA"+"\033[m");
