#!/bin/bash

echo "Testing for forbidden characters (<>:\\|?*):"

flag=0

for file in $(find *); do
  echo -n "."
  name=$(basename "$file")
  if [[ ! "$name" =~ ^[^\<\>:\\|?*]+$ ]];
  then
    echo
    echo "[!] Failed: $file"
    flag=1
  fi
done
echo "done"
exit $flag
