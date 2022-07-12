package assignment_0;
import java.util.Scanner; 
import java.util.ArrayList;
import java.util.*; 
import org.javatuples.Triplet;
//import javafx.util.Pair;

public class SocialNetwork
{
    public static int i,ind_num,business_num,group_num,organis_num,k, m,Type;  
    public static String Name, bday;
    
    public static Scanner scan = new Scanner(System.in);    
    public static void main(String args[])
    {
        
       //Creating and Deleting node of each type    
        i = 0;
        //Creating Individuals
        System.out.println("Input the number of individuals");
        ind_num = scan.nextInt();
        Individual Ilist[] = new Individual[ind_num];
        System.out.println("Input the individuals");
        while(i != ind_num)
        {
            Ilist[i] = new Individual();
            i++;
        }
        System.out.println("Individual nodes are created");
        System.out.println("Give index of individual which is to be deleted");
        //Deleting Individuals
        int index = scan.nextInt();
        if(index>=0 && index<ind_num) 
        {
            Ilist[index]=null;
            System.out.println("Inidvidual node at given index is deleted");        
        }
        
        else
        {
            System.out.println("Invalid index");
        }
        
        //Creating Businesses
        System.out.println("Input the number of businesses");
        business_num = scan.nextInt();
        Business Blist[] = new Business[business_num];
        System.out.println("Input the businesses");
        i = 0;
        while(i != business_num)
        {
            Blist[i] = new Business(Ilist,i);
            i++;
        }
        System.out.println("Business nodes are created");
        
        i = 0;
        while(i != business_num)
        {
            //Blist[i] = new Business(Ilist,i);
            //Blist[i].tell_individuals(i,Blist,Ilist);
            i++;
        }
        
        //Deleting Businesses
        System.out.println("Give index of Business which is to be deleted");
        //List B_list = Arrays.asList(Blist); 
        index = scan.nextInt();
        if(index>=0 && index<business_num) 
        {
            Blist[index]=null;
            System.out.println("Business node at given index is deleted");      
        }
        else
        {
            System.out.println("Invalid index");
        }   
        
        //Creating Groups
        System.out.println("Input the number of Groups");
        group_num = scan.nextInt(); 
        Group Glist[] = new Group[group_num];
        i = 0;
        while(i != group_num)
        {
            Glist[i] = new Group(Blist,i);
            Glist[i].make_links(Ilist,i);
            
            i++;
        }
        System.out.println("Group nodes are created");
        
//      i = 0;
//      while(i != group_num)
//      {
//          //Glist[i].make_b_links(Glist,i);
//          i++;
//      }
        
        //Deleting Groups
        System.out.println("Give index of Group which is to be deleted");
        index = scan.nextInt();
        
        if(index>=0 && index<group_num) 
        {
            Glist[index]=null;
            System.out.println("Group node at given index is deleted");     
        }
        else
        {
            System.out.println("Invalid index");
        }
        
        //  Creating Organisations 
        System.out.println("Input the number of Organisations");
        organis_num = scan.nextInt();
        Organisation Olist[] = new Organisation[organis_num];
        System.out.println("Input the Organisations");
        i = 0;
        while(i != organis_num)
        {
            Olist[i] = new Organisation();
            Olist[i].make_links(Ilist,i);
            i++;
        }
        System.out.println("Organisation nodes are created");
        
        //Deleting Organisations
        System.out.println("Give index of Organisation which is to be deleted");
        index=scan.nextInt();
        if(index>=0 && index< organis_num) 
        {
            Ilist[index]=null;
            System.out.println("Organisation node at given index is deleted");      
        }
        else
        {
            System.out.println("Invalid index");
        }
        
        //Searching based on name and bday. Type has been made into seperate arrays
       int  j = 0; int f = 0;
        System.out.println("Searching for nodes");
        
        while(j!=-1)
     {
        System.out.println("input 0 to search and -1 to quit");
        j = scan.nextInt();
        if(j==-1)
          break;
        System.out.println("If you want to search by name enter 0 else if you want to search by bday enter 1");
         k = scan.nextInt();
        
           if(k==0)
           {
            System.out.println("Give name which is to be searched");
            Name = scan.next();
            for(i=0;i<ind_num;i++)
            {
                if(Ilist[i]!=null)
                {
                    if((Ilist[i].name).equals(Name))
                    {
                        System.out.print("Node with given name has been found at index ");
                        System.out.print(i);System.out.println(" in Individuals array");
                        f = 1;
                    }
                }
            }
            
            for(i=0;i< business_num;i++)
            {
                if(Blist[i]!=null)
                {
                    if((Blist[i].name).equals(Name))
                    {
                      System.out.print("Node with given name has been found at index ");
                  System.out.print(i);System.out.println(" in Business array");
                    f = 1;
                    } 
                }
            }
            
            for(i=0;i<group_num;i++)
            {
                if(Glist[i]!=null)
                {
                    if((Glist[i].name).equals(Name))
                    {
                    System.out.print("Node with given name has been found at index ");
                      System.out.print(i);System.out.println(" in Groups array");
                    f = 1;
                   } 
                }
            }
            
            for(i=0;i<organis_num;i++)
            {
                if(Olist[i]!=null)
                {
                    if((Olist[i].name).equals(Name))
                    {
                        System.out.print("Node with given name has been found at index ");
                       System.out.print(i);System.out.println(" in Organisation array");
                       f = 1;
                    }
                }
            }
            if(f==0)
             System.out.print("Node with given name not found");
          }
           
           if(k==1)
          {
            f = 0;
            bday = scan.next();
            for(i=0;i<ind_num;i++)
            {
                if(Ilist[i]!=null)
                {
                    if(bday.equals(Ilist[i].birthday))
                    {
                        System.out.print("Node with given bday has been found");
                        f = 1;
                    }
                }
            }
            if(f == 0)
            System.out.print("No such node found");
          } 
       }
    
        //Printing indices of linked indices of a node
        
        
        System.out.println("Give index of individual whose linked nodes are to be printed");
        f = 0;
        Type = 1; m = scan.nextInt();
        if((Type == 1) && (m>=0 && m<ind_num))
        {
            System.out.print("indices of nodes linked to node with index ");
            System.out.print(k);
            System.out.print(" are: ");
            Ilist[k].show_friends();
             f=1;
        }
        
           
        if(f==0)
        System.out.println("Invaild index");

        //Posting content of a node
         System.out.println("Give type of node whose content is to be printed, Input 1 for Individual, 2 for Business,3 for Group,4 for Organisation");
        Type = scan.nextInt();
        System.out.println("Give index of node whose content is to be printed");
        m = scan.nextInt();
        f = 0;
        if((Type == 1) && (m>=0 && m<ind_num) && Ilist[m] != null)
        {
           System.out.println(Ilist[m].getContent());
           f=1;
        }
        if((Type == 2) && (m>=0 && m<business_num) && Blist[m]!=null)
         {
          System.out.println(Blist[m].getContent());    
          f=1;
         }
        if((Type == 3) && (m>=0 && m<group_num) && Glist[m]!=null)
         {
          System.out.println(Glist[m].getContent());    
          f = 1;
         }
        if((Type == 4) && (m>=0 && m<organis_num) && Olist[m]!=null)
         {
          System.out.println(Olist[m].getContent());    
          f = 1;
         }  
        if(f==0)
        System.out.println("Invaild index or type");
        // Searching a node by content
        System.out.println("Give content to be searched");
        String s_content;
        Scanner ob = new Scanner(System.in);
        s_content = ob.nextLine();
        f = 0; 
        for(i=0;i<ind_num;i++)
        {
            if(Ilist[i]!=null)
            {
                if((Ilist[i].content).equals(s_content))
                {
                    System.out.print("Node with given content has been found at index ");
                    System.out.print(i);System.out.println(" in Individuals array");
                    f = 1;
                }
            }
        }
        for(i=0;i< business_num;i++)
        {
            if(Blist[i]!=null)
            {
                if((Blist[i].content).equals(s_content))
                {
                  System.out.print("Node with given content has been found at index ");
                  System.out.print(i);System.out.println(" in Business array");
                  f = 1;
                } 
            }
        }
        for(i=0;i<group_num;i++)
        {
            if(Glist[i]!=null)
            {
                if((Glist[i].content).equals(s_content))
                {
                System.out.print("Node with given content has been found at index ");
                  System.out.print(i);System.out.println(" in Groups array");
                f = 1;
               } 
            }
        }
        for(i=0;i<organis_num;i++)
        {
            if(Olist[i]!=null)
            {
                if((Olist[i].content).equals(s_content))
                {
                    System.out.print("Node with given content has been found at index ");
                   System.out.print(i);System.out.println(" in Organisation array");
                   f = 1;
                }
            }
        }
        if(f==0)
         System.out.print("Node with given content not found");
        System.out.println(" ");
        
        
        //Posting content by nodes linked to a node 
        System.out.println("Give index of individual whose connected nodes content is to be printed");
        k = scan.nextInt();
        if(Ilist[k]!=null && k>=0 && k<ind_num)
        {
            Ilist[k].print_friends();
        }
       //ystem.out.println("Which organisations you want whose individuals should print their content. Give index");
        
//        k = scan.nextInt();
//        
        
        ob.close();
        scan.close();
  }
}
       
     class Nodes
        {
            int id,n;
            String name;
            String creation_date;
            String content;
            Scanner scan = new Scanner(System.in);
            public  Nodes()
            {
                
                System.out.println("Enter the id:");
                this.id = Integer.parseInt(scan.nextLine()); 
                //scan.nextLine();
                System.out.println("Enter the name:");
                this.name = scan.nextLine();
                //System.out.print("You have entered: "+this.name);
                System.out.println("Enter the creation date:");
                this.creation_date = scan.nextLine();
                //System.out.print("You have entered: "+this.creation_date);
                //Scanning content from userSystem.out.print("You have entered: "+str);
                //scan.nextLine();
                System.out.println("Enter the content:");
                this.content = scan.nextLine();
//              System.out.println("Enter the number of nodes this node is connected to :");
//              this.n = scan.nextInt();
            }
            //Nodes [] links = new Nodes[n] ; 
            public String getContent()
            {
                return (this.content);
            }
    }

       class Individual extends Nodes 
      {
         String birthday;
         Scanner obj=new Scanner(System.in); int n;
         ArrayList<Business>my_shop_list = new ArrayList<Business>();
         int i = 0;
         //ArrayList<Integer>b_links = new ArrayList<Integer>();
         public Individual()
         {
           System.out.println("Enter your birthday");
           this.birthday = obj.next();
         }
         
        ArrayList<Triplet<Integer, Integer, Individual> >friends=new ArrayList<Triplet<Integer, Integer, Individual> >();
         
         public void add_body(ArrayList<Triplet<Integer, Integer, Individual> >members)
         {
             for(int j=0;j<members.size();j++)
             {
                if(!(members.get(j).getValue2().equals(this)))
                    friends.add(members.get(j));
             }
         }
         
         public void show_friends()
         {
             for(int j=0;j<friends.size();j++)
             {
                 //System.out.println("Link");
                System.out.print(friends.get(j).getValue0());
                System.out.print(" ");
                
             }
         }
         
         public void print_friends()
         {
             System.out.println("Contents of Individuals connected to this node are");
             for(int j=0;j<friends.size();j++)
             {
                 //System.out.println("Link");
                System.out.println(friends.get(j).getValue2().content);
             }
         }
         
//         public void my_shop(Business b)
//         {
//             my_shop_list.add(b);
//         }
         
         
         
      }
         
         
      class Business extends Nodes 
      {
         int x;int y; int c; int j;
         Integer owner;
         Scanner obj=new Scanner(System.in);
         ArrayList<Integer> customers = new ArrayList<Integer>(); 
        
        
         public Business(Individual [] arr,int index)
         {
           System.out.println("Enter your x co-ordinate");
           this.x = obj.nextInt();
           System.out.println("Enter your y co-ordinate");
           this.y = obj.nextInt();
           System.out.println("Does this business have an owner? Input 1 if yes,0 if no");
            c = obj.nextInt();
            if(c==1)
            {
                System.out.println("Give index of the owner in the array of Individuals");
                j = obj.nextInt();
                if(j>=0 && j< arr.length)
                {
                    owner = j;
                    //b_members.add(j);
                    //arr[j].get_linkindex(1,index);
                    System.out.println("Owner has been defined for this business");
                }
            }
          
         System.out.println("Does this business have an customers? Input 1 if yes,0 if no");
         c = obj.nextInt();
         j=0;
         while(c==1 && j!=-1)
          {
            System.out.println("Give indices of the customers in the array of Individuals.Enter -1 if no further customers");
            j = obj.nextInt();
            if(j>=0 && j< arr.length && arr[j]!=null) 
            { 
                customers.add(j);
                //arr[j].get_linkindex(1,index);
              //  b_members.add(j);
            }
               
          }
         if(c==1)
         System.out.println("Customers have been defined for this business");
         }
      } 
         
         
         
       

        class Organisation extends Nodes 
      {
         int xo;int yo; int i;int c;
         ArrayList<Integer> O_link = new ArrayList<Integer>(); 
         ArrayList<Triplet<Integer, Integer, Individual> >members=new ArrayList<Triplet<Integer, Integer, Individual> >();
         Scanner obj = new Scanner(System.in);
         public Organisation()
         {
           System.out.println("Enter your x co-ordinate");
           this.xo = obj.nextInt();
           System.out.println("Enter your y co-ordinate");
           this.yo = obj.nextInt();
         }
   
         
          public void make_links(Individual [] arr,int index)
         {
           System.out.println("Give the connected individuals in the organisation. Give 1 if yes. else 0");
           for(i=0;i<arr.length;i++)
           {
               System.out.print("Is the individual at index "); System.out.print(i);
               System.out.print("  a part of the organisation?");
               this.c=obj.nextInt();
               if(c==1 && arr[i]!=null)
               {
                   Triplet<Integer, Integer, Individual> triplet = new Triplet<Integer, Integer, Individual>(i,index,arr[i]);
                   members.add(triplet);
                   O_link.add(i);
               }
               
           }
           for(i=0;i<arr.length;i++)
           {
               if(arr[i]!= null)
               { 
                   arr[i].add_body(members);
               }
           }
           
         }
      }
        
        
               
        
        
        class Group extends Nodes
      {
            
         ArrayList<Triplet<Integer, Integer, Business> >B_members=new ArrayList<Triplet<Integer, Integer, Business> >(); 
         //ArrayList<Integer> G_link = new ArrayList<Integer>(); 
         ArrayList<Triplet<Integer, Integer, Individual> >G_members=new ArrayList<Triplet<Integer, Integer, Individual> >();
         Scanner obj = new Scanner(System.in);
         int c;int k;
         public Group(Business [] arr,int index)
         {
            System.out.println("Does this group have businesses as members? Input 1 if yes,0 if no");
            c = obj.nextInt();
           // int j = 0;
            if(c==1)
            {
                System.out.println("Give the connected businesses in the organisation. Give 1 if yes. else 0");
               for(int i=0;i<arr.length;i++)
               {
                   System.out.println("Is the Business at index "); System.out.print(i);
                   System.out.print(" is a part of the organisation?");
                  this.k= obj.nextInt();
                  if(k==1)
                  {
                      Triplet<Integer, Integer, Business> triplet = new Triplet<Integer, Integer, Business>(i,index,arr[i]);
                      B_members.add(triplet);
                  }
              }
            }  
            if(c==1)
            System.out.println("Businesses have been added to this group");
         }
         public void make_links(Individual [] arr,int index)
         {
           System.out.println("Give the connected individuals in the organisation. Give 1 if yes. else 0");
           for(int i=0;i<arr.length;i++)
           {
               System.out.println("Is the individual at index "); System.out.print(i);
               System.out.print(" is a part of the organisation?");
               this.c=obj.nextInt();
               if(c==1 && arr[i]!=null)
               {
                   Triplet<Integer, Integer, Individual> triplet = new Triplet<Integer, Integer, Individual>(i,index,arr[i]);
                   G_members.add(triplet);
               }
               
           }
         }
    
     }  
        
      
        
    