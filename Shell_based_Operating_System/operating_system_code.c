#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h> 

#define DEST_SIZE 40
#define INPUT_LINE_BUFSIZE 128
#define SPLIT_LINE_BUFSIZE 64
#define Token_Delim " \t\r\n\a"
#define PATH_SIZE 64
#define BUFSIZE 1000

char path[PATH_SIZE][PATH_SIZE]={"\0"};
int path_count;

///////////////////////////////////////////////////////////////////////////////

int builtin_func_cd(char **args);
int builtin_func_path(char **args);
int builtin_func_exit(char **args);

//int (*builtin_func[])(char **) = {&builtin_func_cd, &builtin_func_path, &builtin_func_exit};

///////////////////////////////////////////////////////////////////////////////

void error_generation()
{
	char error_message[30] = "An error has occurred\n"; 
	write(STDERR_FILENO, error_message, strlen(error_message));
        exit(EXIT_FAILURE);
}

///////////////////////////////////////////////////////////////////////////////

int builtin_func_cd(char **args)
{
  printf("inside cd 2 \n");
  char *result;
  int len_args = strlen(args[1]);
  printf("--lenargs---%d \n", len_args);
  result = malloc(sizeof(char) * len_args);
  strncpy(result, args[1], len_args);
 
  if (chdir(result) != 0) 
  {
      error_generation();
  }
  return 1;
}

////////////////////////////////////////////////////////////////////////////////////////

int builtin_func_exit(char **args)
{

  //for(int i=0; i<8; i++)
  //{
  //    printf("\n ---- data in it -----%d ----%s \n", i, args[i]);

  //}

  //if(args[0] == NULL || args[1] == NULL || args[2] == NULL || args[3] == NULL || args[4] == NULL || args[5] == NULL || args[6] == NULL || args[7] == NULL)
  //{
  //	return 0;
  //}
  //else
  //{
  //      return 0;
  //}

  return 0;
}

////////////////////////////////////////////////////////////////////////////////////////

int builtin_func_path(char **args)
{
        //strcpy(p1,args[1]);
	//printf("P1 : %s\n",p1);
        int ln = sizeof(args);
	int i=0;
        path_count = 0;

        if(ln>5)
        {
            for(i=0; i<ln; i++)
            {
                 if(args[i+1] == NULL)
                 {
                      break;
                 }
                 strcpy(path[i],args[i+1]);
                 path_count = path_count + 1;
		 printf("path : %s\n",path[i]);
            }
	    //path[i]=args[1];
        }

	return 1;
}

////////////////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////

int process_create(char **arg)
{

	int rc=fork();
	pid_t wpid;
	int status;
	
	
	int len_split_line = sizeof(arg);
	printf("len of last argumet %d\n",len_split_line);
	char chout[100];
	char chcmd[100]={""};
	char **ccmd = malloc(10*sizeof(char));

	int count=0;
	while(arg[count])
	{
		if(strcmp(arg[count],">")==0)
		{
			strcpy(chout,arg[count+1]);
			break;
		}
		else
		{
			ccmd[count]=arg[count];
			
		}
		
		count++;
	}

	printf(" CHOUT %s\n",chout);
	printf(" CCMD %s\n",ccmd[0]);
	
	
	if(rc==0)
	{
		
		//printf("---path_count--%d\n", path_count);
		//for (int k=0; k<path_count; k++)
		//{
		//    printf("--path--data----%d----%s\n", k, path[k]);
		//}
		//printf("GGEZ : %s \n",*arg);
		//printf("---path_data--%s\n", path[0]);

		char p1[10];
		strcpy(p1, path[0]);
		char val[2] = "\0";
		if(strcmp(p1, val)==0)
		{
			error_generation();
		}


		int len_split_line = sizeof(arg);
		//printf("\n --- splitline len ---- %d \n", len_split_line);
		int pos;
		int flag = 0;
		char file_name[30];


		//if(flag == 1)
		//{


		//fp = fopen ("/home/soumyadeep/Documents/semester_1/operating_systems/project/);
		//char *arr[] = arg;

		char *result;
		int len_args = strlen(arg[0]);
		result = malloc(sizeof(char) * len_args);
		strncpy(result, arg[0], len_args);

		//int len_dest = 5 + len_args;
		//char dest1[DEST_SIZE] = "/bin/";
		//char dest2[DEST_SIZE] = "/usr/bin/";
		//strcat(dest1, result);
		//strcat(dest2, result);
		//printf("---ans ---%s \n", dest);
		
		for (int i=0; i<path_count; i++)
		{
		char dest[DEST_SIZE] = {"NULL"};
				strcpy(dest, path[i]);
				strcat(dest, "/");
				strcat(dest, result);

		//int fd = open(file_name, O_WRONLY|O_TRUNC|O_CREAT, 0644);
		//if (fd < 0)
		//{ 
		//    error_generation();
		//}
		//if (dup2(fd, 1) < 0) 
		//{ 
		 //   error_generation();
		//}
		//close(fd);
	

				int temp = execv(dest, ccmd);
				if(temp == 1)
				{
					error_generation();
				}
		}

			//}


	}
	else if(rc < 0)
	{
		error_generation();
	}
	else
	{	
		do{
			wpid = waitpid(rc, &status, WUNTRACED);
		  }while(!WIFEXITED(status));		 
	}
	return 1;	
}

////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////
//PARALLEL PROCESS
int parallel_process(char **args)
{
	int x=0, y=3;
	
	for(int i=1;i<=3;i++)
	{
		if(i==2)
		{
			x=2;
			y=4;
		}
		else if(i==3)
		{
			x=6;
			y=7;
		}
		if(strcmp(args[x],"cd")==0)
		{
		  printf("inside cd 2 \n");
		  char *result;
		  int len_args = strlen(args[y]);
		  printf("--lenargs---%d \n", len_args);
		  result = malloc(sizeof(char) * len_args);
		  strncpy(result, args[y], len_args);
		 
		  if (chdir(result) != 0)
		  {
			  error_generation();

		  }
		  
		}
		
		else if(strcmp(args[x],"path")==0)
		{
			
			int i=0;
			path_count = 0;

			 strcpy(path[i],args[y]);
			 path_count = path_count + 1;
			printf("path : %s\n",path[i]);
			
		}
		
		else
		{
			int rc=fork();
			pid_t wpid;
			int status;
			if(rc==0)
			{
				printf("SUCCESS YEAAA");
				char p1[10];
                strcpy(p1, path[0]);
                char val[2] = "\0";
                if(strcmp(p1, val)==0)
                {
                     error_generation();
                }
				char *result;
		   int len_args = strlen(args[x]);
		   result = malloc(sizeof(char) * len_args);
		   strncpy(result, args[x], len_args);
		   for (int i=0; i<path_count; i++)
		   {
			   char dest[DEST_SIZE] = {"NULL"};
			   strcpy(dest, path[i]);
			   strcat(dest, "/");
			   strcat(dest, result);
			   int temp = execv(dest, args);
			   if(temp == 1)
			   {
				   error_generation();
			   }
		   }
				
			}
			else if(rc < 0)
			{
			error_generation();
			}
			else
			{
			do{
			wpid = waitpid(rc, &status, WUNTRACED);
			 }while(!WIFEXITED(status));
			}
		}
	}


return 1;
}


////////////////////////////////////////////////////////////////////////////////////////////

int func_distribute(char **args)
{
  //char *arr_all_builtins[] = {"cd","path","exit"};
  //int num_of_builtin_funcs = 3;
  char check_cd[2] = "cd";
  char check_path[4] = "path";
  char check_exit[4] = "exit";

  char *result;
  int len_args = strlen(args[0]);
  //printf("--lenargs---%d \n", len_args);
  result = malloc(sizeof(char) * len_args);
  strncpy(result, args[0], len_args);
  //int len_res = strlen(result);
  //printf("--lenres---%d \n", len_res);
  
  if (result == NULL) 
  {
      return 1;   // An empty command was entered
  }

  else if (strcmp(result,"cd") == 0) 
  {
      printf("inside cd \n");
      return (builtin_func_cd(args));
  }
  
  else if (strcmp(result,"path") == 0) 
  {
      printf("inside path \n");
      return builtin_func_path(args);
  }

  else if (strcmp(result,"exit") == 0) 
  {
      printf("inside exit \n");
      return builtin_func_exit(args);
  }

  else
  {
      return (process_create(args)); ///execution of non builtin functions
  }
    
}

////////////////////////////////////////////////////////////////////////////////////////

char **split_line(char *line_2)
{

  int bufsize_2 = SPLIT_LINE_BUFSIZE;
  int token_pos = 0;
  char **tokens = malloc(bufsize_2 * sizeof(char*));
  char *token, **tokens_backup;


  if(!tokens)
  {	
	error_generation();
	exit(EXIT_FAILURE);
  }

  token = strtok(line_2, Token_Delim);
  //printf("\n --- token ---- %s \n", token);
  while (token != NULL)
  {
	tokens[token_pos] = token;
        token_pos++;

        if(token_pos >= bufsize_2) 
        {
        	bufsize_2 = bufsize_2 + SPLIT_LINE_BUFSIZE;
                tokens_backup = tokens;
                tokens = realloc(tokens, bufsize_2 * sizeof(char*));
      
                if(!tokens) 
                {
			free(tokens_backup);
                        error_generation();
                        exit(EXIT_FAILURE);
                }
         }
         token = strtok(NULL, Token_Delim);
  }
  tokens[token_pos] = NULL;
  return tokens;
}


///////////////////////////////////////////////////////////////////////////////

void bash_loop(void)
{
  char *buffer;
  size_t bufsize_1 = INPUT_LINE_BUFSIZE;
  size_t line_1;
  char **final_args;
  int loop_status = 1;
  int extra_status = 1;

  buffer = (char *)malloc(bufsize_1 * sizeof(char));

  printf("Inside bash loop \n");

  while(extra_status != 0)
  {
	if(buffer == NULL)
	{
	error_generation();
		exit(EXIT_FAILURE);
	loop_status = 0;
	}
	else
	{
			printf("\n");
	printf("dash> ");
	line_1 = getline(&buffer, &bufsize_1, stdin);
	printf("\n");
	printf("value in characters----%zu", line_1);
	printf("\n");
	printf("value in typed command ----%s", buffer);
	printf("\n");


	final_args = split_line(buffer); 
	if(final_args[1]&&(strcmp(final_args[1],"&")==0)&&(final_args[7])&&(strcmp(final_args[5],"&")==0))
	{
		extra_status = parallel_process(final_args);
		printf("Parallel worked");
	}
	else
	{
		extra_status = func_distribute(final_args);
	}

			free(buffer);
			free(final_args);
	}
  }
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char **argv)
{
  //char *file_data;

  if(argv[1] == NULL)
  {
      bash_loop();
  }
  else
  {
	  FILE *fp = fopen(argv[1], "r"); 
	  char buff[BUFSIZE];
	  char *buffer_new;
	  size_t bufsize_1_new = INPUT_LINE_BUFSIZE;
	  char **final_args_new;
          int extra_status = 1;

	  if(buffer_new == NULL)
	  {
	  	error_generation();
	        exit(EXIT_FAILURE);
	  } 

	  while(fgets(buff, BUFSIZE - 1, fp) != NULL) 
	  {
	     //printf ("%s\n", buff);
             buffer_new = buff;

             final_args_new = split_line(buffer_new);
             extra_status = func_distribute(final_args_new);

             //free(buffer_new);
             //free(final_args_new);
             
	  }
	  fclose(fp);
          free(buffer_new);
          free(final_args_new);
          //bash_loop();
  }
  return EXIT_SUCCESS;
}
