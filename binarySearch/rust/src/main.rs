#![allow(dead_code)]
// rust还不太熟，先抄着吧
fn main() {
    println!("Hello, world!");
}


//  https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
//  time 20210615
pub fn count_negatives1(grid:Vec<Vec<i32>>) ->i32{
    grid.iter()
        .flatten()
        .filter(|item| **item < 0)
        .count() as i32
}

pub fn count_negatives2(grid:Vec<Vec<i32>>) ->i32{
    grid.iter().map(|x|{
        x.iter().filter(|a|(**a).is_negative()).count() as i32
    }).fold(0,|acc,x| acc + x)
}

