all: generator consumer dispatcher

generator: generator.o
	g++ -Wall -g -o generator generator.o

consumer: consumer.o
	g++ -Wall -g -o consumer consumer.o

dispatcher: dispatcher.o
	g++ -Wall -g -o dispatcher dispatcher.o
    
generator.o: generator.cpp
	g++ -Wall -g -c generator.cpp

consumer.o: consumer.cpp
	g++ -Wall -g -c consumer.cpp

dispatcher.o: dispatcher.cpp
	g++ -Wall -g -c dispatcher.cpp

clean:
	rm -f *.o *~ generator consumer dispatcher
