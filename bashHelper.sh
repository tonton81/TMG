if [ ! -z "$1" ]
  then
    if [ $1 == "READCPKEY" ] # read params keys for QT
      then
        cd /data/params/d/
        array=(`cat $2 | sed 's/,/\n/g' | sed 's/[][]//g'`) && echo ${array[@]}
    fi
    if [ $1 == "GETKEYS" ] # params keys for QT combobox
      then
        echo "$(</data/TMG/keylist)" | tr -d \"
    fi
fi
