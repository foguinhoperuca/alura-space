#!/bin/bash

login() {
    URL="${BASE_ENDPOINT}/login"
    echo "Testing login!! URL=${URL}"
    curl -i -X POST -F "username=jonh_doe" -F "password=123" $URL
}

auth() {
    set +x

    if [ "$1" == "NO_AUTH" ];
    then
        AUTH_HEADER=""
    elif [ "$1" == "INVALID_AUTH" ];
    then
        AUTH_HEADER="Authorization: INVALID $API_AUTHORIZATION_TOKEN WRONG"
    elif [ "$1" == "IGNORE_AUTH" ];
    then
        AUTH_HEADER="Authorization: IGNORED $API_AUTHORIZATION_TOKEN"
    elif [ "$1" == "ERR_AUTH" ];
    then
        AUTH_HEADER="Authorization: Api-Key MY_CUSTOM_FAKE_TOKEN"
    else
        AUTH_HEADER="Authorization: Api-Key $API_AUTHORIZATION_TOKEN"
    fi
    URL="$BASE_ENDPOINT/emergency/protected_test_custom_auth/"
    echo "$URL -- $AUTH_HEADER"

    curl -i -X GET $URL -H "$AUTH_HEADER"
}

BASE_ENDPOINT="http://localhost:8080"
# case $2 in
#     "LOCAL") BASE_ENDPOINT="http://localhost:8080";;
#     "DEV") BASE_ENDPOINT="https://localhost:8080";;
#     "STAGE") BASE_ENDPOINT="https://localhost:8080";;
#     "PROD") BASE_ENDPOINT="https://localhost:8080";;
#     *) echo "USAGE: [LOCAL | DEV | STAGE | PROD]. $2 *NOT* found!!"
# esac

case $1 in
    "register") register $3;;
    "login") login $3;;
    *) echo "USAGE: [emergency | guideline | flood | auth | help] [LOCAL | DEV | STAGE | PROD]. $1 *NOT* found!!"
esac
