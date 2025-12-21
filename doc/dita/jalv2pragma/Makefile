# Title: Makefile to create the Compiler documentaion in pdf and html documentation using dita
# Author: Rob Jansen, Copyright (c) 2025..2025, all rights reserved.
# Adapted by:
# 
# This file is part of jallib (https://github.com/jallib/jallib)
# Released under the ZLIB license (http://www.opensource.org/licenses/zlib-license.html)
#

SOURCE_DIR=`pwd`

clean: 
	rm -rf $$HOME/tmp/pdf
	rm -rf $$HOME/tmp/html

doc:
	# Jallib documentation in pdf format
	$$DITA_HOME/bin/dita -project=${SOURCE_DIR}/pdf.xml -o $$HOME/tmp/pdf
	# Jallib documentation in html format
	$$DITA_HOME/bin/dita -project=${SOURCE_DIR}/html.xml -o $$HOME/tmp/html

all: clean doc

