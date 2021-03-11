using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// In the tutorial this is writte in the Main method
// However, the main method is cleared and re-used for every lesson.

// https://www.youtube.com/watch?v=GhQdlIFylQ8
// Building a Better Calculator
// Four function. Extended to include exponent, and modulus

namespace vi_draft
{
    class BasicCalculator
    {
        public static void Calculator()
        {
            Console.WriteLine();

            string[] prompts = { "Enter a number: ", "Enter Operator: " };

            double num1, num2;
            string op;

            Console.Write(prompts[0]);
            num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write(prompts[1]);
            op = Console.ReadLine();

            Console.Write(prompts[0]);
            num2 = Convert.ToDouble(Console.ReadLine());

            double[] numInputs = { num1, num2 };

            string[] opers = { "+", "-", "*", "/", "**", "%", "!" };
            string msgOutput;

            if (opers.Contains(op))
            {
                msgOutput = string.Format("{0} {1} {2} = {3}", num1, op, num2, PerformOperation(numInputs, op));
            }
            else
            {
                msgOutput = ("Inavlid Operation: " + op);
            }

            Console.WriteLine(msgOutput);
        }

        static double PerformOperation(double[] nums, string oper)
        {
            double ret = 0;
            switch (oper)
            {
                case "+": ret = nums[0] + nums[1]; break;
                case "-": ret = nums[0] - nums[1]; break;
                case "*": ret = nums[0] * nums[1]; break;
                case "/": ret = nums[0] / nums[1]; break;
                case "^": ret = Math.Pow(nums[0], nums[1]); break;
                case "**": ret = Math.Pow(nums[0], nums[1]); break;
                case "%": ret = nums[0] % nums[1]; break;
                case "!":
                    double beGin = nums[0];
                    ret = 1;
                    while (beGin != 1)
                    {
                        ret = ret * beGin;
                        beGin = beGin - 1;
                    }
                    break;
            }

            return ret;
        }
    }
}
