#!/bin/bash

if [[ ($1 == "-h") || ($1 == "--help") ]]
then
    echo "Usage:"
    echo "$0 [-h,-help] <-o,--out(format: 'ip:port')> 
    where:
        -h, --help  show this help text
	-o, --out set an output destination
    
    takes a loopback udp port (14550) as input, 
    distribute the input stream to output destinations."
    exit 0
fi
    
STREAM_OUT=""
COMMAND="mavproxy.py --out=udpin:127.0.0.1:14550 "
while [[ $# > 1 ]]
do
    key="$1"

    case $key in
	-o|--out)
	    STREAM_OUT+="--out=udp:$2 "
	    shift
	    ;;
		    *) # unknown option
	    ;;
    esac
    shift
done

COMMAND+="$STREAM_OUT"
echo "command:" $COMMAND "running: "
eval $COMMAND
