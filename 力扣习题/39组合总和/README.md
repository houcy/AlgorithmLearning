# ��Ŀ

## ����ܺ�

### ��Դ:

[����-����ܺ�](https://leetcode-cn.com/problems/combination-sum/)

### ��Ŀ����

����һ�����ظ�Ԫ�ص�����?`candidates`?��һ��Ŀ����?`target`?���ҳ�?`candidates`?�����п���ʹ���ֺ�Ϊ?`target`?����ϡ�

`candidates`?�е����ֿ����������ظ���ѡȡ��

˵����

- �������֣�����?`target`��������������
- �⼯���ܰ����ظ�����ϡ�?

### ʾ��?1��

```plaintext
���룺candidates = [2,3,6,7], target = 7,
����⼯Ϊ��
[
  [7],
  [2,2,3]
]
```

### ʾ��?2��

```plaintext
���룺candidates = [2,3,5], target = 8,
����⼯Ϊ��
[
? [2,2,2,2],
? [2,3,3],
? [3,5]
]
```

### ��ʾ��

- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- `candidate` �е�ÿ��Ԫ�ض��Ƕ�һ�޶��ġ�
- `1 <= target <= 500`
