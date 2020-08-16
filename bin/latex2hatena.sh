#! /usr/bin/sh
# -o, --bibliography=, --csl=, -M enable-upload=true/false
execdir="`dirname $0`"
settingsdir="${execdir}/../settings"
filterdir="${execdir}/../filter"
pandoc --mathjax --wrap=auto -F pandoc-crossref  -F pandoc-citeproc -F ${filterdir}/hateblo-filter.py -f latex -M reference-section-title='参考文献' -M crossrefYaml=${settingsdir}/pandoc-crossref-settings.yaml $@