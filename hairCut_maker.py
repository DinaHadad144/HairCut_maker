#include<iostream>
#include<string>
using namespace std;

int main()
{
    cout << "hi our dear customer \n";
    string gender;
    cout<<"are you male or female?\n>> ";
    cin>>gender;
    if (gender == "female"){
    
    
      string kind ;
      cout<<"superhero or supervilian?\n>>: ";
      cin>>kind;
      if(kind=="superhero"){
         string state;
         cout<<"anime or sitcom?\n>> ";
         cin>>state;
         if(state=="anime")
           cout<<"you should go with bangs.";
         else if (state=="sitcom")
           cout<<"you should get a bob.";   
    
    }
      else if (kind=="supervillian"){
          cout<<"you should get a mohawk.";
      
    }
     

    
       
    
    
  }
    else if (gender=="male"){
      string kind ;
      cout<<"superhero or supervilian?\n>> ";
      cin>>kind;
      if(kind=="superhero"){
         string food;
         cout<<"steak or sushi?\n>> ";
         cin>>food;
         if(food=="steak")
           cout<<"you should get a flat top.";
         else if (food=="sushi")
           cout<<"you should get a pompadour.";   
    
   }
      else if (kind=="supervillian"){
          cout<<"you should get a mohawk.";
        
 
        }
     


   } 
    return 0;
}