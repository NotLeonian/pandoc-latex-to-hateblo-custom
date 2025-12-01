#! /bin/bash
# -o, --bibliography=, --csl=, -M enable-upload=true/false
execdir="`dirname $0`"
filterdir="${execdir}/../filter"

function usage {
cat <<EOF
  convert LaTeX source to HTML with syntax provided by hatenablog.com

  Usage:
    $(basename ${0}) [options] INPUT.tex

  Options:
    -o FILE                   output file path. if not specified, to Stdout
    --bibliography=FILE PATH  bib.file path
    -M ...                    pandoc meta file arguments
EOF
}

if [ $# -eq 0 ]; then
  usage
  exit 1
fi

pandoc \
  -f latex \
  -t html5 \
  --mathjax \
  --wrap=auto \
  -F pandoc-crossref \
  --citeproc \
  -F ${filterdir}/hateblo-filter.py \
  -M reference-section-title='参考文献' \
  -M figureTitle='図' \
  -M figPrefix='図' \
  -M tableTitle='表' \
  -M tblPrefix='表' \
  -M link-citations \
  -M linkReferences \
  $@
