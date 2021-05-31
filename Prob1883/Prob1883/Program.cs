using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prob1883
{
    //public class Solution
    //{
    //    public int MinSkips(int[] dist, int speed, int hoursBefore)
    //    {


    //        int minSkipsSoFar = 0;
    //        bool minSkipFound = false;
    //        Dictionary<int, int> skips = new Dictionary<int, int>();

    //        // Step 1: Skip all stops to see if its even possible
    //        // to arrive on time.
    //        double timeToTravelNoSkip = dist.Sum() / speed;
    //        if (timeToTravelNoSkip > hoursBefore)
    //            return -1;

    //        // Step 2Maybe: Check time without skipping anything
    //        if ()





    //        // Step 2maybe: Attempt to skip the largest value in the array?
    //        //         (This may be complicated by the fact that
    //        //          a user must wait until the next full hour to leave if not skipping a thing)
    //        while (!minSkipFound && minSkipsSoFar < dist.Length)
    //        {
    //            skips.Max()

    //        }

    //        // Step 3: Repeat step 2 until done?
    //    }

    //    /// <summary>
    //    /// Initially, just brute force permutations 
    //    /// until we find fewest skips. (Eventually, wanna do
    //    /// sort of a BFS rather than this sort of random
    //    /// search).
    //    /// </summary>
    //    /// <param name="dist"></param>
    //    /// <param name="speed"></param>
    //    /// <param name="hoursBefore"></param>
    //    /// <returns></returns>
    //    private int FindFewestSkips(int[] dist, int speed, int hoursBefore)
    //    {
    //        bool[] locsSkipped = new bool[dist.Length];
    //        int totalPerms = (int)Math.Pow(2, dist.Length);

    //        for(int x = 0; x < totalPerms; x++)
    //        {
    //            for(int y = 0; y < dist.Length; y++)
    //            {
    //                if ((y - x) % dist.Length == 0)
    //                    locsSkipped[y] = true;
    //                else
    //                    locsSkipped[y] = false;
    //            }
    //        }
    //    }
    //}


    class Program
    {
        static void TestLoopStuff()
        {
            int[] dist = new int[3];
            dist[0] = 0;
            dist[1] = 1;
            dist[2] = 2;

            TreeNode perms = new TreeNode(dist.Length);


        }
        static void Main(string[] args)
        {
            TestLoopStuff();
            Console.Read();
        }
    }
}
