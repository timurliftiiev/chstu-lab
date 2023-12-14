#!/bin/bash
if [[ $1 =~ ^(.*) ]]; then
    DIRECTORY="${BASH_REMATCH[1]}"
fi

if [ ! -d "$DIRECTORY" ]; then
    echo "The directory $DIRECTORY does not exist."
    exit 2
fi
FILE_COUNT=$(find "$DIRECTORY" -type f | wc -l)
echo "Number of files in $DIRECTORY: $FILE_COUNT"
