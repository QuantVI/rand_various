using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Static Class Attributes
namespace vi_draft
{
    class Song
    {
        public string title;
        public string artist;
        public int duration;

        /*  this staic class attrbute will not be unique per object.
         Instead, the entire class will have this attribute with whatever the static value is,
         or changes to. All object will have the same songCount.
 
            We can make static attribute be "fixed" values, like a constant, e.g. 7.
            We can also make statis class attributes update themselves, and keep track of things
            such as, the number of objects created from this Class, during that session.
         */
        public static int songCount = 0;
        // invididual objects/instances CANNOT access static Class attributes directly.
        // If mySong was a Song, then mySong.songCount DOES NOT exist.
        // Song.songCount does exist.


        public Song(string aTitle, string aArtist, int aDuration)
        {
            title = aTitle;
            artist = aArtist;
            duration = aDuration;

            // update the static Class attribute
            songCount++;
        }

        public override string ToString()
        {
            // since duration is an int, we get a whole number for duration/60
            int[] minSec = { duration / 60, duration % 60 };

            return String.Format(@"    ""{0}"" by {1}.
     Length: {2}:{3:D2}
", title, artist, minSec[0], minSec[1]);
        }

        public int getSongCount() => songCount;
    }
}

