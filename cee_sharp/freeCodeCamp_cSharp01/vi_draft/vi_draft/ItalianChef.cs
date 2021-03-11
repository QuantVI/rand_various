using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Inheritance
namespace vi_draft
{
    class ItalianChef : Chef // inherits all functionality from the Chef class.
                             // ItalianChef is considered the Sub-class
                             // Chef is considered the Super-class

    {
        public void MakePasta()
        {
            Console.WriteLine("The Italian Chef makes pasta.");
        }

        // We override the MakeSpecialDish method, using the override identifier
        public override void MakeSpecialDish()
        {
            Console.WriteLine("The Italian Chef makes chicken alfredo.");
        }

    }
}


