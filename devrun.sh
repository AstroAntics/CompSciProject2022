########################################################################################
############################### Development Deploy Script ##############################
############ Opens a new instance of the app using the `flask run` command #############
### DO NOT RUN THIS IN PRODUCTION, it's wildly insecure (not in the emotional way :p) ##
###################### and doesn't always do what you want it to do. ###################
########################################################################################

RED="\e[31m";
GREEN="\e[32m";
END_COLOR="\e[0m";

echo "Booting website now...";
echo -e "${RED}DO NOT RUN THIS SCRIPT IN PRODUCTION! ${END_COLOR}";
flask run;