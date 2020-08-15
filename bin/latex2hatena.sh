#! /bin/sh
# -o, --bibliography=, --csl=
execdir="`dirname $0`"
settingsdir="${execdir}/../settings"
filterdir="${execdir}/../filter"
pandoc --mathjax --wrap=auto -F pandoc-crossref -F pandoc-citeproc -F ${filterdir}/hateblo-filter.py -M reference-section-title='参考文献' -f latex -M crossrefYaml=${settingsdir}/pandoc-crossref-settings.yaml -t html $@