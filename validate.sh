
#!/bin/bash

echo "Testing for forbidden characters (<>:\\|?*):"

flag=0

for file in $(find *); do
  name=$(basename "$file")
  if [[ ! "$name" =~ ^[^\<\>:\\|?*]+$ ]];
  then
    echo "[!] Failed: $file"
    flag=1
  fi
done
exit $flag
