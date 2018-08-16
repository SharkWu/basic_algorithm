# -*-coding:utf-8-*-
# 快速排序 （递归）：
'''
  1 选取i、j、pivot
  2 循环置换i、j 的位置（左小置换、右大置换）
  3 对pivot前半后半两部分进行递归排序
'''
n=0
def QuickSort(L,start,end):
    global n
    if start<end:
        n+= 1
        i,j=start,end
        pivot=L[i]   #pivot存放中心点的值

        #i指向比pivot小的数，j指向比pivot大的数，比较到i=j
        while i<j:
            while i<j and L[j]>pivot:  #j大，则无需改变该元素位置，并继续前移
                j=j-1
            L[i]=L[j]                  #否则，置换且比较i

            while i<j and L[i]<=pivot:  # i小，则无需改变该元素位置，并继续后移
                i=i+1
            L[j]=L[i]                   # 否则，置换且比较j

        L[i]=pivot  #一轮比较结束，将中心值就位

        print("第%d轮排序:  "% n, L,'pivot=L[%d]=%d '%(start,pivot))

        #递归前后部分
        QuickSort(L,start,i-1)
        QuickSort(L,j+1,end)

    return L

if __name__=='__main__':
    L = [49, 38, 23, 11, 79, 97, 5, 27]
    print ('原始序列 ： ',L)
    QuickSort(L,0,len(L)-1)
    L=map(str,L)
    print ('排序后的序列：','  '.join(L))






