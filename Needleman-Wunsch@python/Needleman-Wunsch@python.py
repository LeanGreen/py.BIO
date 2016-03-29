def seq_alignment(seq1,seq2):
    s=-3 #mismatch.
    m=4 #match.
    g=-4 #one gap.  
    seq1=seq1.strip()
    seq2=seq2.strip()
    if len(seq1)==0:
        print "Error, seq1 length can't be zero."
        sys.exit(1)
    elif len(seq2)==0:
        print "Error, seq2 length can't be zero."
        sys.exit(1)
    Len1=len(seq1)
    Len2=len(seq2)
    table=[]
    for i in range(len(seq1)+1):
        table.append([i*g])
    table[0]=[]
    for o in range(len(seq2)+1):
        table[0].append(o*g)
    for i in range(0,Len1):
        for j in range(0,Len2):
            if seq1[i] == seq2[j]:
                table[i+1].append(max(table[i][j]+m, table[i][j+1]+g, table[i+1][j]+g))
            else:
                table[i+1].append(max(table[i][j]+s, table[i][j+1]+g, table[i+1][j]+g))
    i=Len1-1
    j=Len2-1
    seq3 = ""
    seq4 = ""
    k=""
    if len(seq1) <= 1 and len(seq2)<=1:
        print "Error, too short!"
        sys.exit(1)
    while True:
        if i < 0 and j < 0:
            break
        if seq1[i] == seq2[j]:
            if table[i][j]+4>table[i][j+1]-4 and table[i][j]+4>table[i+1][j]-4:
                seq3 = seq1[i] + seq3
                seq4 = seq2[j] + seq4
                k = "|" + k
                i = i - 1
                j = j - 1
            else:
                if table[i][j+1] > table[i+1][j]:
                    seq3 = seq1[i] + seq3
                    seq4 = "-" + seq4
                    k = " " + k
                    i = i-1
                else:
                    seq3 = "-" + seq3
                    seq4 = seq2[j] + seq4
                    k = " " + k
                    j = j-1
        else:
            if table[i][j]-3>table[i][j+1]-4 and table[i][j]-3>table[i+1][j]-4:
                seq3 = seq1[i] + seq3
                seq4 = seq2[j] + seq4
                k = " " + k
                i = i - 1
                j = j - 1
            else:
                if table[i][j+1] > table[i+1][j]:
                    seq3 = seq1[i] + seq3
                    seq4 = "-" + seq4
                    k = " " + k
                    i = i-1
                else:
                    seq3 = "-" + seq3
                    seq4 = seq2[j] + seq4
                    k = " " + k
                    j = j-1
    return seq3, seq4, table, k
import sys
x = raw_input("sequence1:")
y = raw_input("sequence2:")
m, n, juzhen, jiange= seq_alignment(x,y)
print juzhen # Dynamic programming matrix
print m
print jiange
print n
