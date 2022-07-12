#include<iostream>
#include <dirent.h>
#include <sys/types.h>
#include <fstream>
#include <string>
#include <unistd.h>
#include <sys/stat.h>
#include <algorithm>
# include <bits/stdc++.h>

using namespace std;

bool cmp(pair<int,int> p1,pair<int,int> p2)
{
	return(p1.first>p2.first);
}

bool cmp2(pair<int,string> p1,pair<int,string> p2)
{
	return(p1.first>p2.first);
}


// searches for substrings 
int isSubstring(string s, string s2)
{
    int M = s.length();
    int N = s2.length();
 
    /* A loop to slide pat[] one by one */
    for (int i = 0; i <= N - M; i++) {
        int j;
 
        /* For current i i, check for
 pattern match */
        for (j = 0; j < M; j++)
            if (s2[i + j] != s[j])
                break;
 
        if (j == M)
            return i;
    }
 
    return -1;
}

// sorting 2d vector
bool sortcol( const vector<int>& v1, 
               const vector<int>& v2 ) { 
 return v1[1] < v2[1]; 
} 

int removeDupWord(string str,string w)
{
	//cout<<"str: "<<str;

	char mm[str.size()];
	for(int i=0;i<str.size();i++)
	{
		mm[i]=str[i];
	}
	//mm[str.size()]='\0';

    // Returns first token
    int count = 0; 
    char *token = strtok(mm, " ");
  
    // Keep printing tokens while one of the
    // delimiters present in str.
    while (token != NULL)
    {
    	string h=token;
        //printf("%s\n", token);
        if(h == w)
        {
        	//cout<<"SAME"<<endl;
        	count++;
        }
        token = strtok(NULL, " ");
        //cout<<"IN"<<endl;
    }
    return count;
}

//Opening directory and making input.txt file
void make_list() 
{
	DIR *dr;
	struct dirent *en;
	ifstream fin; int flag = 0; int c =1;
   //string dir, filepath,filepath1,s; 
   //ofstream ff,f1;
   struct stat filestat;
  // std::string item_name;
   //string item_name;
   ifstream nameFileout;
   /* 
    Making list of books in i.txt
   */

   dr = opendir("/home/sanyukta/Downloads/Assignment-1 (1)/Directory1"); //open the directory
   ofstream file;
   string s;
   file.open ("input.txt");
   if (dr) 
   {
   	int k=0;

    while ((en = readdir(dr)) != NULL) 
     {
        {
         	if(k<2)
         	{
         		k++;
         		continue;
         	}
          cout<< "Input the type of book "<< en->d_name<<" is"<<'\n';
          cin >> s;
          file << en->d_name<<" - "<<s<<"\n";
        }
         
     }
     file.close();
   }   
   
   
   closedir(dr);
    return;
    
}

void print_listname()
{
	DIR *dr;
   struct dirent *en;
   ifstream fin; int flag = 0; int c =1;
   string dir, filepath,filepath1,s; 
   ofstream ff,f1;
   struct stat filestat;
   std::string item_name;
   //string item_name;
   ifstream nameFileout;
   string path = "/home/sanyukta/Downloads/Assignment-1 (1)/Directory1";
    dr = opendir("/home/sanyukta/Downloads/Assignment-1 (1)/Directory1"); //open the directory
    ff.open("list.txt");	f1.open("list1.txt");
    int h=0;


     if (dr) 
    {
   	   
      cout<<'\n';
      cout <<"List :" <<'\n';
      int k = 0;
      while ((en = readdir(dr)) != NULL) 
       {
          if(k<2)
          {
            k++;
            continue;
          }

          cout<< c <<") File name: "<< en->d_name<<'\n';
          c++;
          filepath = path + '/' + en->d_name; 
          //cout<<"filepath: "<<filepath<<endl;

          fin.open(filepath);
		      string l;
		      

  			while (!fin.eof())
  			{
  				 fin>>item_name;
  			   if(item_name == "Title" || item_name == "Author" )
  			   	{
  			   		getline(fin,l);
  			   		cout <<item_name<<l<<'\n';
  			   		ff<<item_name<<l<<'\n'; 
  			   		flag++;
  			   		//cout<<"flag_inner: "<<flag<<endl;
  			   		continue;
  			   	}	
  			   //	ff<<'\n';
  			   if(flag == 2)
  			   {
  			   	flag=0;
  			   	filepath.clear();
  			   	fin.close();
  			   	cout<<'\n';
  			   	break;
  			   }
  			} 

	 		fin.close();

	    }		
     
   }  
   ff.close();
   closedir(dr);
}

void search_name()
{
   DIR *dr;
   struct dirent *en;
   ifstream fin; int flag = 0; int c =1;
   string dir, filepath,filepath1,s; 
   ofstream ff,f1;
   struct stat filestat;
   std::string item_name;
   //stclosedir(dr);ring item_name;
   ifstream nameFileout;

   string path1 = "/home/sanyukta/2nd_year/sem4/Software Engineering/Labs/list.txt"; 
   string st; char ch;
   ch='0'; string m;
    
    
    cout << "Give name of title or author character by character of book to be searched, For stopping give 0: "<<'\n';
    while(1)
    {
    	
    	cin >> ch;
    	//cout <<"matching list is :"<<'\n';
    	if(ch=='0')
    	  break;  	
    	st = st+ch;
    }

    fin.open(path1);

    int u=0;
    
	while(getline(fin,m))
	{
		//cout<<"Hey"<<'\n';
		
		transform(m.begin(), m.end(), m.begin(), ::tolower);
		transform(st.begin(), st.end(), st.begin(), ::tolower);
		
		if(u%2==0)
		{ 
			
			m=m.substr(8, m.size()-1);
			//cout << "m:"<<m<<'\n';
			s = m;
		}
		else
		{
			m=m.substr(9, m.size()-1);
		}

		u++;
		if(isSubstring(st,m)!=-1)
		{	
			//cout<<"Hey"<<'\n';
			cout << s<<'\n'; 
			f1 << s <<'\n' ; 
		}
		
	}
	//<<"Hey"<<'\n';
  fin.close();
}
void print_book()
{
     //DIR *dr;
   struct dirent *en;
   ifstream fin; int flag = 0; int c =1;
   string dir, filepath,filepath1,s; 
   ofstream ff,f1;
   struct stat filestat;
   std::string item_name;
   //string item_name;
   ifstream nameFileout;

	string name,s2; 
  string path = "/home/sanyukta/Downloads/Assignment-1 (1)/Directory1";  
   cout << "Given name of book to printed "<<'\n';
    cin.ignore();
    getline(cin, name, '\n');
   //cin >> name;
    string path2;
   path2 = path + '/' + name+".txt";
   //cout<<path<<'\n';
   fin.open(path2);

   while(getline(fin,s2))
   {
    cout<<s2<<'\n'; 
   }  
    fin.close();
}

string removeWord(string str, string w)
{
    if (str.find(w) != string::npos)
    {
        size_t p = -1;
        string tempWord = w + " ";
        while ((p = str.find(w)) != string::npos)
            str.replace(p, tempWord.length(), "");

        tempWord = " " + w;
        while ((p = str.find(w)) != string::npos)
            str.replace(p, tempWord.length(), "");
    }

    return str;
}
int countFreq(string &pat, string &txt)
{
    int M = pat.length();
    int N = txt.length();
    int res = 0;

    /* A loop to slide pat[] one by one */
    for (int i = 0; i <= N - M; i++)
    {
        /* For current i i, check for
           pattern match */
        int j;
        for (j = 0; j < M; j++)
            if (txt[i+j] != pat[j])
                break;

        // if pat[0...M-1] = txt[i, i+1, ...i+M-1]
        if (j == M)
        {
           res++;
           j = 0;
        }
    }
    return res;
}
void display(const set<pair<int,string>>& s,int k)
{
    bool found = false;
    int n=5;set<pair<int,string>>::iterator it;
    it=s.end();
    it--;
    // range-based for loop
   while(n>0 && k!=0)
        {
         
         cout << " Count: "<<(*it).first <<'\n';
         if(k!=1)
         cout<< (*it).second;
        n--;
        it--;
        k--;
        cout <<'\n';
    }
}


void print_top5()
{
   DIR *dr;
   ifstream fin;
   struct dirent *en;
   string w;
   cout << "Give w to be searched "<<'\n';
        cin >> w;
    cout <<"Give value of top k paras or chapters to be printed"<<'\n';
    int k1;
    cin>>k1;
    cout<<"Give 1 if displaying paras with w and give 2 to display chapter names "<<'\n';
    int j;
    cin >> j;  
    if(j==1)
  {
         string path3,path4,w,s4;
     dr = opendir("/home/sanyukta/Downloads/Assignment-1 (1)/Directory1"); //open the directory
     path4 = "/home/sanyukta/Downloads/Assignment-1 (1)/Directory1";
     vector<string>v1; int count = 0;
     int number=0; 
     vector<vector<string>>top2; vector<vector<int>>top1; int max=0;  
     //string s;
     //file.open ("input.txt");
     if (dr) 
     {
        int k=0;
        int cntt=0;


        vector<pair<int,string> >final;
        while ((en = readdir(dr)) != NULL) 
      {
        
              
              if(k<2)
              {
                k++;
                continue;
              }
               if(j==1) 
               
                  {
                    cout<< "If "<< en->d_name<<" is a novel give n else give p"<<'\n';
                    char a;
                    cin>>a; 

                    if(a=='p')
                    continue;
                    //fin >> w ;
                    //cout << "Give ch for displaying top k chapters and ph for displaying top k paragraphs"<<'\n';
                    //cin >> s4;
                    
                    path3 = path4+'/'+en->d_name ; 
                  }
                  
                  if(j == 1)
                  {
                
                    fin.open(path3);
                    //cout<<"PATH3333"<<endl;
                    vector<pair<int,int> > v;
                    int h=0;


                    map<int,string> mp;
                    v.clear(); mp.clear();

                    //cout<<"above "<<endl;
                    //cout<<"w: "<<w<<endl;
                    while(getline(fin,w) && !fin.eof())
                    {
                      count=0; //cout<<"w first: "<<w<<endl;
                      string para=""; 

                      while(w.size()!=0 && w.size()!=1 && !fin.eof())
                        {
                          para=para+w.substr(0,w.size())+"\n";
                          //cout<<"w: "<<w<<endl;
                           //cout<<"para: "<<para<<endl;
                          //cout<<"w.size(): "<<w.size()<<endl;
                          count += removeDupWord(w,w);
                                getline(fin,w);
                                
                        }  

                      //cout<<"count: "<<count<<endl;
                      //cout<<"para: "<<para<<endl;
                      //cout<<"#####################################################################"<<endl;
                      v.push_back(make_pair(count,h));

                      mp.insert(make_pair(h,para));

                      h++;  

                    }   

                  sort(v.begin(), v.end(), cmp);
                  // for(int i=0;i<v.size();i++)
                  // {
                  //  cout<<v[i].first<<","<<v[i].second<<endl;
                  // }      

                  for(int i=0;i<k1;i++)
                  {

                    //cout<<mp[v[i].second]<<endl;
                    //cout<<"count:- "<<v[i].first<<endl;
                    // cout<<"##############################################"<<endl;
                    final.push_back(make_pair(v[i].first,mp[v[i].second]));
                  }
                       // cout<<"##############################################"<<endl;
                        fin.close();
                    
                }

        

      }
          cout<<"----------------------------------------------------------------"<<endl;
          cout<<"FOR NOVELS:-"<<endl;

            sort(final.begin(), final.end(), cmp2);  

            for(int i=0;i<k1;i++)
            {
              cout<<final[i].second<<endl;
              cout<<"count:- "<<final[i].first<<endl;
            cout<<"##############################################"<<endl;
            }

      cout<<"-------------------------------------------------------------------"<<endl;      
           

      }
  }
  //closedir(dr);

    if(j==2)
    {
              string srt1,srt2 ;
          srt2="CHAPTER";
          //string w;
          //cout<<"enter the w "<<endl;
          //cin>>w;
          ifstream myfile1;
          //myfile1.open("doc1.txt");
          string path2 = "/home/sanyukta/2nd_year/sem4/Software Engineering/Labs/";
          path2 = path2 +"doc1.txt" ;
           myfile1.open(path2);
          set<pair<int,string>>s;
           int position = 0;
           int i; int w1=0; string sname;
           do{
            getline(myfile1,srt1);
           }
           while((i = srt1.find(srt2, position)) == string::npos);//chapter 1 found
           cout<<srt1<<endl;
           sname=srt1;
          while(getline(myfile1,srt1))
          {
             if((i = srt1.find(srt2, position)) == string::npos)
                {
                w1=w1+countFreq(w,srt1);
             }
                else
              {
                s.insert(make_pair(w1,sname));    
                sname=srt1;
                w1 = 0 ;
              }
          }
          display(s,k1);
          myfile1.close();
    }  

}

 bool isUpper(string s) {

    if (std::all_of(s.begin(), s.end(), [](unsigned char c){ return std::isupper(c); })) {
        return(true);
    } else {
        return(false);
    }
}
// string removeWord(string str, string w)
// {
//     if (str.find(w) != string::npos)
//     {
//         size_t p = -1;
//         string tempWord = w + " ";
//         while ((p = str.find(w)) != string::npos)
//             str.replace(p, tempWord.length(), "");

//         tempWord = " " + w;
//         while ((p = str.find(w)) != string::npos)
//             str.replace(p, tempWord.length(), "");
//     }

//     return str;
// }



void list_char()
{
  set<string> s;
    string srt1,srt2,srt3;
    srt2="SCENE";
    string w;
    cout<<"Enter the character name"<<endl;
    cin>>w;
  ifstream myfile1;
  int position=0; int i;
  int chfound=0;
  string path3 = "/home/sanyukta/2nd_year/sem4/Software Engineering/Labs/";
  path3 = path3+"doc2.txt";
  myfile1.open(path3);
  do{
    getline(myfile1,srt1);
   }
   while((i = srt1.find(srt2, position)) == string::npos);//chapter 1 found
   cout<<srt1<<endl;
   while(getline(myfile1,srt1))
   {
        if((i = srt1.find(srt2, position)) == string::npos)
        {
         srt3= removeWord(srt1,".");
         if((i = srt3.find(w, position)) != string::npos)
            chfound=1;
         if(chfound==1 && isUpper(srt3) && srt3!=w)
            s.insert(srt3);
       }
       else
       {
           chfound=0;
       }
   }
   // set<int>::iterator itr;
   cout<<"**************LIST OF CHARACTERS FOUND WITH "<<w<<"***********"<<endl;
    for(auto itr=s.begin();itr!=s.end();itr++)
        cout <<*itr<<endl;
}

int main()
{
   DIR *dr;
   struct dirent *en;
   ifstream fin; int flag = 0; int c =1;
   string dir, filepath,filepath1,s; 
   ofstream ff,f1;
   struct stat filestat;
   std::string item_name;
   //string item_name;
   ifstream nameFileout;
   
   int j;
   cout<<"Input 1 to make i.txt"<<'\n';
   cout<<"Input 2 to print list"<<'\n'; 
   cout<<"input 3 to search by title ar author"<<'\n';
   cout<<"input 4 to print a book"<<'\n';
   cout<<"Input 5 to print top 5 paragraphs/chapters where w occurs"<<'\n';
   cout <<"Input 0 to stop LMS"<<'\n';

   while(j!=0)
   {
     cin>>j;
     if(j==1){make_list();}
     if(j==2){ print_listname();} 
     if(j==3){ search_name();}
     if(j==4){ print_book();}
     if(j==5)
      { 
        cout << "Give 'n' for novels and give 'p' for plays"<<'\n';
        char c;
        cin >> c;
        if(c == 'n')
        print_top5();
        if(c == 'p')
        list_char();
      }
  
   }
   
   
   return(0);
}
