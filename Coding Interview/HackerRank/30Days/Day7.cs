// int n = Convert.ToInt32(Console.ReadLine());
// int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));

using System;

namespace HackerRank_30Days
{

    // https://www.hackerrank.com/challenges/30-review-loop/problem
    class Day7
    {
        public void prob_array(int n, int[] arr)
        {
            int[] new_arr = new int[n];
            int j = 0;
            for (int i = n - 1; i >= 0; i--)
            {
                new_arr[j] = arr[i];
                Console.Write(new_arr[j]);
                Console.Write(" ");
                j++;
            }
        }
    }
}
