#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct dumi{
	char ime[51];
	dumi *next;
};

dumi st;
dumi *head=NULL, *p, *q;

void readDumi()
{

	printf("\nIme: ");gets(st.ime);
	
	getchar(); //паразитния 'Enter'
	printf("-----------------\n");
}

void showDumi(dumi *st)
{
	printf("Stringa %s\n",st->ime);
	
	printf("--------------------------------\n");
}

void createElement()
{
	if ((p=new dumi)==NULL){printf("Nedostatuchna pamet....\n");getch();return;}
	readDumi();
	strcpy(p->ime,st.ime);
	p->next=NULL;
}

void createFirst()
{
	printf("Suzdavane na purvi element...\n");
	if (head!=NULL) {printf("Veche ima purvi...\n");getch();return;}
	createElement();head=p;q=p;
}

void addDumi()
{
	printf("Dobavqne na informaciq...\n");
	if (head==NULL) {printf("Ne e suzdaden purvi...\n");getch();return;}
	createElement();q->next=p;q=p;
}

void showAll()
{
	printf("\tSpisak:\n---------------------------\n");
	if (head==NULL) {printf("Spisaka e prazen...\n");getch();return;}
	p=head;
	while (p!=NULL)
	{
		showDumi(p);p=p->next;
	}
	getch();
}

void findByName()
{
	char name[51];// ключ за търсене
	int nameren=0; //флаг за "намерен", 0 - няма такъв
	printf("Tursene s ime: ");gets(name);
	p=head;
	while (p!=NULL) //докато не е стигнат краят на списъка
	{
		if (strcmp(p->ime,name)==0) {nameren=1; showDumi(p);}
		p=p->next;
	}
	if (nameren==0) printf("Nqma takava duma...\n");
	getch();
}

void changeDumiByIme()
{
	char name[7];// ключ за търсене
	int nameren=0; //флаг за "намерен", 0 - няма такъв
	printf("Promqna na element s ime: ");gets(name);
	p=head;
	while (p!=NULL) //докато не е стигнат краят на списъка
	{
		if (strcmp(p->ime,name)==0) {
			nameren=1; readDumi();
			strcpy(p->ime,st.ime);	
			printf("Dannite sa obnoveni...\n");
			break;
		}
		p=p->next;
	}
	if (nameren==0) printf("Nqma takuv chovek...\n");
	getch();
}
void delprocen()
{
	
	int nameren=0; char * pch;
	p=head;q=head;
	while (p!=NULL) //докато не е стигнат краят на списъка
	{
		char current=p->ime[2];char current1=p->ime[4];
		   if(current == '%' && current1 =='a'){                            
			   if (p==head) head=head->next;//ако елементът е първи
			nameren=1; q->next=p->next;  //връзка със следващия
		   delete p;
		   printf("Element iztrit...");
			break;
		   }
		   q=p;p=p->next;
	   }
	   if (nameren==0)printf("Nqma takuv element...\n");
        getch();
}
void removeDumibyIme()
{
	char name[7];// ключ за търсене
	int nameren=0; //флаг за "намерен", 0 - няма такъв
	printf("Iztrivane na string s ime: ");gets(name);
	p=head;q=head;
	while (p!=NULL) //докато не е стигнат краят на списъка
	{
		
		if (strcmp(p->ime,name)==0) { //при съвпадение
			if (p==head) head=head->next;//ако елементът е първи
			nameren=1; q->next=p->next;  //връзка със следващия
			delete p;
			printf("Element iztrit...");
			break;
		}
		q=p;p=p->next;
	}
	if (nameren==0) printf("Nqma takuv...\n");
	getch();
}

void removeAll()
{
	p=head;   printf("\n");
	while(p!=NULL){
		q=p->next; delete p; p=q;
		printf(".");
	}
	head=NULL;
	printf("\nSpisaka iztrit!\n");getch();
}


void exportToTxtFile(){
	FILE *txt=NULL; char fileName[255];
	printf("Ekspotirane na faila v tekstov fail s ime: ");gets(fileName);
	txt=fopen(fileName,"wt");
	if (txt==NULL){printf("Neuspeh pri otvarqne za pisane\n");getch();return;}

	char header[255]=" име \n";
	fputs(header,txt);

	p=head;
	while(p!=NULL)//докато (не е стигнат краят на списъка)   //докато опитът е успешен
	{	//обработка
		char red[255]; //буфер за текстовия файл - един ред
		char num[10];
	    strcpy(red,p->ime);strcat(red,"\t");
		
		strcat(red,"\n");
		fputs(red,txt); //запис на реда в текстовия файл
		p=p->next;//опит за следващо четене на данни
	}
	fclose(txt);
	printf("Spisaka e uspeshno ekspotiran...");getch();
}

void importFromTxtFile()
{
	FILE *txt=NULL; char fileName[255];
	printf("Impotirane na tekst ot tekstov fail s ime: ");gets(fileName);
	txt=fopen(fileName,"rt");
	if (txt==NULL){printf("Neuspeh pri otvarqne\n");getch();return;}
	char header[255];fgets(header,255,txt); //прочитане на заглавието - "паразитна" за БД информация
	char red[255]; //буфер (ред) за четене от текстовия файл
	fscanf(txt,"%s ",st.ime);//опит за четене
	while(!feof(txt))//докато (не е стигнат краят на файла)
	{
		if ((p=new dumi)==NULL){printf("Недост. памет...");return;getch();};
		printf("."); p->next=NULL;
		strcpy(p->ime,st.ime); // прехвърляне от буфера на файла в елемента от списъка
		if (head==NULL) {head=p;q=head;}
		else {q->next=p;q=p;}

		fscanf(txt,"%s ",st.ime);//опит за следващо четене

	}
	printf("\n");fclose(txt);
	printf("BD e uspeshno impotirana...");getch();
}

void main()
{
	

	system("chcp 1251"); char izb='0';

	do{
	   system("cls");
	   printf("\t\tMAIN MENU\n");
	   printf("1. Suzdavane na purvi element v spisaka\n");
	   printf("2. Dobavqne na elementi v spisaka\n");
	   printf("3. Razglezhdane na spisaka\n");
	   printf("4. Tursene po ime\n");
	   printf("5. Aktualizaciq po ime\n");
	   printf("6. Iztrivane na element ot spisaka po ime\n");
	   printf("q. Iztrivane na element ot spisaka s procent na 3ta poziciq i a na 5ta\n");
	   printf("7. Iztrivane na celiq spisak\n");
	   printf("8. Export ==> txt file\n");
	   printf("9. Import <== txt file\n");
	   printf("\n\nVashiq izbor: /0-izhod\n");izb=getch();
	   switch(izb){
			case '1':createFirst();break;
			case '2':addDumi();break;
		    case '3':showAll();break;
		    case '4':findByName();break;
		    case '5':changeDumiByIme();break;
		    case '6':removeDumibyIme();break;
		    case '7':removeAll();break;
		    case '8':exportToTxtFile();break;
		    case '9':importFromTxtFile();break;
		    case 'q':delprocen();break;
	   }
	   
	}while(izb!='0');
	removeAll();
}
