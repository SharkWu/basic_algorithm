# -*-coding:utf-8-*-
# 归并排序 （递归）：
'''
  1 左右拆分
  2 递归左半右半执行排序（直到L长为1）
  3 构建merge函数合并有序序列（设置指针ij指向首尾）
  4 每次递归retuern 对两半的merge
  '''

# 合并函数：a、b两个序列作有序合并
def merge(a,b):
    c=[]     # c存放合并后的字符串
    i=j=0    #i、j，初始指针为0

    #比较a/b的元素，直到其中一段序列比完
    while i<len(a) and j<len(b):

        # 提出较小值插入新的序列中，并后移指针
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    #将未比完的序列的剩余元素插入c中
    if i==len(a):
        for x in b[j:]:
            c.append(x)
    else:
        for y in a[i:]:
            c.append(y)
    return c

def merge_sort(L):
    if len(L)<=1:
        return L
    mid=len(L)//2
    #左右拆分
    left=merge_sort(L[:mid])
    right=merge_sort(L[mid:])

    return merge(left,right) #合并

if __name__=='__main__':
    L = [49, 38, 23, 11, 79, 97, 5,27]
    print('原始序列 ： ', L)
    L = map(str, merge_sort(L))
    print('排序后的序列：', '  '.join(L))
