# the compiler: gcc for C program, define as g++ for C++
CC = gcc

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -g -Wall

# define any directories containing header files other than /usr/include
#
INCLUDES = -I/home/newhall/include  -I../include

# define library paths in addition 
# Sample: ./lib
#LFLAGS = -L./lib

# define any libraries to link into executable.
# must be in library paths
# Sample: -lmylib
#LIBS = -lmylib

# All files c
SRCFILES= $(wildcard *.c)

# .o same name as files
OBJFILES= $(patsubst %.c, %.o, $(SRCFILES))

# Each file a different executable
PROGFILES= $(patsubst %.c, %, $(SRCFILES))

# .PHONY == Special targets no associated with files
.PHONY: all clean

# all: Compile all programs
all: $(PROGFILES)

# clean: Clean all files generated!
clean:
	rm -f $(OBJFILES) $(PROGFILES) *~
