
import java.util.*;

public class Solution {
    // No.03
    public int findRepeatNumber(int[] nums){
        Set<Integer> set = new HashSet<Integer>();
        for(int i:nums){
            if (set.contains(i)) return i;
            else set.add(i);
        }
        return -1;
    }

    public int findRepeatNumber_(int[] nums){
        int tmp;
        for(int i = 0; i < nums.length; i ++){
            while(i!=nums[i]){
                if(nums[i] == nums[nums[i]]) return nums[i];
                tmp = nums[i];
                nums[i] = nums[tmp];
                nums[tmp] = tmp;
            }
        }
        return -1;
    }

    // No.04
    public boolean findNumberIn2DArray(int[][] matrix, int target){
        int i = matrix.length - 1, j = 0;
        while (i >= 0 && j < matrix[0].length){
            if (matrix[i][j] > target) i--;
            else if (matrix[i][j] < target) j++;
            else return true;
        }
        return false;
    }

    // No.05
    public String replaceSpace(String s){
        StringBuilder res = new StringBuilder();
        for(Character c:s.toCharArray()){
            if (c == ' ') res.append("%20");
            else res.append(c);
        }
        return res.toString();
    }

    // No.06
    public int[] reversePrint(ListNode head){
        LinkedList<Integer> stack = new LinkedList<Integer>();
        while (head != null){
            stack.addLast(head.val);
            head = head.next;
        }
        int[] res = new int[stack.size()];
        for(int i = 0; i < res.length; i++) res[i] = stack.removeLast();
        return res;
    }

    // No.07
    HashMap<Integer, Integer> dic = new HashMap<>();
    int [] po;
    public TreeNode buildTree(int[] preorder, int[] inorder){
        po = preorder;
        for (int i = 0; i < inorder.length; i++) dic.put(inorder[i],i);
        return recur(0,0,inorder.length-1);
    }
    TreeNode recur(int pre_root, int in_left, int in_right){
        if (in_left > in_right) return null;
        TreeNode root = new TreeNode(po[pre_root]);
        int i = dic.get(po[pre_root]);
        root.left = recur(pre_root+1,in_left,i-1);
        root.right = recur(pre_root+i-in_left,i+1,in_right);
        return root;
    }

    // No.10
    public int fib(int n){
        int a = 0, b = 1, sum;
        for (int i = 0;i < n; i++){
            sum = (a+b);
            a = b;
            b = sum;
        }
        return a;
    }

    // No.11
    public int minArray(int[] numbers){
        int left = 0, right = numbers.length - 1;
        while (left < right){
            int mid = (left + right) / 2;
            if (numbers[mid] < numbers[right]) right = mid;
            else if (numbers[mid] > numbers[right]) left = mid + 1;
            else right -= 1;
        }
        return numbers[left];
    }

    // No.14
    public int cuttingRope(int n){
        if (n <= 3) return n-1;
        int[] sub = new int[n+1];
        sub[1] = 1;
        sub[2] = 2;
        sub[3] = 3;
        for (int i = 4; i < n+1; i++){
            int max_val = 0;
            for (int j = 1; j < i/2+1; j++) max_val = Math.max(max_val,sub[j]*sub[i-j]);
            sub[i] = max_val;
        }
        return sub[n];
    }

    // No.15
    public int hammingWeight(int n){
        int ans = 0;
        while (n != 0){
            ans += 1;
            n = (n-1) & n;
        }
        return ans;
    }

    // No.16
    public double myPow(double x, int n){
        if (x == 0) return 0;
        long b = n;
        double res = 1.0;
        if (b < 0){
            x = 1 / x;
            b = -b;
        }
        while (b > 0){
            if ((b & 1) == 1) res *= x;
            x *= x;
            b >>= 1;
        }
        return res;
    }

    // No.18
    public ListNode deleteNode(ListNode head, int val){
        if (head.val == val) return head.next;
        ListNode pre = head, cur = head.next;
        while (cur != null && cur.val != val){
            pre = cur;
            cur = cur.next;
        }
        if (cur != null) pre.next = cur.next;
        return head;
    }

    // No.21
    public int[] exchange(int[] nums){
        int left = 0, right = nums.length -1, tmp;
        while(left < right){
            while(left < right && (nums[left] & 1) == 1) left++;
            while(left < right && (nums[right] & 1) == 0) right--;
            tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
        }
        return nums;
    }

    // No.22
    public ListNode getKthFromEnd(ListNode head, int k){
        if (head == null || k <= 0 ) return null;
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

    // No.24
    public ListNode reverseList(ListNode head){
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

    // No.25
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
        ListNode head = new ListNode(0);
        ListNode root = head;
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                root.next = l1;
                l1 = l1.next;
            }
            else{
                root.next = l2;
                l2 = l2.next;
            }
            root = root.next;
        }
        root.next = l1 != null? l1:l2;
        return head.next;
    }

    // No.26
    public boolean isSubStructure(TreeNode A, TreeNode B){
        return (A != null && B != null) &&
                (recur(A,B) || isSubStructure(A.left,B) || isSubStructure(A.right,B));
    }
    boolean recur(TreeNode A, TreeNode B){
        if (B == null) return true;
        if (A == null || A.val != B.val) return false;
        return recur(A.left, B.left) && recur(A.right,B.right);
    }

    // No.27
    public TreeNode mirrorTree(TreeNode root){
        if(root == null) return null;
        TreeNode tmp = root.left;
        root.left = mirrorTree(root.right);
        root.right = mirrorTree(tmp);
        return root;
    }

    // No.28
    public boolean isSymmetric(TreeNode root){
        return root == null? true:recur(root.left,root.right);
    }
    boolean recur(TreeNode L, TreeNode R){
        if(L == null && R == null) return true;
        if(L == null || R== null || L.val != R.val) return false;
        return recur(L.left,R.right) && recur(L.right,R.left);
    }

}
