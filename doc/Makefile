# Title: Makefile to create jal compiler pdf and html documentation using dita
# Author: Rob Jansen, Copyright (c) 2022..2022, all rights reserved.
# Adapted by:
# 
# This file is part of jallib (https://github.com/jallib/jallib)
# Released under the ZLIB license (http://www.opensource.org/licenses/zlib-license.html)
#
#

DITA_DIR=`pwd`/dita-ot-3.7.2
PDF_DIR=`pwd`/pdf
HTML_DIR=`pwd`/html
SOURCE_DIR=`pwd`/dita

clean: 
	rm -rf ${HTML_DIR}
	rm -rf ${PDF_DIR}

pdf:
	# Jalv2 documentation in pdf format
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2/pdf.xml -o ${PDF_DIR}
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2opt/pdf.xml -o ${PDF_DIR}
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2pragma/pdf.xml -o ${PDF_DIR}

html:
	# Jalv2 documentation in html format
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2/html.xml -o ${HTML_DIR}/jalv2
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2opt/html.xml -o ${HTML_DIR}/jalv2opt
	${DITA_DIR}/bin/dita -project=${SOURCE_DIR}/jalv2pragma/html.xml -o ${HTML_DIR}/jalv2pragma

all: clean pdf html

