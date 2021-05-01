using System;
using System.Collections.Generic;
using System.IO;

namespace HackerRank_30Days
{
    // https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
    class Day8
    {

        public void solve()
        {
            int numEntry = int.Parse(Console.ReadLine()); // 3

            Dictionary<string, string> entries = new Dictionary<string, string>();
            string temp = "";

            for (int i = 0; i < numEntry; i++)
            {
                temp = Console.ReadLine();
                string[] splitTemp = temp.Split(' ');

                entries.Add(splitTemp[0], splitTemp[1]);
            }

            for (int i = 0; i < numEntry; i++)
            {
                temp = Console.ReadLine();
                if (entries.ContainsKey(temp))
                {
                    Console.WriteLine("{0}={1}", temp, entries[temp]);
                }
                else
                {
                    Console.WriteLine("Not found");
                }
            }
        }
    }
}