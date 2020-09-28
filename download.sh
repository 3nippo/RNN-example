#!/bin/bash
mkdir src_repos
cd src_repos

input="../links"

while IFS= read -r line
do
    git clone $line
done < "$input"

cd ..

find ./src_repos/ \( -name '*.cpp' -or -name '*.c' \) -exec file '{}' -i >> src_encs \;

python ./merge_src_files.py
# && sudo rm -r src_repos src_encs
