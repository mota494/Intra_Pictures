all:
	@if ! cc main.c ; then \
	    echo "Main.c Compilation failed"; \
	else \
		./a.out && python3 soup.py; \
	fi

clean:
	rm -rf ./a.out
