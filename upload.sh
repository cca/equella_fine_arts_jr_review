#!/usr/bin/env bash
# sort the taxonomy, just helps when reading through it in admin console
sort taxo.csv > tmp; mv tmp taxo.csv
# upload it
uptaxo --un $(jq -r .username ~/.equellarc) --pw $(jq -r .password ~/.equellarc) --csv taxo.csv --tid $(eq tax --name 'Fine Arts Junior Review students' | jq -r .uuid) --clear
