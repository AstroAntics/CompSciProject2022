# Production deployment script

RED="\e[31m";
GREEN="\e[32m";
END_COLOR="\e[0m";

echo "${GREEN}Running website now *** PRODUCTION MODE ***...${END_COLOR}";
echo "Powering up Gunicorn now.";
gunicorn -w 8 -b 127.0.0.1:8000 app:app