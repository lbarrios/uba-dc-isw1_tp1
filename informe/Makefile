TEX = pdflatex -shell-escape -interaction=batchmode -file-line-error

informe.pdf: informe.tex
	@( $(TEX) informe.tex && clear && $(TEX) informe.tex ) || ( rm -f informe.pdf && echo -e "\n\n\e[1;31m¡La compilación falló amigo!\e[0m">&2 )

clean:
	rm -f *.aux *.log *.out *.fdb_latexmk *.fls *.ilg *.ind *.idx *.toc *.synctex.gz

