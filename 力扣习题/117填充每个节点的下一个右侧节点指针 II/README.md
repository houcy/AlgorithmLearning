# ��Ŀ

## ���ÿ���ڵ����һ���Ҳ�ڵ�ָ�� II

### ��Դ:

[����-���ÿ���ڵ����һ���Ҳ�ڵ�ָ�� II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

### ��Ŀ����

����һ��������

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

�������ÿ�� `next` ָ�룬�����ָ��ָ������һ���Ҳ�ڵ㡣����Ҳ�����һ���Ҳ�ڵ㣬�� next ָ������Ϊ NULL��

��ʼ״̬�£�����?`next` ָ�붼������Ϊ `NULL`��

### ʾ����

![ʾ��](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)

```plaintext
���룺root = [1,2,3,4,5,null,7]
�����[1,#,2,3,#,4,5,7,#]
```

#### ���ͣ�������������ͼ A ��ʾ����ĺ���Ӧ���������ÿ�� next ָ�룬��ָ������һ���Ҳ�ڵ㣬��ͼ B ��ʾ��

### ���ף�

- ��ֻ��ʹ�ó���������ռ䡣
- ʹ�õݹ����Ҳ����Ҫ�󣬱����еݹ����ռ�õ�ջ�ռ䲻��������Ŀռ临�Ӷȡ�
