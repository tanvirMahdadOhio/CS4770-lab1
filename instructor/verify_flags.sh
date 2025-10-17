#!/usr/bin/env bash
# Usage: ./verify_flags.sh flag1 flag2 flag3
# Compares sha256 of provided flags to expected list with flag_hashes
HASHFILE="instructor_flags_hashes.txt"
if [ ! -f "$HASHFILE" ]; then
  echo "Missing $HASHFILE (instructor-only). Create file with expected hashes."
  exit 2
fi
i=1
for flag in "$@"; do
  expected=$(sed -n "${i}p" "$HASHFILE" | tr -d '\n')
  provided=$(echo -n "$flag" | sha256sum | awk '{print $1}')
  if [ "$provided" = "$expected" ]; then
    echo "Flag $i OK"
  else
    echo "Flag $i WRONG"
    exit 1
  fi
  i=$((i+1))
done
echo "All flags OK"
