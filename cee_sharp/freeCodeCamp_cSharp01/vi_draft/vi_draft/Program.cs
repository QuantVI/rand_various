using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

// https://www.youtube.com/watch?v=GhQdlIFylQ8
// Inheritance
/* We can have one class (Sub Class) inherit all of the functionality of another class (Super Class).
*
*/
namespace vi_draft /* this is the overall project name */
{
    class Program /* class name is the name of the file*/
    {
        static void Main(string[] args) /* this is considered method - thus a Class method. */
        {
            Console.WriteLine();

            Chef chef = new Chef();
            chef.MakeTurkey();
            chef.MimicRamsay();
            chef.MakeSpecialDish();

            Console.WriteLine();

            ItalianChef talia = new ItalianChef();
            talia.MakePasta();
            talia.MimicRamsay();
            /* Below: returns "The Chef makes Shepherd's Pie." before we override anything
             *
             */
            talia.MakeSpecialDish();

            GuessingGame();

            BasicCalculator.Calculator();

            Console.WriteLine();
            Console.ReadKey();

        }

        public static void GuessingGame(string wordToGuess = "draft")
        {
            Console.WriteLine();
            string secretWord = wordToGuess;
            string guess = "";

            string[] hints = { "Starts with a '{0}'.", "Ends with a '{0}'.", "Contains a '{0}'." };

            int secretLength = secretWord.Length;
            int givenHints = 0;

            while (guess != secretWord && givenHints <= secretLength) // keep looking if guess is not the same a secretWord
            {
                Console.Write("Enter a guess: ");
                guess = Console.ReadLine();
                if (guess != secretWord)
                {
                    if (givenHints < secretLength)
                        switch (givenHints)
                        {
                            case 0:
                                Console.WriteLine(string.Format(hints[givenHints], secretWord[givenHints]));
                                givenHints++;
                                break;
                            case 1:
                                Console.WriteLine(string.Format(hints[givenHints], secretWord[secretLength-1]));
                                givenHints++;
                                break;
                            default:
                                Console.WriteLine(string.Format(hints[2], secretWord[givenHints]));
                                givenHints++;
                                break;
                        }
                    else
                    {
                        Console.Write("--------");
                        break; // out of the entire While Loop
                    }
                }
            }

            if (givenHints == secretLength)
            {
                Console.WriteLine(string.Format("You were given too many hints: {0}", givenHints));
            }

            if (guess == secretWord)
            {
                Console.Write("You guessed correctly!");
            }

        }

    }
}