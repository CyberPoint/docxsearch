PROJECT_NAME = docxsearch
SOURCE_FOLDER = docxsearch
OUTPUT_BINARY = docxsearch
PYINSTALLER = pyinstaller
TOOL_VERSION := 0.0.1
COMPRESS = zip
ifeq ($(OS),Windows_NT)
RM := rd /q /s
PYTHON := python
PIP := pip
else
UNAME_S := $(shell uname -s)
RM := /bin/rm -rf 	
PYTHON := python3
PIP := pip3
endif

.PHONY: virtual install build-requirements black isort flake8

all: package
	@pandoc README.md --listings -H listings-setup.tex -V geometry:"left=1cm, top=1cm, right=1cm, bottom=2cm" -V fontsize=12pt -s -o dist/$(OUTPUT_BINARY)_README_$(CATO_VERSION).pdf

develop:
	sudo apt-get -y install python3.8 python3-pip pandoc texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra upx
	$(PIP) install --user --upgrade setuptools wheel
	$(PIP) install -Ur requirements.txt

package:
ifeq ($(OS),Windows_NT)
	@$(PYTHON) setup.py bdist_wheel
	@$(PYINSTALLER) -y -F --path="$(SOURCE_FOLDER)/" --noupx scripts/$(OUTPUT_BINARY)
else
	@$(PYTHON) setup.py sdist bdist_wheel
endif

binary:
	@$(PYINSTALLER) -y -F --path="catocli/" --noupx scripts/catocli
	@cd dist && $(COMPRESS) $(OUTPUT_BINARY)-$(CATO_VERSION).zip $(OUTPUT_BINARY) $(OUTPUT_BINARY)_README_$(CATO_VERSION).pdf

clean:
ifeq ($(OS),Windows_NT)
	$(RM) dist catocli.build build cato_cli.egg-info 2>nul
else
	$(RM) $(USER)/.cato/* 2> /dev/null
	@$(RM) dist catocli.build build cato_cli.egg-info 2> /dev/null
endif
	@sudo $(PIP) uninstall --yes $(PROJECT_NAME) 2> /dev/null