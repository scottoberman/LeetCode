using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prob1883
{
    public class Solution
    {
        int[] dist;
        int speed;
        int hoursBefore;

        public int MinSkips(int[] dist, int speed, int hoursBefore)
        {
            int fewestSkips;
            this.dist = dist;
            this.hoursBefore = hoursBefore;
            this.speed = speed;
            bool[] initSkip = Enumerable.Repeat(false, dist.Length).ToArray();
            bool[] endSkip  = Enumerable.Repeat(true, dist.Length).ToArray();

            // Just initially check the base node
            // and see if we don't need to progress.
            if (CheckNode(initSkip))
                return 0;
            // Check if its even possible to reach
            // our destination within the time
            // constraints.
            else if (!CheckNode(endSkip))
                return -1;

            bool[] result = CheckRow(0, 0, 0, initSkip);

            fewestSkips = result != null ? result.Count(b => b == true) : -1;

            return fewestSkips;
        }

        private bool[] CheckRow(int depthCur, int curNodeNum, int distInd, bool[] curSkipsCheck)
        {
            int numChildren = dist.Length - depthCur - distInd;
            bool[][] children = new bool[numChildren][];
            // Generate children and check that child
            // to see if it fullfills our time requiremnts.
            for (int x = 0; x < numChildren; x++)
            {
                children[x] = new bool[dist.Length];
                curSkipsCheck.CopyTo(children[x], 0);

                int curSkipTracker = (curNodeNum) % dist.Length;
                while (children[x][curSkipTracker])
                {
                    curSkipTracker = (curSkipTracker + 1) % dist.Length;
                }

                children[x][curSkipTracker] = true;

                if(CheckNode(children[x]))
                    return children[x];
            }

            // Explore children
            for (int x = 0; x < numChildren - 1; x++)
            {
                bool[] childSuccess = CheckRow(depthCur + 1, curNodeNum + x, distInd + 1, children[x]);
                if (childSuccess != null)
                    return children[x];
            }

            return null;
        }

        private bool CheckNode(bool[] skipToCheck)
        {
            double timeTotal = 0;
            for (int x = 0; x < dist.Length; x++)
            {
                timeTotal = timeTotal + (double)dist[x] / speed;
                if (!skipToCheck[x] && x != dist.Length - 1)
                    timeTotal = Math.Ceiling(timeTotal);
            }

            return timeTotal <= this.hoursBefore;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int speed = 2;
            int hoursBefore = 10;
            int[] dist = new int[4];
            dist[0] = 7;
            dist[1] = 3;
            dist[2] = 5;
            dist[3] = 5;
            Solution sol = new Solution();
            var result = sol.MinSkips(dist, speed, hoursBefore);
            Console.Read();
        }
    }
}
