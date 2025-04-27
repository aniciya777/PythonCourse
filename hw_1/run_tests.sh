#!/usr/bin/env sh

# Task 1
printf ">>> nl -b a samples/2.txt \n" > artifacts/nl.txt
nl -b a samples/2.txt >> artifacts/nl.txt

printf "\n>>> python3 nl.py samples/2.txt \n" >> artifacts/nl.txt
python3 nl.py samples/2.txt >> artifacts/nl.txt

printf "\n>>> printf \"a\\\\nb\\\\nc\" | nl -b a \n" >> artifacts/nl.txt
printf "a\nb\nc" | nl -b a >> artifacts/nl.txt

printf "\n>>> printf \"a\\\\nb\\\\nc\" | python3 nl.py \n" >> artifacts/nl.txt
printf "a\nb\nc" | python3 nl.py >> artifacts/nl.txt

# Task 2
printf ">>> tail samples/1.txt \n" > artifacts/tail.txt
tail samples/1.txt >> artifacts/tail.txt

printf "\n>>> python3 tail.py samples/1.txt \n" >> artifacts/tail.txt
python3 tail.py samples/1.txt >> artifacts/tail.txt

printf "\n>>> tail samples/1.txt samples/2.txt \n" >> artifacts/tail.txt
tail samples/1.txt samples/2.txt >> artifacts/tail.txt

printf "\n>>> python3 tail.py samples/1.txt samples/2.txt \n" >> artifacts/tail.txt
python3 tail.py samples/1.txt samples/2.txt >> artifacts/tail.txt

printf "\n>>> seq 1 20 | tail -n 17 \n" >> artifacts/tail.txt
seq 1 20 | tail -n 17 >> artifacts/tail.txt

printf "\n>>> seq 1 20 | python3 tail.py \n" >> artifacts/tail.txt
seq 1 20 | python3 tail.py >> artifacts/tail.txt

# Task 3
printf ">>> wc samples/2.txt \n" > artifacts/wc.txt
wc samples/2.txt >> artifacts/wc.txt

printf "\n>>> python3 wc.py samples/2.txt \n" >> artifacts/wc.txt
python3 wc.py samples/2.txt >> artifacts/wc.txt

printf "\n>>> wc samples/1.txt samples/2.txt samples/3.txt \n" >> artifacts/wc.txt
wc samples/1.txt samples/2.txt samples/3.txt >> artifacts/wc.txt

printf "\n>>> python3 wc.py samples/1.txt samples/2.txt samples/3.txt \n" >> artifacts/wc.txt
python3 wc.py samples/1.txt samples/2.txt samples/3.txt >> artifacts/wc.txt

printf "\n>>> printf \"1 2 3\\\\na bc def\" | wc \n" >> artifacts/wc.txt
printf "1 2 3\na bc def" | wc >> artifacts/wc.txt

printf "\n>>> printf \"1 2 3\\\\na bc def\" | python3 wc.py \n" >> artifacts/wc.txt
printf "1 2 3\na bc def" | python3 wc.py >> artifacts/wc.txt
