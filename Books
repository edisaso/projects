#include<iostream>
#include<stdlib.h>
using namespace std;
 class Cbook {
 public:
int inventaren_nomer;
char avtor[20], zaglavie[30];
int broi_stranici;
float cena;
 void getData();
 void display();
 
 };
 void Cbook::getData(){
 cout<<"Въведи инвентарен номер \n";cin>>inventaren_nomer;
 cout<<"Автор \n";cin.getline(avtor,20);
 cout<<"Заглавие \n";cin.getline(zaglavie,30);
 cout<<"брой страници \n";cin>>broi_stranici;
 cout<<"цена \n";cin>>cena;

 }
 void Cbook::display(){
 cout<<"Въведи инвентарен номер \n"<<inventaren_nomer<<endl;
 cout<<"Автор \n"<<avtor<<endl;
 cout<<"Заглавие \n"<<zaglavie<<endl;
 cout<<"брой страници \n"<<broi_stranici<<endl;
 cout<<"цена \n"<<cena<<endl;
 }
 float sumaCeni(Cbook maxknig[],int n){

return 0;
 }
 void KnigZadAvtor(Cbook maxknig[],int n, char zadAvtor[]){
 }
 void iztriKni(Cbook maxknig[],int &n){
 }
 void masvsknig (Cbook maxknig[],int brknig, Cbook maxknigcena[],int &brknig15){
 }
 class Cbook1{
 public:
char zaglavie[30];
float cena;
void display(){
cout<<zaglavie<< " "<<cena<<endl;
}
 };
 
 int main(){
system("chcp 1251");
char kp;
int i, brknig=0,brknig15;
Cbook masKnigi[10],masknigi15[10];
Cbook1 masknigi150[10];
char zadavtor[21];
do{
cout<<"меню ";
cout<<"1- dobavqne na danni za kniga\n";
cout<<"2 - za izvejdane na vsichki knigi\n";
cout<<"3 - za namirane i izvejdane na sumata ot cenite ot vsichki knigi\n";
cout<<"4 - za izvejdane na dannite na vsichki knigi\n";
cout<<"5 - za iztrivane na dannite na kniga\n";
cout<<"6 - za suzdavane na masiv s vsichki danni za cena s 15\n";
cout<<"posochete operaviq ili 0 za krai : \n"; cin>>kp;

switch(kp){
case '0': break;
case '1':masKnigi[brknig++].getData();break;
case'2': cout<<"spisuk na vsichki knigi \n";
for(i=0;i<brknig;i++)masKnigi[i].display();break;
case'3':cout<<"sumata na cenite ot vsichki knigi \n"<<sumaCeni(masKnigi,brknig)<<endl;
break;
case'4':cout<<"Zadaite avtora \n";cin.getline(zadavtor,20);
cout<<"knigi ot \n"<<zadavtor;
KnigZadAvtor(masKnigi,brknig,zadavtor);break;
case'5':iztriKni(masKnigi,brknig);break;
case'6':masvsknig(masKnigi,brknig,masknigi15,brknig15);
for(i=0;i<brknig15;i++)masKnigi[i].display();
break;

default: cout<<"Greshen kod na operaciq \n";
}

}while(kp!='0');
