# Births .sh how many births in a state
#usage births.sh [sate abbreviation]
cut -f7 $1.tsv | tail -n+2 | python add.py