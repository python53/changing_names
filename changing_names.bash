
#!/bin/bash

older.txt

file=$(grep "name"../data/list.txt cut -d' ' -f3)

for x in $file; do
  if [-e $HOMES$x]; then
      echo $HOMES$x >>older.txt;
  fi

done


