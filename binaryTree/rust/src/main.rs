use std::cell::RefCell;

// rust还不太熟，先抄着吧
use std::rc::Rc;
// use std::cell::RefCell;
fn main() {
    println!("Hello, world!");
}

// Definition for a binary tree node
#[derive(Debug, PartialEq,Eq)]
pub struct  TreeNode{
    pub val:i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) ->Self{
        TreeNode{
            val,
            left:None,
            right:None
        }
    }
}
type Node = Rc<RefCell<TreeNode>>;
impl Solution {
    fn preorder(node:Option<Node>, target:i32) -> Option<Node>{
        let mut stack = Vec::new();
        let mut result = Vec::new();
        stack.push(node);

        while let Some(node) = stack.pop(){
            if let Some(node) = node{
                if node.borrow().val == target{return Some(node.clone());};

                result.push(node.clone());
                stack.push(node.borrow().right.clone());
                stack.push(node.borrow().left.clone());
            }
        }
        None
    }
    pub fn search_bst(root:Option<Node>, val:I32) ->Option<Node>{
        Self::preorder(root,val)
    }
}


impl Solution {
    pub fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = &root{
            if node.borrow().val == val{
                return root;
            }else if node.borrow().val < val{
                return Self::search_bst(node.borrow().right.clone(),val);
            }
            return Self::search_bst(node.borrow().left.clone(),val);
        }else{
            return None;
        }
    }
}

impl Solution {
    pub fn search_bst(mut root:Option<Rc<RefCell<TreeNode>>>, val:i32) -> Option<Rc<RefCell<TreeNode>>>{
        while let Some(node) = root{
            if node.borrow().val < val{
                root = node.borrow().right.clone();
            }else if node.borrow().val > val{
                root = node.borrow().left.clone();
            }else {
                return Some(node);
            }
        }
        None
    }
}


impl Solution{
    pub fn search_bst(root:Option<Rc<RefCell<TreeNode>>>,val:i32) -> Option<Rc<RefCell<TreeNode>>>{
        if let Some(node) = &root{
            if node.borrow().val < val{
                return Self::search_bst(node.borrow().right.clone(),val);
            }else if node.borrow().val  > val{
                return Self::search_bst(node.borrow().left.clone(),val);
            }
        }
        root
    }
}
