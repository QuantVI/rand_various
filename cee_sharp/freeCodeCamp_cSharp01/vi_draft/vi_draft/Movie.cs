using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Getters and Setters
// Assume a movie can only be rated G, PG, PG-13, R, NR.
// How can we ensure/enforce we only get these ratings - within the Movie Class?

namespace vi_draft
{
    class Movie
    {
        public string title; // "public" : any other program or code can access this
        public string director;

        // "private" : only code within the Movie class can access rating.
        private string rating; // by making this private, it is exposed to be set, only at construction.
        /* Moreover, rating cannot be accessed ("get") directly. Such as with
         myMovie.rating
 
            Instead, we can only get or set rating by using a Class Method.
            1. The constructor (which we write)
            2. Some other method we write
 
            This allows us to check a given value for rating against the values we wish to allow.
        */

        public override string ToString()
        {
            string filler = @"    Movie: {0}
    By: {1}
    Rated: {2}
";
            return String.Format(filler, title, director, rating);
        }

        public Movie(string aTitle, string aDirector, string aRating)
        {
            title = aTitle;
            director = aDirector;
            Rating = aRating;
        }

        // the getters ans setter allow outside code to acces and modify/set the rating or other private item
        public string Rating
        {
            get => rating; // this does the same thing as the line below
            // get { return rating; }
            set
            {
                // we can define rules for setting rating, within here
                string[] validRatings = { "G", "PG", "PG-13", "NC-17", "R", "NR" };
                rating = validRatings.Contains(value) ? value : "NR";
            }
        }
    }
}

