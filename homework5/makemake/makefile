all: exprtest
    
exprtest: exprtest.o driver.o parser.tab.o scanner.o
	g++ -Wall -g -o exprtest exprtest.o driver.o parser.tab.o scanner.o

exprtest.o: exprtest.cpp
	g++ -Wall -g -c exprtest.cpp

driver.o: driver.cpp driver.hpp scanner.hpp
	g++ -Wall -g -c driver.cpp

parser.tab.o: parser.tab.hpp parser.tab.cpp expression.hpp scanner.hpp driver.hpp
	g++ -Wall -g -c parser.tab.cpp

parser.tab.hpp: 
	bison parser.ypp
	
scanner.o: scanner.cpp
	g++ -Wall -g -c scanner.cpp

scanner.cpp: scanner.ll scanner.hpp
	flex -t scanner.ll > scanner.cpp

scanner.hpp: parser.tab.hpp

clean:
	rm -f *.o *.tab.* scanner.cpp *.hh exprtest
