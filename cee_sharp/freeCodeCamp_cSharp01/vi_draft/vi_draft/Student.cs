using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Object Methods
namespace vi_draft
{
    class Student
    {
        public string name;
        public string major;
        public double gpa;

        public Student(string aName, string aMajor, double aGpa)
        {
            name = aName;
            major = aMajor;
            gpa = aGpa;
        }

        public override string ToString()
        {
            return String.Format("Name: {0},\tMajor: {1},\tGPA: {2}", name, major, gpa)
            ;
        }

        // object method
        public bool HasHonors(double gpaCutoff = 3.5)
        {
            return gpa >= gpaCutoff;
        }
    }
}

