__author__ = 'sckaira'

import matplotlib.pyplot as plt
import numpy as np
lines1= []
lines15 = []
lines15Index = []
lines1Corr = []

def plotGraph(oneSegmentFile, twoSegmentFile, dest, title, xl):
    global lines1,lines15,lines15Index,lines1Corr
    lines1= []
    lines15 = []
    lines15Index = []
    lines1Corr = []
    with open(oneSegmentFile) as foneSeg:
        lines1 = foneSeg.read().splitlines()

    with open(twoSegmentFile) as ffifteenSeg:
        lines15 = ffifteenSeg.read().splitlines()

    lines1 = map(float, lines1)
    lines15 = map(float, lines15)

    const = range(0,len(lines1))
    #lines15Index = [h[0] for h in sorted(enumerate(lines15), key=lambda x:lines15[1])]
    lines15Index = sorted(range(len(lines15)),key=lambda x:lines15[x])

    #lines1.sort()
    for i in range(0, len(lines15Index)):
        lines1Corr.append(lines1[lines15Index[i]])
    lines15.sort()


    print title
    print "mean:" + str(round(np.mean(lines1Corr),5)) + " variance:" + str(round(np.var(lines1Corr),)) + " standard deviation=" + str(round(np.std(lines1Corr),3))

    print "mean:" + str(round(np.mean(lines15),5)) + " variance:" + str(round(np.var(lines15),3)) + " standard deviation=" + str(round(np.std(lines15),3))






plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\_avg.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\Segment15\_avg.txt", "P_1_15_avg.png",
            "Portland Dog Data 1 Segment Vs 15 Segment Avg",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')



plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\_avg_.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\HDCT\_avg.txt", "S_1_HDCT_avg.png",
          "Stanford Dog Data 1 Segment Vs HDCT Avg(dog,dog-walker,leash) data",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\dog_.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\HDCT\dog.txt", "S_1_HDCT_dog.png",
          "Stanford Dog Data 1 Segment Vs HDCT Dog data",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')



plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\dog-walker_.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\HDCT\dog-walker_.txt", "S_1_HDCT_dog-walker.png",
           "Stanford Dog Data 1 Segment Vs HDCT Dog-walker data",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')



plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\leash_.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\HDCT\leash_.txt", "S_1_HDCT_leash.png",
          "Stanford Dog Data 1 Segment Vs HDCT Leash data",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')


plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\_avg.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\Segment15\_avg.txt", "S_1_15_avg.png",
          "Stanford Dog Data 1 Segment Vs 15 Segment Avg data",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')


plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\dog.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\Segment15\dog.txt", "S_1_15_dog.png",
          "Stanford Dog Data 1 Segment Vs 15 Segment Dog data",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')


plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\dog-walker.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\Segment15\dog-walker.txt", "S_1_15_dog-walker.png",
          "Stanford Dog Data 1 Segment Vs 15 Segment Dog-walker data",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\segment1\leash.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Stanford\Segment15\leash.txt", "S_1_15_leash.png" ,
          "Stanford Dog Data 1 Segment Vs 15 Segment Leash data",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\_avg.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\HDCT\_avg.txt", "P_1_HDCT_avg.png",
          "Portland Dog Data 1 Segment Vs HDCT Avg(dog,dog-walker,leash)",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\dog.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\HDCT\dog.txt", "P_1_HDCT_dog.png",
           "Portland Dog Data 1 Segment Vs HDCT Dog",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')


plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\dog-walker.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\HDCT\dog-walker.txt", "P_1_HDCT_dog-walker.png",
          "Portland Dog Data 1 Segment Vs HDCT Dog-walker",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\leash.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\HDCT\leash.txt", "P_1_HDCT_leash.png",
          "Portland Dog Data 1 Segment Vs HDCT Leash",
          'Images (1 to 500) - 1 Segment(Blue) - HDCT (Red)')



plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\dog.txt",
        "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\Segment15\dog.txt", "P_1_15_dog.png",
           "Portland Dog Data 1 Segment Vs 15 Segment Dog",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')

plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\dog-walker.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\Segment15\dog-walker.txt", "P_1_15_dog-walker.png",
          "Portland Dog Data 1 Segment Vs 15 Segment Dog-walker",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')


plotGraph("C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\segment1\leash.txt",
          "C:\Users\sckaira\Desktop\Courses\MLProject\Final Results\Portland\Segment15\leash.txt", "P_1_15_leash.png",
          "Portland Dog Data 1 Segment Vs 15 Segment Leash",
          'Images (1 to 500) - 1 Segment(Blue) - 15 Segment (Red)')