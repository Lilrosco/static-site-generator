PUBLIC_DIRECTORY="./public"

# if [ -d "$PUBLIC_DIRECTORY" ]; then
#    echo "$PUBLIC_DIRECTORY already exists"
# else
#     mkdir $PUBLIC_DIRECTORY
# fi

python3 src/main.py /
cd public && python3 -m http.server 8888
