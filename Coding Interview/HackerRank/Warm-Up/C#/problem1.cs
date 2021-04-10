using System;
using System.Collections.Generic;
using System.Linq;

namespace HackerRank
{
    // https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
    class Problem1 
    {
        private static List<int> arrayNum = new List<int> { 10, 20, 20, 10, 10, 30, 50, 10, 20 };
        

        public List<int> UniqueList()
        {
            List<int> unique_arr = new List<int>();
            unique_arr = arrayNum.Distinct().ToList();
            return unique_arr;
        }
        public void Nice()
        {
            for(var i = 0; i <= arrayNum.Count - 1; i++)
            {
                Console.WriteLine(arrayNum[i]);
            }
            Console.WriteLine("Nice");
        }

        public int GetAnswer()
        {
            List<int> unique_count = new List<int>();
            // for(int x = 0; x < arrayNum.Count - 1; x++)
            // {
            //     for(int )
            // }
            return 1;
        }
    }
}