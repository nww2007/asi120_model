TARGET := asi120_model

PYSRCS := main.py
PYSRCS += progress.py
PYSRCS += ser.py

VERB := @


all: main.py ctags
	$(VERB)python3 $< ASICAP_2019-05-05_01_46_42_235.SER


dist:
	$(VERB)python setup.py sdist


vim: ctags
# 	$(VERB)source /home/nww/projects/astronomy/asi120_model/bin/activate
	$(VERB)echo vim $(PYSRCS) Makefile
# 	deactivate


lint: $(PYSRCS)
	@echo ========== pylint ==========
	$(VERB)pylint3    $^ || true
	@echo =========== mypy ===========
	$(VERB)mypy       $^ || true
	@echo =========== pydocstyle ===========
	$(VERB)pydocstyle $^ || true


CTAGS = ctags
CTAGSFLAGS = -h ".py" --python-kinds=-i

ctags:
	$(VERB)$(CTAGS) $(CTAGSFLAGS) $(PYSRCS)


show:
	$(VERB)echo "TARGET:     " $(TARGET)
	$(VERB)echo "PYSRCS:     " $(PYSRCS)
	$(VERB)echo "VERB:       " $(VERB)
	$(VERB)echo "CTAGS:      " $(CTAGS)
	$(VERB)echo "CTAGSFLAGS: " $(CTAGSFLAGS)


.PHONY: dist


# $@ Имя цели обрабатываемого правила
# $< Имя первой зависимости обрабатываемого правила
# $^ Список всех зависимостей обрабатываемого правила
