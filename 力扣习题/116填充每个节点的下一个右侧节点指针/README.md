# ��Ŀ

## ���ÿ���ڵ����һ���Ҳ�ڵ�ָ��

### ��Դ:

[����-���ÿ���ڵ����һ���Ҳ�ڵ�ָ��](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

### ��Ŀ����

����һ��������������������Ҷ�ӽڵ㶼��ͬһ�㣬ÿ�����ڵ㶼�������ӽڵ㡣�������������£�

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

�������ÿ�� `next` ָ�룬�����ָ��ָ������һ���Ҳ�ڵ㡣����Ҳ�����һ���Ҳ�ڵ㣬�� `next` ָ������Ϊ `NULL`��

��ʼ״̬�£�����?`next` ָ�붼������Ϊ `NULL`��

### ʾ����

```plaintext
���룺{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

�����{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
```

![ʾ��ͼ](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png)

#### ���ͣ�

������������ͼ A ��ʾ����ĺ���Ӧ���������ÿ�� `next` ָ�룬��ָ������һ���Ҳ�ڵ㣬��ͼ B ��ʾ��

### ��ʾ��

- ��ֻ��ʹ�ó���������ռ䡣
- ʹ�õݹ����Ҳ����Ҫ�󣬱����еݹ����ռ�õ�ջ�ռ䲻��������Ŀռ临�Ӷȡ�
