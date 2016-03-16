#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <dirent.h>
#include <linux/input.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/select.h>
#include <sys/time.h>
#include <termios.h>
#include <signal.h>

void handler (int sig)
{
  printf ("Exiting... signal received: (%d)\n", sig);
  exit (0);
}

void perror_exit (char *error)
{
  perror (error);
  handler (9);
}

int main (int argc, char *argv[])
{
  struct input_event ev[64];
  int fd, rd, value, size = sizeof (struct input_event);
  char name[256] = "Unknown";
  char *device = NULL;

  //Setup check
  if (argv[1] == NULL)
  {
	printf("Bad usage, Specified the path to the dev event interface\n");
	printf("Sample /dev/input/event5\n");
	exit (0);
    }

  if ((getuid ()) != 0)
    printf ("You are not root!\n");

  if (argc > 1)
    device = argv[1];

  //Open Device
  if ((fd = open (device, O_RDONLY)) == -1)
    printf ("Device: %s is not a valid device.\n", device);

  //Print Device Name
  ioctl (fd, EVIOCGNAME (sizeof (name)), name);
  printf ("Reading From : %s (%s), forever...\n", device, name);

  while (1)
  {
      if ((rd = read (fd, ev, size * 64)) < size)
          perror_exit ("read()\n");      

      value = ev[0].value;

      if (value != ' ' && ev[1].value == 1 && ev[1].type == 1){ // Only read the key press event
	   printf ("  Code[%d] received. \n", (ev[1].code));
      }
  }

  return 0;
} 
