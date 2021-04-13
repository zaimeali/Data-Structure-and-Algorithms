using System;

namespace HackerRank_30Days
{

    // https://www.hackerrank.com/challenges/30-review-loop/problem
    class Day6
    {
        public void let_review()
        {
            int T = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i < T; i++)
            {
                string S = Console.ReadLine();
                string even = "";
                string odd = "";

                for (int j = 0; j < S.Length; j++)
                {
                    if (j % 2 == 0)
                    {
                        even += S[j];
                    }
                    else
                    {
                        odd += S[j];
                    }
                }

                Console.WriteLine(even + " " + odd);
            }
        }
    }
}
