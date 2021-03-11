using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Inheritance
namespace vi_draft
{
    class Chef
    {
        public void MakeTurkey()
        {
            Console.WriteLine("The Chef makes turkey.");
        }

        public void MimicRamsay()
        {   // Use a Gordon Ramsey quote
            Console.WriteLine("Et's rotten you edjuyat.");
        }

        public void MakeSalad()
        {
            Console.WriteLine("The Chef makes salad.");
        }

        // specifying "virtual" means this method can be overriden in any subclass.
        public virtual void MakeSpecialDish()
        {
            Console.WriteLine("The Chef makes Shepherd's Pie.");
        }
    }
}