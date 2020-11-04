#include <stdio.h>
#include<semaphore.h> 
#include<stdio.h> 
#include<unistd.h> 
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define MAX_SLEEP_TIME 2	//Sleep time for student while programming

pthread_mutex_t lock;		//Mutex Lock
sem_t stdnt;				//Semaphore used by coordinator thread to wait on incoming students
sem_t cordintr;				//Semaphore used by teacher thread to wait on coordinator to wake it up
int total_chairs,occupiedseats;		//Total number of chairs given by user & seats occupied by students respectively
int total_number_of_helps;			//Total number of helps that a student can take from tutor (given by user)
int times_visited =0;				//Total number of times that all students tried to get help (including when there were no seats available) 
int total_teachers, available_teachers; //Total teachers given by user & available teachers at any threading moment 
sem_t *students_all;		//Semaphores created for each individual student thread
int students_in_q=0;		//Total students in queue (or sitting on chair)
int students_being_helped = 0;		//Number of students currently being helped
int total_students_tutored = 0;		//Total number of times students has been tutored
long *helped_by;				//Array pointer used to store value of the tutor who helped a student

/////////////-----Doubly linked list used to maintain the information of students coming to coordinator--------///////////////////////////////////

struct Node
{
	int help;		//Number of times a student has gotten helped
	int id;			//Student ID
	struct Node* next;	//Next node of list
	struct Node* prev;	//Previous node of list
};
struct Node* head = NULL; //Pointer pointing at the first element in the Node linked list

/////////////////-------Doubly linked list to maintain the students sitting in chair in priority------------/////////////////////////////////////

struct Node_stu
{
	int help;		//Number of times a student has gotten helped
	int id;			//Student ID
	struct Node_stu* next;		//Next node of list
	struct Node_stu* prev;		//Previous node of list
};
struct Node_stu *head_stu = NULL; //Pointer pointing at the first element in the Node_stu linked list

////////////////-----Student gets in a queue from where coordinator thread reads the student info when student comes-----///////////////////////

void push_to_coordinator(int id,int help)
{
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	struct Node* last = head;
	new_node->id = id;
	new_node->help = help;
	new_node->next = NULL;
	if (head == NULL) 
	{ 
		new_node->prev = NULL; 
		head = new_node;
	} 
	else
	{
		while (last->next != NULL)
		{					
			last = last->next;
		}

		last->next = new_node;
		new_node->prev = last;
	}
}
///////////////////---Coordinator uses this fucntion to put student in priority queue----//////////////////////////////////////////////////////

void push_to_chair()
{
	struct Node_stu* new_node = (struct Node_stu*)malloc(sizeof(struct Node_stu));
	new_node->id = head->id;
	new_node->help = head->help;
	new_node->next = NULL;
	int flag=0;
	struct Node_stu* last_stu = head_stu;
	if (head_stu == NULL) 
	{ 
		new_node->prev = NULL; 
		head_stu = new_node;
	} 
	else
	{
		while (last_stu->next != NULL)			//Student is inputted based on priority
		{	
			if(last_stu->help > new_node->help)	
			{
				new_node->prev = last_stu->prev;
				new_node->next = last_stu;
				last_stu->prev = new_node;
				flag = 1;
				break;
			}
			last_stu = last_stu->next;
		}
		if(flag==0)
		{
			last_stu->next = new_node;
			new_node->prev = last_stu; 
		}
	}
}
////////////////--------Tutor thread for teaching the students according to their priority-------/////////////////////////////////////////////

void *tutor(void *arg)
{
	int tutorid = *(int*)arg;
	int help_time;
	int release_id;
	
	while(1)
	{
		sem_wait(&cordintr);			//Tutor waits for coordinator to signal
		help_time = 0.2;
		pthread_mutex_lock(&lock);
		struct Node_stu* last = head_stu;
		if(last==NULL){					//checks if there are any elements in the list
			continue;
		}
		students_in_q--;				//decreases the number of students in the queue
		students_being_helped++;		//increases the number of students being helped
		total_students_tutored++;		//increases the number of students currently being helped
		release_id = head_stu->id;
		available_teachers--;
		helped_by[release_id]=tutorid;
		head_stu = head_stu->next;
		free(last);
		printf("Tu: Student %d tutored by Tutor %d. Students tutored now = %d. Total sessions tutored = %d\n",release_id,tutorid,students_being_helped,total_students_tutored);
		pthread_mutex_unlock(&lock);
		sleep(help_time);					//waiting for teacher to teach student
		pthread_mutex_lock(&lock);
		students_being_helped--;			//decreases students being helped	
		pthread_mutex_unlock(&lock);
		sem_post(&students_all[release_id]); //posts on the semaphore of the student which just got helped
		
	}
	pthread_exit(NULL);
}

/////////////////-----Coordinator thread to insert the student according to its priority in chairs------//////////////////////////////////////////////

void *coordinator(void *arg)
{
	while(1)
	{
		sem_wait(&stdnt);				//Waits for a student to arrive
		pthread_mutex_lock(&lock);
		push_to_chair();
		students_in_q++;
		printf("Co: Student %d with priority %d in the queue. Waiting students now = %d. Total requests = %d\n",head->id,head->help,students_in_q,times_visited);
		struct Node* last = head;
		head = head->next;
		free(last);
		pthread_mutex_unlock(&lock);
		sem_post(&cordintr);			//Signals tutor to wake up after student is placed on a chair
	}
	pthread_exit(NULL);	
}

//////////////////------Student thread which inserts itself in a queue from which coordinator can read its information-------////////////////////////

void *student(void *arg)
{
	int i = *(int*)arg;
	int times_help = 0;
	int programmingT;
	while(1)
	{
		programmingT = rand() % MAX_SLEEP_TIME + 1;			//student time for programming
		sleep(programmingT);								//student sleeps for programming
		pthread_mutex_lock(&lock);
		times_visited++;
		if(occupiedseats > total_chairs)
		{
			printf("St: Student %d found no empty chairs.Will try again later\n",i);
			pthread_mutex_unlock(&lock);
			continue;
		}
		else
		{
			times_help +=1;
			printf("St: Student %d going to teacher for help for %d time\n",i,times_help);
			int flag =0;
			push_to_coordinator(i,times_help);		//Student enters the queue from which coordinator reads the information of student
			occupiedseats++;						
			pthread_mutex_unlock(&lock);
			sem_post(&stdnt);						//signals coordinator that student has arrived to be put in the chair
			sem_wait(&students_all[i]);				//waits on tutor to signal 
			pthread_mutex_lock(&lock);
			occupiedseats--;
			pthread_mutex_unlock(&lock);
			printf("St: Student %d recieved help from Tutor %ld\n",i,helped_by[i]);
			if(times_help == total_number_of_helps)		//Checks if the total number of helps taken exceeds maximum allowed value
			{
				break;
			}
		}
	}		
	pthread_exit(NULL);
}

////////////////---Main function to initialize semaphores, threads and other variables ------------///////////////////////////////////////////////

int main(int argc, char *argv[])
{
	pthread_t *teacher_t, *stdnt_t, codntr;					//Declares the threads to be used
	int num_students,num_teachers,num_chairs,num_help;   	//Declares the variables to be used to get the input data from user
	int x;
	int retVal=0;
	if (argc < 5) 	//If all inputs are not given then quit
	{
		fprintf(stderr, "%s: %s nthread\n", argv[0], argv[0]);
		exit(-1);
    }
	else			//If all inputs are given then read all inputs
	{
		num_students = atoi(argv[1]);
		num_teachers = atoi(argv[2]);
		num_chairs = atoi(argv[3]);
		num_help = atoi(argv[4]);
	}
	
	sem_init(&stdnt,0,0);			//Initilization of a semaphore
	sem_init(&cordintr,0,0);		//Initilization of a semaphore

	total_teachers = num_teachers;
	available_teachers = num_teachers;
	total_number_of_helps = num_help;
	total_chairs = num_chairs;
	occupiedseats = 0;
	
	helped_by = malloc(sizeof(long)*num_students);		//Allocating size to an array which will store the teacher id of the teacher who helped a student
	
	students_all = (sem_t*)malloc(sizeof(sem_t)*num_students);		//Alloting size to all the students' semaphores as they are not pre allocated memory
	
	
	for(x=0;x<num_students;x++)						//Initializing all the students' semaphores
	{
		sem_init(&students_all[x], 0, 0);
	}
	
	pthread_create(&codntr,NULL,coordinator,NULL);
	
	teacher_t = (pthread_t*)malloc(sizeof(pthread_t)*num_teachers); //Alloting size to all the teacher threads as they are not pre allocated memory
	
	for(x=0;x<num_teachers;x++)					//Creating all teacher threads
	{
		retVal = pthread_create(&teacher_t[x],NULL,tutor,(void *)&x);
		if(retVal != 0)
		{
			printf("pthread_create failed for number %d\n",x);
			exit(EXIT_FAILURE);
		}
	}
	
	stdnt_t = (pthread_t*)malloc(sizeof(pthread_t)*num_students);	//Alloting size to all the student threads as they are not pre allocated memory
	
	for(x=0;x<num_students;x++)					//Creating all student threads
	{
		retVal = pthread_create(&stdnt_t[x],NULL,student,(void *)&x);
		if(retVal != 0)
		{
			printf("pthread_create failed for number %d\n",x);
			exit(EXIT_FAILURE);
		}
	}
	
	for(x=0;x<num_students;x++)					//Waiting for all student threads to complete execution before moving forward
	{
		retVal = pthread_join(stdnt_t[x],NULL);
		if(retVal != 0)
		{
			printf("pthread_join failed for number %d\n",x);
			exit(EXIT_FAILURE);
		}
	}

	return 0;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////