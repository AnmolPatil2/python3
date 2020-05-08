#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int i=0;


struct node
{
   char name[5];
   int batch_no,count;
   float price;
   struct date
   {
      int month;
      int year;   
   }d;
   struct node *link;
};

struct medicine
{
   char name[5];
   int batch_no,count;
   float price;
   struct exp
   {
      int month;
      int year;   
   }d;
};



struct medicine medi[20];
typedef struct node* med;


med getnode()
{
    med x;
    x = (med )malloc(sizeof(struct node));
    char name[5];
    int batch_no;
    int month,year;
   
    if(x == NULL)
    {
         printf("out of memory");
         exit(0); 
    }
    return x;
}


int search(int batch_no,med first)
{
    med cur;
    cur = first;
    
   
    if(first == NULL)
    {
       
       return 0;
      

    }
     
  
    while(cur->link != NULL)
    {
        
        if(cur->batch_no ==  batch_no)
        {
             
             return 1;
             
        }
        cur = cur->link;
    }
  return 0;
   
}

med display(med first)
{

    med cur;
    cur = first;
    
    printf("NAME\tBATCH\tCOUNT\tPRICE\t\tEXPIRY DATE\n");
    while(cur->link != NULL)
    {  
      printf("%s\t%d\t%d\t%f\t%d-%d\n",cur->name,cur->batch_no,cur->count,cur->price,cur->d.month,cur->d.year); 
      cur = cur->link;
    }
    printf("%s\t%d\t%d\t%f\t%d-%d\n",cur->name,cur->batch_no,cur->count,cur->price,cur->d.month,cur->d.year); 
   return first;
}
        
        


med entry(med first)
{  
    med temp;
    int flag;
    char name[25];
    int batch_no,count;
    float price;
    int month,year; 
    printf("NAME OF THE MEDICINE :\t");

    scanf("%s",name);
    printf("BATCH NUMBER :\t");
    scanf("%d",&batch_no);
    
    flag = search(batch_no,first);


     

    if(flag == 1)
    {
        printf("MEDICINE ALREADY EXISTS");
        return first;
    }
   
       printf("QUANTITY:\t");
       scanf("%d",&count);
       printf("PRICE:\t");
       scanf("%f",&price);
       printf("EXPIRING MONTH :\t");
       scanf("%d",&month);
       printf("EXPIRING YEAR :\t");
       scanf("%d",&year);
       pt=fopen("medicine","a");


   
       temp = getnode();
    
       strcpy(temp->name,name);
       temp->batch_no = batch_no;
       temp->count = count;
       temp->price = price; 
       temp->d.month = month;
       temp->d.year = year;
  
       temp->link = NULL;
       

       if(first == NULL) 
       {
           return temp;
       } 
       
       temp->link = first;
       return temp;
     

}

void delete(med first)
{
   int month,year;
   printf("enter month and year:\n");
   scanf("%d%d",&month,&year);
  
   med cur;
   cur = first;

   while(cur->link != NULL)
   {
      if(cur->d.year < year)  
      {       
            printf("%s\t\t%d\t%d\t\t%f\t%d-%d\n",cur->name,cur->batch_no,cur->count,cur->price,cur->d.month,cur->d.year); 
      }
      
  
      else if(cur->d.year = year)
      {
          if(cur->d.month < month)
          {       
            printf("%s\t\t%d\t%d\t\t%f\t%d-%d\n",cur->name,cur->batch_no,cur->count,cur->price,cur->d.month,cur->d.year); 
          }
     
      }
      else
      {
         continue;
      }
   cur = cur->link;
   }
}  

void count_decrease(int batch_no,med first,int count)
{
      med cur;
      cur = first;
      char name[5];
      int quantity,batch;
      float price;
      int month,year;
   
      while(cur->link != NULL)
      {
           if(cur->batch_no == batch_no)
           {
                if(cur->count >= count)
                {
                     cur->count = cur->count - count ;

                     strcpy(medi[i].name,cur->name);
                     /*batch = cur->batch_no;
                     count = cur->count;
                     price = cur->price;
                     month = cur->d.month;
                     year = cur->d.year;*/ 
                        
                      
                     medi[i].batch_no = cur->batch_no;
                     medi[i].count = cur->count;
                     medi[i].price = cur->price;
                     medi[i].d.month = cur->d.month;
                     medi[i].d.year = cur->d.year;
                     
                     /*medi[i].batch_no = batch;
                     medi[i].count = count;
                     medi[i].price = price;
                     medi[i].d.month = month;
                     medi[i].d.year = year;
                     */
                     
                     i++;
                         
                }
             
                else
                {
                  printf("STOCK INSUFFICIENT\n");
                                   
                }
           }
        
               
           
      cur = cur->link;
      }
      

}
    

med bill(med first)
{
 
    char name[5];
    med cur;
    int batch_no,count,flag,choice;
    int a;int c=0;
    
    
    
    while(1)
    {
 
       printf("enter 1 for bill and 0 for exit\n ");
       scanf("%d",&a);
       
   
       if(a==1)
       { 
          printf("enter name :\t");
          scanf("%s",name);
          printf("enter batch number:\t");
          scanf("%d",&batch_no);
          printf("count:\t");
          scanf("%d",&count);
          count_decrease(batch_no,first,count);
          c = c+1;

       }
       else
       {

         printf("NAME\tBATCH\tCOUNT\tPRICE\tEXIPRY DATE\n");
         for(i=0;i<c;i++)
         {
           printf("%s\t%d\t%d\t%f\t%d-%d",medi[i].name,medi[i].batch_no,medi[i].count,medi[i].price,medi[i].d.month,medi[i].d.year);
           /*printf("%d",medi[i].batch_no);
           printf("%d",medi[i].count);
           printf("%f",medi[i].price);
           printf("%d-%d",medi[i].d.month,medi[i].d.year);*/
           printf("\n");
         }
         
       }
    }
    
   
    return first;   
   
}

void main()
{
    med first;
    int choice;
    first = NULL;
    printf("************************************************************************************************************************************************************************************************************");
printf("**********************************************************************************SARKAR MEDICAL STORE MANAGEMENT*******************************************************************************************");
printf("************************************************************************************************************************************************************************************************************");

     
    while(1)
    {    

                   
               printf("\n\n\n");  
               printf("\t\t\t 1. MEDICINE ADDITION  \t\t\t 2.STOCK DISPLAY \t\t\t 3. STOCK DELETION\t\t\t4.STOCK PURCHASE\n");
               printf("ENTER A CHOICE :\n");
               scanf("%d",&choice);
    
               switch(choice)
               {
                    case 1 : first = entry(first);
                             break;
                    case 2 : first = display(first);
                             break;
                    case 3 : delete(first);
                             break;
                    case 4 : first = bill(first);
                             break;
                    default :exit(0);
               }  
    }    
}










