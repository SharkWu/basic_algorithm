# -*-coding:utf-8-*-
# 堆排序 （大顶堆）：
'''
  1 L首位+0不处理
  2 构建一个调整父子关系函数
  3 构建大顶堆（从n/2调整）
  4 在大顶堆的基础上从1开始调整父子（首尾置换、for循环调整（len-1））
  '''

# 父子调整函数:
def element_exchange(L,low,len):
    temp = L[low] # temp存储替换值
    i=low         # i存储替换指针
    j=2*i         # j指向low节点的左孩子节点

    while j<=len:
        if j<len and L[j]<L[j+1]:# j<len，即j=len-1
            ## low有两个孩子,需对孩子比较
            j=j+1

        #将父与大孩子比较，父小则置换
        if temp<L[j]:
            L[i]=L[j]
            i=j
            j=i*2
            L[i] = temp
        else:
            break
    return L

def heap_sort(L):

    # 1 指定第一个需要调整的元素的下标：即完全二叉树的第一个非叶子节点（第n/2个）
    length=len(L)-1
    first_ex=int(length/2)
    print('从 L(' + str(first_ex) + ')=' + str(L[first_ex])+' 开始调整:')

    # 2 建立初始堆L[]
    for x in range(first_ex):
        element_exchange(L,first_ex-x,length)
    print ('初始堆：',str(L))

    # 3 将根节点放到最终位，length-1次循环
    for y in range(length-1):
        # 首尾置换
        temp=L[1]
        L[1]=L[length-y]
        L[length-y]=temp

        L=element_exchange(L,1,length-y-1)
        # 调整其他元素位置，从根往下调，每次调整忽略序列后y位（已有序）
        print("第%d轮排序后: " % (y + 1) +str(L[1:]))

if __name__=='__main__':
    L = [49, 38, 23, 11, 79, 97, 5, 27,2,12]
    L.insert(0, 0)
    # 元素的存储从1开始，下标0处插入0，不参与排序
    heap_sort(L)
    L=map(str,(L[1:]))
    print ('排序后的序列：'+'  '.join(L))
