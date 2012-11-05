#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <iostream>
#include <sys/wait.h>
#include <sys/types.h>

int main() {
	pid_t gen, con;	// pid
	char *tmp[] = {}; // tmp for execute
	int pipefd[2];	// pipefd array
	int stat_val;	

	pipe2(pipefd, 0);

	// generator
	if(!(gen = fork())) {
		dup2(pipefd[1], 1);
		close(pipefd[1]);
		execve("./generator", tmp, tmp);
		_exit(0);
	}

	//execve("pstree -ap ppid", tmp, tmp);
	sleep(1);
	kill(gen, SIGTERM);
	waitpid(gen, &stat_val, WNOHANG);
	std::cerr << "Child exited with code " << WEXITSTATUS(stat_val) << std::endl;

	// consumer
	if (!(con = fork())) {
		dup2(pipefd[0], 0);
		close(pipefd[1]);
		execve("./consumer", tmp, tmp);
		_exit(0);
	}

	return 0;
}

