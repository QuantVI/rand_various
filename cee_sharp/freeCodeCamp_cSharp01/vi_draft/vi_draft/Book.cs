using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


//  Book.cs - for the Book class
//  Constructors

namespace vi_draft
{
    class Book
    {   // Class Attributes
        public string title;
        public string author;
        public int pages;

        // This is the constructor for this class.
        // Called when we create an object of this class
        public Book(string aTitle, string anAuthor, int thePages)
        {
            title = aTitle;
            author = anAuthor;
            pages = thePages;
            Console.WriteLine("... Creating Book ... {0}", title);
        }
    }
}

