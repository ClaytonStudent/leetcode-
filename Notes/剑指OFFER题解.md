## 剑指offer题解

### 3. 数组中重复的数字

题目：在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字

```python
# python solution
class Solution(object):
	def findRepeatNumber(self,nums):
		dic = {}
		for n in nums:
			dic[n] = dic[n]+1 if dic.get(n) else 1
            if dic[n] > 1:
                return n
         return -1
# 循环交换，降低空间复杂度到O(1)
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return -1
```

```java
// java solution 1
class Solution {
    public int findRepeatNumber(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i:nums){
            if (set.contains(i)){
                return i;
                }else{
                    set.add(i);
                } 
        }
        return -1;
    }
}
// 循环交换，降低空间复杂度到O(1)        
class Solution {
    public int findRepeatNumber(int[] nums){
        int tmp;
        for (int i = 0;i<nums.length;i++){
            while(i!=nums[i]){
                if(nums[i]==nums[nums[i]]){
                    return nums[i];
                } 
                tmp = nums[i];
                nums[i] = nums[tmp];
                nums[tmp] = tmp;
            }
        }
        return -1;
    }
}
```

```javascript
// javaScript solution
var findRepreatNumber = function(nums){
    const map = {};  // this map is an object
    for (const num of nums){
        if(!map[num]){
            map[num]= true;
        }else{
            return num;
        }
    }
    return -1;
}
// after ES6 we can use Map
var findRepeatNumber = function(nums) {
    const map = new Map(); // this map is a map
    for (const num of nums){
        if(!map.has(num)){
            map.set(num,true);
        }else{
            return num;
        }
    }
    return -1;
};
```

### 4.二位数组中的查找

题目：在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

```python
# python: 右上角开始
class Solution(object):
    def findNumberIn2DArray(self,matrix,target):
        if not matrix:
            return None
        m,n = len(matrix),len(matrix[0])
        i,j = 0,n-1
        while i<m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
# python: 从左下角开始。抛弃mn，好处是不用专门判断为空
class Solution(object):
    def findNumberIn2DArray(self,matrix,target):
        i,j = len(matrix) -1,0
        while i>=0 and j <len(matrix[0]):
            if matrix[i][j] > target:
                i-=1
            elif matrix[i][j] < target:
                j+=1
            else:
                return True
        return False
```

```java
// java, begins with bottom left
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        int i = matrix.length - 1, j = 0;
        while(i >= 0 && j < matrix[0].length)
        {
            if(matrix[i][j] > target) i--;
            else if(matrix[i][j] < target) j++;
            else return true;
        }
        return false;
    }
}

```

```javascript
// js begins with bottom left
var findNumberIn2DArray = function(matrix,target){
    let i = matrix.length -1, j = 0;
    while(i >= 0 && j < matrix[0].length){
        if(matrix[i][j] > target) i--;
        else if(matrix[i][j] < target) j++;
        else return true;
    }
    return false;
}
```

### 5. 替换空格

请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

```python
class Solution:
    def replaceSpace(self, s):
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)
```

```java
class Solution {
    public String replaceSpace(String s) {
        StringBuilder res = new StringBuilder(); 
        // StringBuilder内部也是封装的一个字符数组，只不过该数组非final修饰，可以不断修改
        for(Character c:s.toCharArray()){  // string to array
            if(c==' ') res.append("%20");
            else res.append(c);
        }
		return res.toString(); // array to string
    }
}
```

```javascript
var replaceSpace = function(s) {
    return s.replace(/ /g, "%20");   // g使用此修饰符后，搜索时会查找所有的匹配项
};
```

### 6.从尾到头打印链表

题目：输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）

```python
class Solution(object):
    def reversePrint(self,head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
```

```java
class Solution {
    public int[] reversePrint(ListNode head) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        while(head != null) {
            // insert a specific element at the end of a LinkedList
            stack.addLast(head.val); 
            head = head.next;
        }
        int[] res = new int[stack.size()];
        for(int i = 0; i < res.length; i++)
            //  remove the last element from the LinkedList, and return the element
            res[i] = stack.removeLast(); 
    return res;
    }
}
```

```javascript
var reversePrint = function (head){
    const res = []
    while (head){
        res.push(head.val)
        head = head.next
    }
    return res.reverse()
}
```

### 7. 重建二叉树

```python
class Solution(object):
    def buildTree(self,preorder,inorder):
        if not preorder or not inorder:
            return None
       	root_val = preorder[0]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree(preorder[1+index:],inorder[index+1:])
        return root
```

```java
class Solution {
    HashMap<Integer, Integer> dic = new HashMap<>();
    int[] po;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        po = preorder;
        for(int i = 0; i < inorder.length; i++) 
            dic.put(inorder[i], i);
        return recur(0, 0, inorder.length - 1);
    }
    TreeNode recur(int pre_root, int in_left, int in_right) {
        if(in_left > in_right) return null;
        TreeNode root = new TreeNode(po[pre_root]);
        int i = dic.get(po[pre_root]);
        root.left = recur(pre_root + 1, in_left, i - 1);
        root.right = recur(pre_root + i - in_left + 1, i + 1, in_right);
        return root;
    }
}

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // java 递归版本待议

    }
}
```

```javascript
var buildTree = function (preorder, inorder) {
    if (!preorder.length || !inorder.length) return null
    let root = preorder[0]; // 前序遍历的第一个元素为根节点
    let node = new TreeNode(root); // 确定根节点

    let i = inorder.indexOf(root); // 获取根节点在中序遍历中的位置(用于分割左右子树)

    // 递归
    node.left = buildTree(preorder.slice(1, i + 1), inorder.slice(0, i));
    node.right = buildTree(preorder.slice(i + 1), inorder.slice(i + 1));
    return node
};
```

### 9.用两个栈实现队列

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

```python
class CQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def appendTail(self,value):
        self.stack1.append(value)
    def deleteHead(self):
        if self.stack2:
            return self.stack2.pop()
       	if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
```

```java
class CQueue{
    LinkedList<Integer> A,B;
    public CQueue(){
        A = new LinkedList<Integer>();
        B = new LinkedList<Integer>();
    }
    public void appendTail(int value){
        A.addLast(value);
    }
    public int deleteHead(){
        if(!B.isEmpty()) return B.removeLast();
        if(A.isEmpty()) return -1;
        while(!A.isEmpty())
            B.addLast(A.removeLast());
       	return B.removeLast();
    }
}
```

```javascript
var CQueue = function(){
    this.inStack = [];
    this.outStack = [];
};
CQueue.prototype.appendTail = function(value){
    this.inStack.push(value);
};
CQueue.prototype.deleteHead = function(){
    if(this.outStack.length) return this.outStack.pop();
    if(!this.inStack.length) return -1;
    while(this.inStack.length){
        this.outStack.push(this.inStack.pop());
    }
    return this.outStack.pop();
}
```

### 10 斐波那契

```python
class Solution:
    def fib(self,n):
        a,b = 0,1
        for _ in range(n):
            a,b = b, a+b
        return a
```

```java
class Solution {
    public int fib(int n) {
        int a = 0, b = 1, sum;
        for (int i=0;i<n;i++){
            sum = (a+b);
            a = b;
            b = sum;
        }
        return a;
    }
}
            
```

```javascript
var fib = function(n) {
    let a = 0,b = 1;
    for(let i = 0;i<n;i++){
        let sum = (a+b)%1000000007;
        a = b;
        b = sum;
    }
    return a
};
```

### 11.旋转数组的最小数字

```python
class Solution(object):
    def minArray(self, numbers):
        if not numbers:
            return None
        left, right = 0, len(numbers)-1
        while left < right:
            mid = (left+right)//2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]
```

```java
class Solution {
    public int minArray(int[] numbers) {
        int left = 0, right = numbers.length -1;
        while (left < right){
            int mid = (left+right) / 2; //直接就取整数了
            if (numbers[mid]<numbers[right]) right = mid;
            else if (numbers[mid]>numbers[right]) left = mid +1;
            else right-=1;
        }
        return numbers[left];
    }
}
```

```javascript
var minArray = function(numbers) {
    let left = 0, right = numbers.length-1;
    while (left < right){
        let mid = Math.floor((left+right)/2); // Math.floor()
        if (numbers[mid]<numbers[right]) right= mid;
        else if(numbers[mid]>numbers[right]) left = mid+1;
        else right-=1;
    }
    return numbers[left];
};
```

### 14.剪绳子

```python
class Solution(object):
    def cuttingRope(self, n):
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        sub = [0,1,2,3]
        for i in range(4,n+1):
            max_val = 0
            for j in range(1,i//2+1):
                max_val = max(max_val,sub[j]*sub[i-j])
            sub.append(max_val)
        return sub[-1]
```

```java
class Solution {
    public int cuttingRope(int n) {
        if (n <= 3) return n-1;
        int[] sub = new int [n+1];
        sub[1] = 1;
        sub[2] = 2;
        sub[3] = 3;
        for (int i=4; i < n+1; i++){
            int max_val = 0;
            for (int j = 1; j < i/2+1; j++){
                max_val = Math.max(max_val,sub[j]*sub[i-j]);
            }
            sub[i] = max_val;
        }
        return sub[n];
    }
}
```

```javascript
var cuttingRope = function(n) {
    if(n<=3) return n-1;
    const dp = new Array(n+1).fill(1);
    dp[2] = 2;
    dp[3] = 3;
    for(let i=4;i<=n;i++){
        let max_val = 0;
        for (let j=1;j<Math.floor(i/2+1);j++){
            max_val = Math.max(max_val,dp[j]*dp[i-j]);
        }
        dp[i] = max_val;
    }
    return dp[n];
};
```

### 15. 二进制中1的个数

```python
class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        while n:
            ans += 1
            n = (n-1) & n
        return ans
```

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n!=0){
            ans += 1;
            n = (n-1) & n;
        }
        return ans;
    }
}
```

```javascript
var hammingWeight = function(n) {
    let ans = 0;
    while(n!=0){
        ans += 1;
        n &=(n-1);
    }
    return ans;
};
```

### 16.数值的整数次方

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        # 如果n是负数，则转成n大于0的范围内
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x # 将当前 xx 乘入 res
            x *= x # 执行平方
            n >>= 1 # 右移1位
        return res
```

```java
class Solution {
    public double myPow(double x, int n) {
        if(x == 0) return 0;
        long b = n;
        double res = 1.0;
        if(b < 0) {
            x = 1 / x;
            b = -b;
        }
        while(b > 0) {
            if((b & 1) == 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }
}
```

### 18 删除链表节点

```python
class Solution(object):
    def deleteNode(self, head, val):
        pre, cur = head, head.next
        if pre.val == val:
            return cur
        while cur and cur.val != val:
            pre,cur = cur,cur.next
        if cur:
            pre.next = cur.next
        return head
```

```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        if(head.val == val) return head.next;
        ListNode pre = head, cur = head.next;
        while(cur != null && cur.val != val) {
            pre = cur;
            cur = cur.next;
        }
        if(cur != null) pre.next = cur.next;
        return head;
    }
}
```

```javascript
var deleteNode = function(head, val) {
    let pre = head, cur = head.next;
    if(pre.val == val) return cur;
    while(cur != null && cur.val != val) {
        pre = cur;
        cur = cur.next;
    }
    if(cur != null) pre.next = cur.next;
    return head;
    }
```

### 21. 奇数在偶数之前

```python
class Solution(object):
    def exchange(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            while left < right and  nums[right] & 1 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
```

```java
class Solution {
    public int[] exchange(int[] nums) {
        int left = 0, right = nums.length -1, tmp;
        while(left < right){
            while(left < right && (nums[left] & 1) == 1) left ++;
            while(left < right && (nums[right] & 1) == 0) right --;
            tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
        }
        return nums;
    }
}
```

```javascript
var exchange = function(nums) {
    let left = 0, right = nums.length-1, tmp;
    while(left < right){
        while(left < right && (nums[left] & 1) == 1) left ++;
        while(left < right && (nums[right] & 1) == 0) right --;
        tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
    }
    return nums;
};
```

### 22.链表中倒数第k个节点

```python
class Solution(object):
    def getKthFromEnd(self, head, k):
        if not head or k <= 0:
            return None
        node = head
        while head and k >0:
            head = head.next
            k -= 1
        while head:
            node = node.next
            head = head.next
        if k == 0:
            return node
```

```java
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        if(head == null || k <= 0) return null;
        ListNode node = head;
        while(head != null && k > 0){
            head = head.next;
            k -= 1;
        } 
        while(head != null){
            node = node.next;
            head = head.next;
        }
        return node;
    }
}
```

```javascript
var getKthFromEnd = function(head, k) {
    if(head == null || k <= 0) return null;
    let node = head;
    while(head != null && k > 0){
        head = head.next;
        k -= 1;
        } 
    while(head != null){
        node = node.next;
        head = head.next;
        }
    return node;
    }
```

### 24 反转链表

```python
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            dummy = cur.next
            cur.next = pre
            pre, cur = cur, dummy
        return pre
```

```java
class Solution {
    public ListNode reverseList(ListNode head) {

        ListNode pre = null;
        ListNode cur = head;
        ListNode dummy = null;
        while(cur != null){
            dummy = cur.next;
            cur.next = pre;
            pre = cur;
            cur = dummy;
        }
        return pre;
    }
}
```

```javascript
var reverseList = function(head) {
    let pre = null, cur = head, dummy = null;
    while(cur != null){
        dummy = cur.next;
        cur.next = pre;
        pre = cur;
        cur = dummy;
    }  
    return pre;
};
```

### 25 合并排序链表

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = root = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        root.next = l1 or l2
        return head.next
```

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode root = head;
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                root.next = l1;
                l1 = l1.next;
            }else{
                root.next = l2;
                l2 = l2.next;
            }
            root = root.next;
        }
        root.next = l1 != null? l1:l2;
        return head.next;
    }
}
```

```javascript
var mergeTwoLists = function(l1, l2) {
    let head = new ListNode(0);
    let root = head;
    while(l1 != null && l2 != null){
        if(l1.val <= l2.val){
            root.next = l1;
            l1 = l1.next;
        }else{
            root.next = l2;
            l2 = l2.next;
        }
        root = root.next;
        }
    root.next = l1 != null? l1:l2;
    return head.next;
    }
```

### 26 树的子结构

```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode):
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
```

```java
class Solution {
    public boolean isSubStructure(TreeNode A, TreeNode B) {
        return (A != null && B != null) && (recur(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B));
    }
    boolean recur(TreeNode A, TreeNode B) {
        if(B == null) return true;
        if(A == null || A.val != B.val) return false;
        return recur(A.left, B.left) && recur(A.right, B.right);
    }
}

```

