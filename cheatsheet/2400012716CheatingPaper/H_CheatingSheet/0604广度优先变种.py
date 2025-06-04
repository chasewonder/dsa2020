'''
描述
公主被恶人抓走，被关押在牢房的某个地方。牢房用N*M (N, M <= 200)的矩阵来表示。矩阵中的每项可以代表道路（@）、墙壁（#）、和守卫（x）。
英勇的骑士（r）决定孤身一人去拯救公主（a）。我们假设拯救成功的表示是“骑士到达了公主所在的位置”。由于在通往公主所在位置的道路中可能遇到守卫，骑士一旦遇到守卫，必须杀死守卫才能继续前进。
现假设骑士可以向上、下、左、右四个方向移动，每移动一个位置需要1个单位时间，杀死一个守卫需要花费额外的1个单位时间。同时假设骑士足够强壮，有能力杀死所有的守卫。

给定牢房矩阵，公主、骑士和守卫在矩阵中的位置，请你计算拯救行动成功需要花费最短时间。

输入
第一行为一个整数S，表示输入的数据的组数（多组输入）
随后有S组数据，每组数据按如下格式输入
1、两个整数代表N和M, (N, M <= 200).
2、随后N行，每行有M个字符。"@"代表道路，"a"代表公主，"r"代表骑士，"x"代表守卫, "#"代表墙壁。
输出
如果拯救行动成功，输出一个整数，表示行动的最短时间。
如果不可能成功，输出"Impossible"
样例输入
2
7 8
#@#####@
#@a#@@r@
#@@#x@@@
@@#@@#@#
#@@@##@@
@#@@@@@@
@@@@@@@@ 
13 40
@x@@##x@#x@x#xxxx##@#x@x@@#x#@#x#@@x@#@x
xx###x@x#@@##xx@@@#@x@@#x@xxx@@#x@#x@@x@
#@x#@x#x#@@##@@x#@xx#xxx@@x##@@@#@x@@x@x
@##x@@@x#xx#@@#xxxx#@@x@x@#@x@@@x@#@#x@#
@#xxxxx##@@x##x@xxx@@#x@x####@@@x#x##@#@
#xxx#@#x##xxxx@@#xx@@@x@xxx#@#xxx@x#####
#x@xxxx#@x@@@@##@x#xx#xxx@#xx#@#####x#@x
xx##@#@x##x##x#@x#@a#xx@##@#@##xx@#@@x@x
x#x#@x@#x#@##@xrx@x#xxxx@##x##xx#@#x@xx@
#x@@#@###x##x@x#@@#@@x@x@@xx@@@@##@@x@@x
x#xx@x###@xxx#@#x#@@###@#@##@x#@x@#@@#@@
#@#x@x#x#x###@x@@xxx####x@x##@x####xx#@x
#x#@x#x######@@#x@#xxxx#xx@@@#xx#x#####@
样例输出
13
7
'''


def move(x,y):
    if  gra[x][y]=="x":
        gra[x][y]='@'
        vis[x][y]="gray"
        return [[x,y]]
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    nei=[]
    for item in dir:
        ix=item[0]
        iy=item[1]
        if gra[x+ix][y+iy]!='#' and vis[x+ix][y+iy]=='white':
            nei.append([x+ix,y+iy])
            vis[x+ix][y+iy]="gray"
    return nei


def save(quequ,time):
    if end in quequ:
        print(time)
        return
    else:
        if len(quequ)==0:
            print("Impossible")
            return
        else:
            nw_quequ=[]
            for item in quequ:
                nw_quequ+=move(item[0],item[1])
            quequ=nw_quequ
            save(quequ,time+1)
        


S=int(input())
for _ in range(S):
    n,m=map(int,input().split())
    gra=[['#']*(m+2) for _ in range(n+2)]
    vis=[['white']*(m+2) for _ in range(n+2)]
    for i in range(1,n+1):
        d=list(input())
        for j in range(1,m+1):
            gra[i][j]=d[j-1]
            if gra[i][j]=='r':
                start=[i,j]
            if gra[i][j]=='a':
                end=[i,j]
    vis[start[0]][start[1]]="gray"
    save([start],0)
    
    
